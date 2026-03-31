namespace StationeersPyTrapIC;

using System;
using System.Collections.Generic;

using System.IO;
using System.Diagnostics;
using System.Threading.Tasks;
using Cysharp.Threading.Tasks;
using StationeersIC10Editor;
using ImGuiEditor.LSP;

public class PythonFormatter : LSPFormatter
{
    private PythonCompiler.CompileResponse lastCompileResponse = null;
    private long _lastResponseVersion = -1;

    public int DebounceDelayMs = 100;
    private static Object _Mutex = new();

    protected static LspClient _sharedLspClient = null;

    public static StaticFormatter StaticFormatter = new PythonStaticFormatter();

    public Editor _IC10Editor = null;
    public Editor IC10Editor
    {
        get
        {
            if (_IC10Editor == null)
            {
                var tab = Editor.ParentTab;
                tab.ClearExtraEditors();
                _IC10Editor = new Editor(Editor.KeyHandler);
                _IC10Editor.IsReadOnly = true;
                tab.AddEditor(_IC10Editor);
            }
            return _IC10Editor;
        }
    }

    public static string WorkspacePath => PythonWorkspace.WorkspaceDir;

    public static LspClient StartTyLSPServer()
    {
        // experimental support, not used currently
        string Args = "server";
        var startInfo = new ProcessStartInfo
        {
            FileName = PythonWorkspace.TyExe,
            Arguments = Args,
            RedirectStandardInput = true,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true,
            WorkingDirectory = PythonWorkspace.VenvDir
        };

        startInfo.Environment["PYTHONPATH"] = PythonWorkspace.SitePackagesDir;

        var rootURI = new Uri(WorkspacePath).AbsoluteUri;

        var initializationOptions = new
        {
            completions = new { autoImport = false },
            // logFile = Path.Combine(WorkspacePath, "ty.log"),
            // logLevel = "trace",
        };

        var lsp = new LspClientStdio(startInfo, initializationOptions, rootURI);
        lsp.OnInitialized += () =>
        {
            lsp.SendNotificationAsync("workspace/didChangeConfiguration", new
            {
                settings = new Dictionary<string, object>
                {
                    ["ty.completions.autoImport"] = false
                }
            }).Forget();
        };
        return lsp;
    }

    public static LspClient SharedLspClient
    {
        get
        {
            if (_sharedLspClient == null)
            {
                _sharedLspClient = StartTyLSPServer();
                _sharedLspClient.OnInfo += (msg) => L.Debug($"[Shared LSP] {msg}");
                _sharedLspClient.OnError += (msg) => L.Debug($"[Shared LSP] {msg}");
            }
            return _sharedLspClient;
        }
    }

    public static object Mutex { get => _Mutex; set => _Mutex = value; }

    public static void DisposeSharedLspClient()
    {
        _sharedLspClient?.Dispose();
        _sharedLspClient = null;
    }

    public PythonFormatter()
        : base()
    {
        Identifier = new VersionedTextDocumentIdentifier { uri = null, version = 1 };
        OnCodeChanged = (Action)Delegate.Combine(SubmitChanges, OnCodeChanged);

        LspClient = SharedLspClient;
        LspClient.OnDiagnostics += UpdateDiagnostics;
        LspClient.OnInitialized += () =>
        {
            Identifier.uri = null;
            SubmitChanges();
            ResetCodeDebounced().Forget();
        };
        if (LspClient.IsInitialized)
            ResetCodeDebounced().Forget();
        OnCodeChanged += () =>
        {
            UniTask.RunOnThreadPool(() => ResetCodeDebounced());
            lastCompileResponse = null;
        };
    }

    public async UniTask WriteLibraries()
    {
        if (Editor.ParentTab == null)
            return;
        await Editor.ParentTab.ParentWindow.LoadLibraries();

        var libs = Editor.ParentTab.ParentWindow.LibraryCodes;

        if (libs == null)
        {
            L.Debug("Library codes is null");
            return;
        }

        string initPath = Path.Combine(WorkspacePath, "library", "__init__.py");
        Directory.CreateDirectory(Path.GetDirectoryName(initPath));
        File.WriteAllText(initPath, "# Init file for libs package\n");
        File.WriteAllText(Path.Combine(WorkspacePath, "__init__.py"), "\n");

        string libPath = Path.Combine(WorkspacePath, "library");

        foreach (var lib in libs)
        {
            if (!lib.Instructions.Contains("stationeers_pytrapic"))
                continue;

            string fileName = lib.Title;
            foreach (char c in " ._<>:\"/\\|?*")
                fileName = fileName.Replace(c, '_');
            var filePath = Path.Combine(libPath, fileName + ".py");
            File.WriteAllText(filePath, lib.Instructions);
        }
    }

    public override void SubmitChanges()
    {
        if (Identifier.uri == null)
        {
            if (!Editor.IsReadOnly)
                WriteLibraries().Forget();
            string filename = Editor.FileName + ".py";
            Identifier.uri = new Uri(Path.Combine(WorkspacePath, filename)).AbsoluteUri;
        }
        base.SubmitChanges();
    }


