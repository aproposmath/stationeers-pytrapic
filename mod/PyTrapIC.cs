using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;
using Assets.Scripts.Networking;
using Assets.Scripts.Networking.Transports;
using Assets.Scripts.UI;
using BepInEx;
using BepInEx.Logging;
using Cysharp.Threading.Tasks;
using Newtonsoft.Json;
using StationeersIC10Editor;
using Util.Commands;

namespace StationeersPyTrapIC
{
    public class Timer : IDisposable
    {
        public Stopwatch stopwatch;
        public string name;

        public Timer(string name)
        {
            this.name = name;
            stopwatch = Stopwatch.StartNew();
        }

        public void Dispose()
        {
            stopwatch.Stop();
            L.Debug($"{name} took {stopwatch.ElapsedMilliseconds}ms");
        }
    }

    public class PediaPage
    {
        public string key;
        public string title;
        public string text;
    }

    public class SourceData
    {
        public static bool IsPythonCode(string code)
        {
            return code != null && code.StartsWith("from stationeers_pytrapic.symbols import *");
        }

        public static bool IsLuaCode(string code)
        {
            return code != null && code.StartsWith("require");
        }

        public static bool NeedsCompile(string code)
        {
            return IsPythonCode(code) || IsLuaCode(code);
        }

        public static string getImportRegex(string code)
        {
            if (IsPythonCode(code))
            {
                // return @"^\s*import\s+library\.(\w+)\s*$";
                // return @"^\s*from\s+\.library\.(\w+)\s+import\s+\*\s*$";
                return @"^\s*from\s+\.library\s+import\s+(\w+)\s*$";
            }
            if (IsLuaCode(code))
            {
                return @"require\s*[""']library\.(?:[A-Za-z0-9_]+\.)*([A-Za-z0-9_]+)[""']";
            }
            return @"$^"; // matches nothing
        }

        public static Dictionary<string, SteamTransport.ItemWrapper> loadLibraries()
        {
            using (new Timer("Load libraries"))
            {
                // todo: can we cache this without missing updates?
                // todo: can this be loaded async without blocking?

                var libraries = NetworkManager
                    .GetLocalAndWorkshopItems(SteamTransport.WorkshopType.ICCode)
                    .GetAwaiter()
                    .GetResult();

                Dictionary<string, SteamTransport.ItemWrapper> libraryMap =
                    new Dictionary<string, SteamTransport.ItemWrapper>();

                foreach (var lib in libraries)
                    libraryMap[lib.DirectoryName.ToLowerInvariant()] = lib;

                return libraryMap;
            }
        }

        public static Dictionary<string, string> LoadImportedModules(string code)
        {
            var importRegex = new Regex(getImportRegex(code), RegexOptions.Multiline);

            var firstMatches = importRegex.Matches(code);

            Dictionary<string, string> result = new Dictionary<string, string>();
            result[""] = code;

            if (firstMatches.Count == 0)
            {
                return result; // No library imports found
            }

            var libraries = loadLibraries();

            List<string> codesToSearch = new List<string>();
            codesToSearch.Add(code);

            while (codesToSearch.Count > 0)
            {
                string nextCode = codesToSearch[0];
                codesToSearch.RemoveAt(0);
                var matches = importRegex.Matches(nextCode);
                foreach (Match match in matches)
                {
                    string libName = match.Groups[1].Value.ToLowerInvariant();

                    if (result.ContainsKey(libName))
                        continue; // Already imported

                    if (!libraries.ContainsKey(libName))
                    {
                        L.Error($"Library {libName} not found in library map, skipping import");
                        continue; // Library not found, skip replacement
                    }

                    var lib = libraries[libName];
                    L.Debug($"Found matching library {libName}: {lib.FilePathFullName}");
                    InstructionData instructionData = InstructionData.GetFromFile(
                        lib.FilePathFullName
                    );

                    result[libName] = instructionData.Instructions;
                    codesToSearch.Add(instructionData.Instructions);
                    // code = code.Replace(match.Value, instructionData.Instructions);
                }
            }

            return result;
        }

        public string PythonCode { get; set; }
        public string IC10Code { get; set; }

        public string Serialize()
        {
            return JsonConvert.SerializeObject(this);
        }

        public void Deserialize(string json)
        {
            var obj = JsonConvert.DeserializeObject<SourceData>(json);
            PythonCode = obj.PythonCode;
            IC10Code = obj.IC10Code;
        }
    }

    public class PythonCompiler
    {
        public static readonly string PYTHON_VERSION = "3.13.7";
        public static PythonCompiler Instance = null;
        public static List<PediaPage> pages = new List<PediaPage>();

        public static CompileOptions options = new CompileOptions();

        private Process _process;
        private StreamWriter _stdin;
        private StreamReader _stdout;
        private string lastInput = "";
        private string lastOutput = "";

        public class CompileError
        {
            public string description;
            public int line = -1;
            public int column = -1;
            public int line_end = -1;
            public int column_end = -1;
        }

