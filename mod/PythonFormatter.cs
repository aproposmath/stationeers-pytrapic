namespace StationeersPyTrapIC;

using System;
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
    private static System.Object _Mutex = new System.Object();

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

    public static string WorkspacePath => PythonWorkspace.WorkspaceDir;

    public static LspClient StartBasedPyrightLSPServer()
    {
        // open a socket and listen
        var listener = new System.Net.Sockets.TcpListener(System.Net.IPAddress.Loopback, 0);
        listener.Start();
        int port = ((System.Net.IPEndPoint)listener.LocalEndpoint).Port;
        StationeersIC10Editor.L.Debug("BasedPyright LSP server listening on port " + port);

        var lspClient = new LspClient();

        UniTask.RunOnThreadPool(async () =>
        {
            var client = await listener.AcceptTcpClientAsync();
            StationeersIC10Editor.L.Debug("BasedPyright LSP server accepted connection.");
            // get stream
            var stream = client.GetStream();
            lspClient.Init(stream, stream);
        }).Forget();


        string workingDir = Path.Combine(BepInEx.Paths.CachePath, "pytrapic");
        // string PyRightExe = Path.Combine(workingDir, ".venv", "Scripts", "basedpyright-langserver.exe");
        string SiteDir = Path.Combine(PythonWorkspace.VenvDir, "Lib", "site-packages");
        string NodeExe = Path.Combine(SiteDir, "nodejs_wheel", "node.exe");
        string PyRightJS = Path.Combine(SiteDir, "basedpyright", "langserver.index.js");
        string Args = $"{PyRightJS} --no-warnings --title \"abc\" --verbose --socket={port}";
        // string Args = "--stdio";
        var startInfo = new ProcessStartInfo
        {
            FileName = NodeExe,
            Arguments = Args,
            RedirectStandardInput = true,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = false,
            WorkingDirectory = workingDir
        };

        var process = new Process
        {
            StartInfo = startInfo,
            EnableRaisingEvents = true
        };

        process.OutputDataReceived += (s, e) =>
        {
            if (e.Data != null)
                File.AppendAllText("pr-stdout.log", e.Data + Environment.NewLine);
        };

        process.ErrorDataReceived += (s, e) =>
        {
            if (e.Data != null)
                File.AppendAllText("pr-stderr.log", e.Data + Environment.NewLine);
        };

        process.Start();
        process.BeginOutputReadLine();
        process.BeginErrorReadLine();

        lspClient._process1 = process;

        return lspClient;
    }

    public static LspClient SharedLspClient
    {
        get
        {
            if (_sharedLspClient == null)
            {
                _sharedLspClient = StartBasedPyrightLSPServer();
                _sharedLspClient.OnInfo += (msg) => L.Debug($"[Shared LSP] {msg}");
                _sharedLspClient.OnError += (msg) => L.Debug($"[Shared LSP] {msg}");
            }
            return _sharedLspClient;
        }
    }

    public static void DisposeSharedLspClient()
    {
        if (_sharedLspClient != null)
        {
            _sharedLspClient._process1.Kill();
            _sharedLspClient = null;
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

    public async UniTask WriteLibraries()
    {
        await Editor.ParentTab.ParentWindow.LoadLibraries();

        var libs = Editor.ParentTab.ParentWindow.LibraryCodes;

        if (libs == null)
        {
            L.Info("Library codes is null");
            return;
        }

        string initPath = Path.Combine(WorkspacePath, "library", "__init__.py");
        Directory.CreateDirectory(Path.GetDirectoryName(initPath));
        File.WriteAllText(initPath, "# Init file for libs package\n");
        File.WriteAllText(Path.Combine(WorkspacePath, "__init__.py"), "\n");

        string libPath = Path.Combine(WorkspacePath, "library");

        foreach (var kvp in libs)
        {
            if(!kvp.Value.Instructions.Contains("stationeers_pytrapic"))
              continue;

            string fileName = kvp.Key;
            foreach (char c in " ._<>:\"/\\|?*")
                fileName = fileName.Replace(c, '_');
            var filePath = Path.Combine(libPath, fileName + ".py");
            File.WriteAllText(filePath, kvp.Value.Instructions);
        }
    }

    public override void SubmitChanges()
    {
        if (Identifier.uri == null)
        {
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

        lock (_Mutex)
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
        await UniTask.SwitchToMainThread();
        L.Debug($"Applying compiled code to IC10 editor, editor = {IC10Editor}");
        IC10Editor.ResetCode(compiled);
    }

    public override StyledLine ParseLine(string line)
    {
        return StaticFormatter.ParseLine(line);
    }

    const string SOURCE_TAG = "PYTRAPIC_SOURCE";

    public override void ResetCode(string code)
    {
        L.Debug($"ResetCode called in PythonFormatter. CODE: |{code}|");
        var pyCode = ExtractEncodedSource(code, SOURCE_TAG);
        L.Debug($"pyCode : |{pyCode}|");
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
}