    public static double MatchingScore(string code)
    {
        if (code.StartsWith("from stationeers_pytrapic.symbols import *"))
            return 1.0;

        if (code.Contains(SOURCE_TAG))
            return 1.0;

        if (code.Contains("stationeers_pytrapic"))
            return 0.7;

        return 0.0;
    }

    public async UniTaskVoid ResetCodeDebounced()
    {
        if (Lines.Count == 0 || Lines.Count == 1 && string.IsNullOrWhiteSpace(Lines[0].Text))
            return;

        await UniTask.SwitchToMainThread();
        SubmitChanges();
        await UniTask.SwitchToThreadPool();

        await PythonCompiler.Instance.WaitForReadyAsync();
        int versionBefore = Version;
        await Task.Delay(DebounceDelayMs);

        if (versionBefore != Version)
            return;

        string code = RawText;

        if (versionBefore != Version)
            return;

        lock (Mutex)
        {
            if (versionBefore != Version)
            {
                L.Debug("Newer debounce task detected, cancelling this one.");
                return;
            }
            L.Debug($"Debounce delay elapsed, proceeding with code reset.");

            var sw = System.Diagnostics.Stopwatch.StartNew();
            var response = PythonCompiler.Instance.Compile(code);
            sw.Stop();
            L.Debug($"Compilation took {sw.ElapsedMilliseconds} ms");
            if (versionBefore != Version)
            {
                L.Debug("Code changed during compilation, cancelling this one.");
                return;
            }
            lastCompileResponse = response;
            _lastResponseVersion = versionBefore;
        }

        var compiled = lastCompileResponse.code ?? "";
        var error = lastCompileResponse.error;
        if (error != null)
            compiled = $"# Error during compilation at line {error.line - 1}, column {error.column - 1}:\n# {error.description.Replace("\n", "\n# ")}\n\n" + compiled;

        await UniTask.SwitchToMainThread();
        L.Debug($"Applying compiled code to IC10 editor, editor = {IC10Editor}");
        IC10Editor.ResetCode(compiled, false);
    }

    public override StyledLine ParseLine(string line)
    {
        return StaticFormatter.ParseLine(line);
    }

    const string SOURCE_TAG = "PYTRAPIC_SOURCE";

    public override void ResetCode(string code)
    {
        // L.Debug($"ResetCode called in PythonFormatter. CODE: |{code}|");
        var pyCode = ExtractEncodedSource(code, SOURCE_TAG);
        // L.Debug($"pyCode : |{pyCode}|");
        if (!string.IsNullOrEmpty(pyCode))
            code = pyCode;
        base.ResetCode(code);
    }

    public override string Compile()
    {
        for (var itry = 0; itry < 10; itry++)
        {
            if (_lastResponseVersion == Version && lastCompileResponse != null)
                break;
            System.Threading.Thread.Sleep(100);
        }

        var code = "Error compiling Python source.\n";
        if (_lastResponseVersion == Version && lastCompileResponse != null)
        {
            code = lastCompileResponse.code + "\n\n" + EncodeSource(RawText, SOURCE_TAG);
        }
        else
        {
            L.Debug("Timeout waiting for compilation result.");
            L.Debug($"Last response version: {_lastResponseVersion}, Current version: {Version}");
        }

        return code;
    }

    private TextPosition _lastHoverTextPos = new TextPosition(-1, -1);
    private StyledText _lastHoverInfo = null;
    private TextPosition _reqestedHoverPos = new TextPosition(-1, -1);

    public async UniTaskVoid GetHoverInfo(TextPosition pos)
    {
        if (pos.Line < 0 || pos.Col < 0)
            return;

        if (pos == _lastHoverTextPos || pos == _reqestedHoverPos)
            return;

        _reqestedHoverPos = pos;

        await Task.Delay(500);

        if (_reqestedHoverPos != pos)
            return;

        _tooltip = null;
        _lastHoverInfo = null;

        var hover = await LspClient.SendRequestAsync("textDocument/hover",
            new
            {
                textDocument = new { uri = Identifier.uri },
                position = new { line = pos.Line, character = pos.Col }
            });

        if (hover == null || !hover.HasValues || hover["contents"] == null)
            return;
        string value = (string)hover["contents"]["value"];
        var info = new StyledText();
        foreach (var line in value.Split('\n'))
            info.AddLine(line, ICodeFormatter.DefaultStyle);

        if (info.Count == 0)
            return;

        _lastHoverInfo = info;

        if (pos == _reqestedHoverPos)
        {
            await UniTask.SwitchToMainThread();
            _lastHoverTextPos = pos;
            UpdateTooltip(pos);
        }
    }

    public override void UpdateTooltip(TextPosition mouseTextPos)
    {
        if (_lastHoverTextPos != mouseTextPos)
        {
            _lastHoverInfo = null;
            GetHoverInfo(mouseTextPos).Forget();
        }

        base.UpdateTooltip(mouseTextPos);
        if (_lastHoverInfo != null)
        {
            var tooltip = new StyledText();
            if (_tooltip != null)
                tooltip.AddRange(_tooltip);
            tooltip.AddRange(_lastHoverInfo);
            _tooltip = tooltip;
        }
    }
}