        public class CompileOptions
        {
            public bool original_code_as_comment = false;
            public bool generated_comments = false;
            public bool inline_functions = true;
            public bool remove_labels = true;
            public bool append_version = true;
            public bool compact = false;

            public CompileOptions Copy()
            {
                return (CompileOptions)this.MemberwiseClone();
            }
        }

        public class CompileInput
        {
            public string action = "compile";
            public Dictionary<string, string> code;
            public bool comments = false;
            public bool compact = true;
            public bool append_version = true;
            public int lineno = -1;
            public int column = -1;
            public CompileOptions options;
        }

        public class CompileResponse
        {
            public CompileError error;
            public string highlighted;
            public string code;
            public string suggestions;
            public string completion;
            public int completion_prefix_length;
            public int num_lines;
            public int num_registers;
            public int num_bytes;
            public CompileInput input;
        }

        public void StopProcess()
        {
            if (_process == null)
                return;
            L.Debug($"Stopping PythonCompiler instance, has quit already: {_process.HasExited}");
            if (!_process.HasExited)
            {
                _process.Kill();
            }
        }

        ~PythonCompiler()
        {
            StopProcess();
        }

        public bool IsRunning()
        {
            return _process != null && !_process.HasExited;
        }

        public async UniTaskVoid Init(bool forceRestart = false, bool forceInstall = false)
        {
            await UniTask.SwitchToThreadPool();
            if (IsRunning())
            {
                if (!forceRestart)
                    return;

                StopProcess();
            }
            await PythonWorkspace.InitWorkspace(forceInstall);
            L.Debug("Python installation checked");

            var pythonPath = PythonWorkspace.PythonExe;
            _process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = pythonPath,
                    Arguments = "-mstationeers_pytrapic.mod_daemon",
                    UseShellExecute = false,
                    RedirectStandardInput = true,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    CreateNoWindow = true,
                },
            };

            L.Debug($"Starting Python compiler at: ${pythonPath}");
            L.Debug($"Full command line : {_process.StartInfo.FileName} {_process.StartInfo.Arguments}");

            _process.Start();
            _stdin = _process.StandardInput;
            _stdout = _process.StandardOutput;
            if (_process.HasExited)
            {
                L.Error($"Tried to run python compiler at: ${pythonPath}");
                L.Error($"Python compiler process exited unexpectedly");
                throw new Exception("Python compiler process exited unexpectedly");
            }
            if (_stdout == null || _stdin == null)
            {
                L.Error($"Tried to run python compiler at: ${pythonPath}");
                L.Error($"Failed to get standard input/output streams from Python compiler");
                throw new Exception("Failed to get standard input/output streams");
            }

            var pagesResponse = await _stdout.ReadLineAsync();
            L.Debug($"Received Stationpedia pages from Python compiler");
            L.Debug($"Decoding Stationpedia pages {pagesResponse}");

            if (pagesResponse == null)
            {
                var errors = await _process.StandardError.ReadToEndAsync();
                L.Error($"Python compiler stderr: {errors}");
                L.Error($"No response from Python compiler for Stationpedia pages");
                throw new Exception("No response from Python compiler for Stationpedia pages");
            }
            L.Debug($"Pages response length: {pagesResponse.Length}");

            pages = JsonConvert.DeserializeObject<List<PediaPage>>(
                Encoding.UTF8.GetString((Convert.FromBase64String(pagesResponse)))
            );
            AddStationpediaPages();

