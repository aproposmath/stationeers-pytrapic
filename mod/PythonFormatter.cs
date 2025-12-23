namespace StationeersPyTrapIC;

using System;
using System.IO;
using System.Threading.Tasks;
using Cysharp.Threading.Tasks;
using StationeersIC10Editor;
using ImGuiEditor.LSP;


public class PythonFormatter : LSPFormatter
{
    private PythonCompiler.CompileResponse lastCompileResponse = null;
    private long _lastResponseVersion = -1;

    public int DebounceDelayMs = 100;
    private System.Object _Mutex = new System.Object();

    protected static LspClient _sharedLspClient = null;

    protected static StaticFormatter StaticFormatter = new PythonStaticFormatter();

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

    public static string WorkspacePath
    {
        get
        {
            string path = Path.Combine(BepInEx.Paths.CachePath, "pytrapic", "ws");
            Directory.CreateDirectory(path);
            return path;
        }
    }

    public static LspClient SharedLspClient
    {
        get
        {
            if (_sharedLspClient == null)
            {
                _sharedLspClient = LspClient.StartBasedPyrightLSPServer();
                _sharedLspClient.OnInfo += (msg) => L.Debug($"[Shared LSP] {msg}");
                _sharedLspClient.OnError += (msg) => L.Debug($"[Shared LSP] {msg}");
            }
            return _sharedLspClient;
        }
    }

    public PythonFormatter()
        : base()
    {
        Identifier = new VersionedTextDocumentIdentifier { uri = null, version = 1 };
        OnCodeChanged = (Action)Delegate.Combine(SubmitChanges, OnCodeChanged);

        LspClient = SharedLspClient;
        LspClient.OnDiagnostics += UpdateDiagnostics;
        LspClient.OnInitialized += () => { SubmitChanges(); };
        if (LspClient.IsInitialized)
            ResetCodeDebounced().Forget();
        OnCodeChanged += () =>
        {
            UniTask.RunOnThreadPool(() => ResetCodeDebounced());
            lastCompileResponse = null;
        };
    }

    public override void SubmitChanges()
    {
        if (Identifier.uri == null)
        {
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

        SubmitChanges();

        await PythonCompiler.Instance.WaitForReadyAsync();
        int versionBefore = Version;
        await Task.Delay(DebounceDelayMs);

        if (versionBefore != Version)
            return;

        string code = RawText;

        if (versionBefore != Version)
            return;

        lock (_Mutex)
        {
            if (versionBefore != Version)
            {
                L.Info("Newer debounce task detected, cancelling this one.");
                return;
            }
            L.Info($"Debounce delay elapsed, proceeding with code reset.");

            var sw = System.Diagnostics.Stopwatch.StartNew();
            var response = PythonCompiler.Instance.Compile(code);
            sw.Stop();
            L.Info($"Compilation took {sw.ElapsedMilliseconds} ms");
            if (versionBefore != Version)
            {
                L.Info("Code changed during compilation, cancelling this one.");
                return;
            }
            lastCompileResponse = response;
            _lastResponseVersion = versionBefore;
        }

        var compiled = lastCompileResponse.code ?? "";
        await UniTask.SwitchToMainThread();
        L.Info($"Applying compiled code to IC10 editor, editor = {IC10Editor}");
        IC10Editor.ResetCode(compiled);
    }

    public override StyledLine ParseLine(string line)
    {
        return StaticFormatter.ParseLine(line);
    }

    const string SOURCE_TAG = "PYTRAPIC_SOURCE";

    public override void ResetCode(string code)
    {
        L.Info($"ResetCode called in PythonFormatter. CODE: |{code}|");
        var pyCode = ExtractEncodedSource(code, SOURCE_TAG);
        L.Info($"pyCode : |{pyCode}|");
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
            L.Info("Timeout waiting for compilation result.");
            L.Info($"Last response version: {_lastResponseVersion}, Current version: {Version}");
        }

        return code;
    }
}
