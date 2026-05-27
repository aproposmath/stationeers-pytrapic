namespace StationeersPyTrapIC;

using System;
using System.Collections.Generic;
using System.Collections.Concurrent;

using System.IO;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Threading;
using Cysharp.Threading.Tasks;
using StationeersIC10Editor;
using ImGuiEditor.LSP;
using ImGuiNET;
using BepInEx.Configuration;

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
                _IC10Editor.CodeFormatter = new StationeersIC10Editor.IC10.IC10CodeFormatter();
                _IC10Editor.CodeFormatter.Editor = _IC10Editor;
                _IC10Editor.CodeFormatter.OnCaretMoved += () => UpdateHighlightedIC10Lines();
            }
            return _IC10Editor;
        }
    }

    public StationeersIC10Editor.IC10.IC10CodeFormatter IC10Formatter => IC10Editor.CodeFormatter as StationeersIC10Editor.IC10.IC10CodeFormatter;

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
                // _sharedLspClient.OnInfo += (msg) => L.Debug($"[Shared LSP] {msg}");
                // _sharedLspClient.OnError += (msg) => L.Debug($"[Shared LSP] {msg}");
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

        OnCaretMoved += UpdateHighlightedIC10Lines;
    }

    public async UniTask WriteLibraries()
    {
        if (Editor.ParentTab == null)
            return;

        var libs = LibraryWindow.VersionedScripts;

        string initPath = Path.Combine(WorkspacePath, "library", "__init__.py");
        Directory.CreateDirectory(Path.GetDirectoryName(initPath));
        File.WriteAllText(initPath, "# Init file for libs package\n");
        File.WriteAllText(Path.Combine(WorkspacePath, "__init__.py"), "\n");

        string libPath = Path.Combine(WorkspacePath, "library");

        foreach (var lib in libs)
        {
            if (!lib.Data.Instructions.Contains("stationeers_pytrapic"))
                continue;

            string fileName = lib.Title;
            foreach (char c in " ._<>:\"/\\|?*")
                fileName = fileName.Replace(c, '_');
            var filePath = Path.Combine(libPath, fileName + ".py");
            File.WriteAllText(filePath, lib.Data.Instructions);
        }
    }

    public override void SubmitChanges()
    {
        lock (Mutex)
        {
            if (Identifier.uri == null)
            {
                if (!Editor.IsReadOnly)
                    WriteLibraries().Forget();
                string filename = Editor.FileName.Replace('|', '/') + ".py";
                L.Debug($"Setting document URI to {filename}");
                Identifier.uri = new Uri(Path.Combine(WorkspacePath, filename)).AbsoluteUri;
            }
            base.SubmitChanges();
        }
    }

    public static double MatchingScore(string input)
    {
        var trimmed = input.Trim();

        if (trimmed.StartsWith("from stationeers_pytrapic.symbols import *") || trimmed.Contains(SOURCE_TAG))
            return 1.0;

        if (trimmed.Contains("stationeers_pytrapic"))
            return 0.7;

        if (string.IsNullOrEmpty(trimmed))
            return 0.0;

        var lines = trimmed.Split('\n');
        double score = 0.0;

        if (lines[0].Contains("import"))
        {
            score += 0.5 * lines.Length;
            if (lines[0].Contains("from"))
                score += 0.5 * lines.Length;
            if (lines[0].EndsWith("*"))
                score += 0.5 * lines.Length;
        }

        foreach (var line in lines)
        {
            var trimmedLine = line.TrimStart();

            if (trimmedLine.EndsWith(":"))
                score += 1;
            if (trimmedLine.StartsWith("def "))
                score += 1;
            if (trimmedLine.StartsWith("if") || trimmedLine.StartsWith("elif") || trimmedLine.StartsWith("else") || trimmedLine.StartsWith("for ") || trimmedLine.StartsWith("while "))
                score += 0.5;
            if (trimmedLine.StartsWith("#"))
                score += 0.2;
        }
        return score / lines.Length;
    }

    private static readonly ConcurrentDictionary<string, PythonCompiler.CompileResponse> _CompileCache = [];
    private static readonly Queue<string> _CompileCacheKeys = [];

    public async UniTask<PythonCompiler.CompileResponse> CompileCode(string code)
    {
        var options = PythonCompiler.options.Copy();
        var cacheKey = options.ToString() + "|" + code;
        if (_CompileCache.TryGetValue(cacheKey, out var cachedResponse))
            return cachedResponse;
        var sw = Stopwatch.StartNew();
        if (PythonCompiler.Instance == null)
        {
            PythonCompiler.Instance = new PythonCompiler();
            await PythonCompiler.Instance.Init();
        }
        await UniTask.SwitchToThreadPool();
        await PythonCompiler.Instance.WaitForReadyAsync();
        var response = PythonCompiler.Instance.Compile(code, options);
        sw.Stop();
        L.Debug($"Compilation took {sw.ElapsedMilliseconds} ms");
        lastCompileResponse = response;
        _CompileCache[cacheKey] = response;
        _CompileCacheKeys.Enqueue(code);
        while (_CompileCacheKeys.Count > 100)
            _CompileCache.TryRemove(_CompileCacheKeys.Dequeue(), out _);
        return response;
    }

    public async UniTaskVoid ResetCodeDebounced()
    {
        if (Lines.Count == 0 || Lines.Count == 1 && string.IsNullOrWhiteSpace(Lines[0].Text))
            return;

        // await UniTask.SwitchToMainThread();
        SubmitChanges();

        // This is the case for the library preview, we don't want to compile and show the IC10 code in this case
        if (Editor.IsReadOnly)
            return;

        await UniTask.SwitchToThreadPool();

        int versionBefore = Version;
        await Task.Delay(DebounceDelayMs);

        L.Debug($"ResetCodeDebounced called, Version: {Version}, versionBefore: {versionBefore}, _lastResponseVersion: {_lastResponseVersion}");

        if (versionBefore != Version)
            return;

        string code = RawText;

        L.Debug("Starting compilation of code from ResetCodeDebounced...");

        var response = await CompileCode(code);

        L.Debug($"Compilation finished in ResetCodeDebounced with response: {response?.code}, error: {response?.error}, versionBefore: {versionBefore}, current Version: {Version}");

        if (versionBefore != Version)
            return;
        L.Debug($"Applying compilation result from ResetCodeDebounced, versionBefore: {versionBefore}, current Version: {Version}");
        lastCompileResponse = response;
        _lastResponseVersion = versionBefore;

        var compiled = lastCompileResponse.code ?? "";
        var error = lastCompileResponse.error;
        if (error != null)
            compiled = $"# Error during compilation at line {error.line - 1}, column {error.column - 1}:\n# {error.description.Replace("\n", "\n# ")}\n\n" + compiled;

        await UniTask.SwitchToMainThread();
        L.Debug($"Applying compiled code to IC10 editor, editor = {IC10Editor}");
        IC10Editor.CaretPos = new TextPosition(0, 0);
        IC10Formatter.ResetCode(compiled);
        IC10Formatter.OnCodeChanged();
        IC10Formatter.OnCaretMoved();
        UpdateHighlightedIC10Lines();
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
        if (_lastResponseVersion == -1)
            ResetCodeDebounced().Forget();

        for (var itry = 0; itry < 20; itry++)
        {
            if (_lastResponseVersion == Version && lastCompileResponse != null)
                break;
            Thread.Sleep(100);
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
        if (!_isOpen || pos.Line < 0 || pos.Col < 0)
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

    private void DrawCheckBox(string label, ConfigEntry<bool> entry, ref bool value)
    {
        if (ImGuiUtils.Checkbox(label, ref value, entry.Description.Description))
        {
            entry.Value = value;
            ResetCodeDebounced().Forget();
        }
    }

    public override void DrawButtons()
    {
        DrawCheckBox("Inline", PyTrapICPlugin.InlineFunctions, ref PythonCompiler.options.inline_functions);
        ImGui.SameLine();
        DrawCheckBox("No Labels", PyTrapICPlugin.RemoveLabels, ref PythonCompiler.options.remove_labels);
        ImGui.SameLine();
        DrawCheckBox("Compact", PyTrapICPlugin.CompactOutput, ref PythonCompiler.options.compact);
        ImGui.SameLine();
        DrawCheckBox("Indent", PyTrapICPlugin.IndentOutput, ref PythonCompiler.options.indent);
        ImGui.SameLine();
        var pos = ImGui.GetCursorScreenPos();

        if (lastCompileResponse != null)
        {
            var str = $" {lastCompileResponse.num_registers} registers";
            ImGui.GetWindowDrawList().AddText(pos + new UnityEngine.Vector2(-ImGui.CalcTextSize(str).x - 0.5f * Settings.CharWidth, Settings.LineHeightWithSpacing), 0xffffffff, str);
        }
    }

    public static uint ColorBackground = ColorFromHTML("#000080");

    public void UpdateHighlightedIC10Lines()
    {
        var lineStyles = IC10Editor.CodeFormatter.LineStyles;
        var style = new Style { Background = ColorBackground };
        foreach (var i in new List<int>(lineStyles.Keys))
        {
            var lineStyle = lineStyles[i];
            if (lineStyle.Equals(style))
                lineStyles.Remove(i);
            else if (lineStyle.Background == style.Background)
                lineStyles[i] = new Style { Color = lineStyle.Color };
        }

        if (lastCompileResponse == null || lastCompileResponse.source_mapping == null)
            return;

        if (lastCompileResponse.source_mapping.TryGetValue(_lastCaretPos.Line, out var ic10LineNumbers))
            foreach (var ic10Line in ic10LineNumbers)
            {
                if (lineStyles.ContainsKey(ic10Line))
                    lineStyles[ic10Line] = new Style { Color = lineStyles[ic10Line].Color, Background = ColorBackground };
                else
                    lineStyles[ic10Line] = style;
            }
    }
}