            L.Debug($"PythonCompiler running");
            L.Debug($"Registered Python code formatter");
            L.Debug($"Get formatter {CodeFormatters.GetFormatter()}");
            _initTcs.TrySetResult();
        }

        public void AddStationpediaPages()
        {
            L.Debug($"Add {pages.Count} PyTrapIC pages to Stationpedia");
            foreach (var page in pages)
            {
                L.Debug($"Stationpedia page: {page.key} - {page.title}");
                var stationPediaPage = new StationpediaPage(page.key, page.title, page.text);
                stationPediaPage._parsed = page.text;
                stationPediaPage.Description = page.text;
                Stationpedia.Register(stationPediaPage);
            }
        }

        private readonly UniTaskCompletionSource _initTcs = new UniTaskCompletionSource();

        public UniTask WaitForReadyAsync() => _initTcs.Task;

        public PythonCompiler()
        {
            UniTask.RunOnThreadPool(() => Init());
        }

        public static void GetPosition(out int lineno, out int column)
        {
            try
            {
                var sc = InputSourceCode.Instance;
                string lineNrStr = sc.CurrentLine.LineNumber.text;
                lineno = 1 + Int32.Parse(lineNrStr.TrimEnd('.'));
                column = sc.CaretPosition;
                // L.Debug($"Caret position: {lineno}:{column}");
            }
            catch (Exception ex)
            {
                L.Error($"Error getting caret position: {ex}");
                lineno = -1;
                column = -1;
            }
        }

        public CompileResponse Compile(string pythonCode, int lineno = -1, int column = -1)
        {
            if (!IsRunning())
            {
                L.Error("Python compiler is not running, cannot compile");
                return new CompileResponse
                {
                    error = { description = "Python compiler is not running" },
                };
            }

            var modules = SourceData.LoadImportedModules(pythonCode);
            var compileOptions = options.Copy();

            CompileInput input = new CompileInput
            {
                action = "compile",
                code = modules,
                options = compileOptions,
                lineno = lineno,
                column = column,
            };

            var response = JsonConvert.DeserializeObject<CompileResponse>(
                SendData(JsonConvert.SerializeObject(input))
            );
            response.input = input;

            return response;
        }

        public string Highlight(string pythonCode)
        {
            if (!IsRunning())
            {
                L.Error("Python compiler is not running, cannot highlight");
                return pythonCode;
            }

            if (pythonCode.Length == 0)
                return pythonCode;

            CompileResponse data = Compile(pythonCode);

            if (data == null || data.highlighted == null)
            {
                L.Error($"Error highlighting code: {data?.error}");
                return pythonCode;
            }

            return data.highlighted;
        }

        public string SendCommand(string message)
        {
            var data = Convert.ToBase64String(Encoding.UTF8.GetBytes(message));
            _stdin.WriteLine(data);
            _stdin.Flush();

            // Read response
            string line = _stdout.ReadLine();
            if (line == null)
                return null;
            byte[] raw = Convert.FromBase64String(line);
            return Encoding.UTF8.GetString(raw);
        }

        private System.Object _sendDataLock = new System.Object();

        public string SendData(string data)
        {
            if (data == lastInput)
                return lastOutput;

            try
            {
                lock (_sendDataLock)
                {
                    L.Debug($"Sending data to Python compiler");
                    String response = null;
                    using (new Timer("Compile"))
                        response = SendCommand(data);
                    if (response == null)
                    {
                        L.Error($"No response from Python compiler, was sent: {data}");
                        return "Error: No response from Python compiler";
                    }
                    lastInput = data;
                    lastOutput = response;
                    return response;
                }
            }
            catch (Exception ex)
            {
                L.Error($"Error sending Python data: {ex}");
                return $"Error: {ex.Message}";
            }
        }
    }

    [BepInDependency(
        "aproposmath-stationeers-ic10-editor",
        BepInDependency.DependencyFlags.HardDependency
    )]
    [BepInPlugin(ThisModInfo.ModID, ThisModInfo.AssemblyName, ThisModInfo.Version)]
    public class PyTrapICPlugin : BaseUnityPlugin
    {
        private void Awake()
        {
            try
            {
                L.SetLogger(this.Logger);
                L.Info( $"Awake {ThisModInfo.Info}");
                var sw = Stopwatch.StartNew();

                PythonCompiler.Instance = new PythonCompiler();
                CommandLine.AddCommand("pytrapic", new PyTrapICCommand());

                sw.Stop();
                L.Debug(
                    $"PyTrapIC initialized in {sw.ElapsedMilliseconds}ms"
                );

                CodeFormatters.RegisterFormatter("Python", typeof(PythonFormatter));
            }
            catch (Exception ex)
            {
                L.Error($"Error during init of {ThisModInfo.Info}: {ex}");
            }
        }

        private void OnDestroy()
        {
            L.Info($"OnDestroy of ${ThisModInfo.Info}");
            PythonCompiler.Instance.StopProcess();
            PythonFormatter.DisposeSharedLspClient();
        }
    }

    class PyTrapICCommand : CommandBase
    {
        public override string HelpText =>
            @"Usage: pytrapic <command>

Available commands:
    help           Show this help message
    restart        Restart Python daemon for compiling
    status         Check if Python daemon is running
    libraries      List available libraries
    version        Show PyTrapIC version
    reinstall      Reinstall Python and dependencies
    debug_logging  Toggle debug logging";

        public override string[] Arguments { get; } = new string[] { };

        public override bool IsLaunchCmd { get; }

        public override string Execute(string[] args)
        {
            if (args.Length == 0 || args[0] == "help" || args.Length > 1)
            {
                return HelpText;
            }

            switch (args[0].ToLowerInvariant())
            {
                case "restart":
                    PythonCompiler.Instance.Init(true).Forget();
                    return "Python daemon restarted.";
                case "status":
                    return PythonCompiler.Instance.IsRunning()
                        ? "Python daemon is running."
                        : "Python daemon is not running.";
                case "libraries":
                    return string.Join("\n", SourceData.loadLibraries().Keys.OrderBy(x => x));
                case "version":
                    return $"PyTrapIC version {ThisModInfo.Version}, git version: {ThisModInfo.VersionGit}, Python {PythonCompiler.PYTHON_VERSION}";
                case "reinstall":
                    PythonCompiler.Instance.Init(true, true).Forget();
                    return "Python and dependencies reinstalled.";
                default:
                    return HelpText;
            }
        }
    }
}
