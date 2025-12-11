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
using Util.Commands;
using StationeersIC10Editor;

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
                return @"^\s*from\s+library\s+import\s+(\w+)\s*$";
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

    public static class L
    {
        private static ManualLogSource _logger;
#if DEBUG
        private static bool _debugEnabled = true;
#else
        private static bool _debugEnabled = false;
#endif

        public static string Timestamp => DateTime.Now.ToString("HH:mm:ss.fff - ");

        public static void Initialize(ManualLogSource logger)
        {
            _logger = logger;
        }

        public static bool ToggleDebug()
        {
            _debugEnabled = !_debugEnabled;
            return _debugEnabled;
        }

        public static void Log(string message)
        {
            _logger?.LogMessage(Timestamp + message?.ToString());
        }

        public static void Info(object msg)
        {
            _logger?.LogInfo(Timestamp + msg?.ToString());
        }

        public static void Error(object msg)
        {
            _logger?.LogError(Timestamp + msg?.ToString());
        }

        public static void Debug(object msg)
        {
            if (!_debugEnabled)
                return;
            _logger?.LogDebug(Timestamp + msg?.ToString());
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

        private void StopProcess()
        {
            if (_process == null)
                return;
            L.Info("Stopping PythonCompiler instance");
            if (!_process.HasExited)
            {
                _stdin?.WriteLine("EXIT");
                System.Threading.Thread.Sleep(100);
                if (!_process.HasExited)
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

        public string GetCacheDir()
        {
            return Path.Combine(BepInEx.Paths.CachePath, "pytrapic");
        }

        public string GetVenvDir()
        {
            return Path.Combine(GetCacheDir(), $"venv");
        }

        public string GetPythonExePath()
        {
            return Path.Combine(GetVenvDir(), "python.exe");
        }

        public void UpdatePythonModules(bool force = false)
        {
#if DEBUG
            // I'm using symlinks to the python sources for development
            return;
#endif
            // Todo: check for verison number and build time, do this only when changed
            string modulesZipDir = Path.Combine(
                Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
                "pytrapic_python_modules.zip"
            );
            string extractDir = Path.Combine(GetVenvDir(), "site-packages");
            if (Directory.Exists(extractDir))
                Directory.Delete(extractDir, recursive: true);
            System.IO.Compression.ZipFile.ExtractToDirectory(modulesZipDir, extractDir);
        }

        public void InstallPython(bool force = false)
        {
#if DEBUG
            // I'm using symlinks to the python sources for development
            return;
#endif
            try
            {
                if (
                    File.Exists(GetPythonExePath())
                    && File.Exists(Path.Combine(GetVenvDir(), "pytrapic_python_modules.zip"))
                    && !force
                )
                {
                    L.Debug("Python already installed");
                    return;
                }
                Timer t = new Timer("InstallPython");

                StopProcess();

                if (File.Exists(GetPythonExePath()) && force)
                {
                    L.Info($"Forcing re-install of Python {PYTHON_VERSION} and dependencies");
                    try
                    {
                        Directory.Delete(GetVenvDir(), true);
                    }
                    catch (Exception ex)
                    {
                        L.Error($"Error deleting existing venv: {ex}");
                        return;
                    }
                }

                L.Info("Installing Python and dependencies");
                var pythonZipName = $"python-{PYTHON_VERSION}-embed-amd64.zip";
                var url = $"https://www.python.org/ftp/python/{PYTHON_VERSION}/{pythonZipName}";
                var pythonDir = GetVenvDir();
                var pythonZipPath = Path.Combine(
                    BepInEx.Paths.CachePath,
                    "pytrapic",
                    pythonZipName
                );
                Directory.CreateDirectory(pythonDir);
                using (var client = new System.Net.WebClient())
                {
                    client.DownloadFile(url, pythonZipPath);
                }
                System.IO.Compression.ZipFile.ExtractToDirectory(pythonZipPath, pythonDir);

                var pythonVersion = PYTHON_VERSION
                    .Substring(0, PYTHON_VERSION.LastIndexOf('.'))
                    .Replace(".", "");

                File.AppendAllText(
                    Path.Combine(pythonDir, $"python{pythonVersion}._pth"),
                    "\nsite-packages\n",
                    Encoding.UTF8
                );

                L.Info($"Installed Python {PYTHON_VERSION} to {pythonDir}");
                t.Dispose();
            }
            catch (Exception ex)
            {
                L.Error($"Error installing Python: {ex}");
            }
        }

        public async UniTaskVoid Init(bool forceRestart = false, bool forceInstall = false)
        {
            L.Debug("Initializing PythonCompiler");
            using (new Timer("Install Python"))
                InstallPython(forceInstall);
            using (new Timer("Update Python modules"))
                UpdatePythonModules();
            L.Debug("Python installation checked");
            if (IsRunning())
            {
                if (!forceRestart)
                    return;

                StopProcess();
            }
            L.Debug($"Starting PythonCompiler instance");
            var pythonPath = GetPythonExePath();
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

            pages = JsonConvert.DeserializeObject<List<PediaPage>>(
                Encoding.UTF8.GetString((Convert.FromBase64String(await _stdout.ReadLineAsync())))
            );
            AddStationpediaPages();

            L.Info($"PythonCompiler running");
            L.Info($"Registered Python code formatter");
            L.Info($"Get formatter {CodeFormatters.GetFormatter()}");
            _initTcs.TrySetResult();
        }

        public void AddStationpediaPages()
        {
            L.Info($"Add {pages.Count} PyTrapIC pages to Stationpedia");
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


    [BepInDependency("aproposmath-stationeers-ic10-editor", BepInDependency.DependencyFlags.HardDependency)]
    [BepInPlugin(pluginGuid, pluginName, pluginVersion)]
    public class PyTrapICPlugin : BaseUnityPlugin
    {
        public const string pluginGuid = "aproposmath-stationeers-pytrapic";
        public const string pluginName = "PyTrapIC";
        public const string pluginVersion = VersionInfo.Version;

        private void Awake()
        {
            try
            {
                L.Debug("Awake PyTrapIC plugin");
                var sw = Stopwatch.StartNew();
                L.Initialize(Logger);
                L.Info(
                    $"Awake PyTrapIC {VersionInfo.VersionGit} build time {VersionInfo.BuildTime}"
                );

                PythonCompiler.Instance = new PythonCompiler();
                CommandLine.AddCommand("pytrapic", new PyTrapICCommand());

                sw.Stop();
                L.Info(
                    $"PyTrapIC {VersionInfo.VersionGit} initialized in {sw.ElapsedMilliseconds}ms"
                );

                CodeFormatters.RegisterFormatter("Python", typeof(PythonFormatter));
            }
            catch (Exception ex)
            {
                L.Error($"Error during PyTrapIC {VersionInfo.VersionGit} init: {ex}");
            }
        }

        private void OnDestroy()
        {
            L.Info($"OnDestroy ${pluginName} {VersionInfo.VersionGit}");
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
                case "debug_logging":
                    return "Debug logging " + (L.ToggleDebug() ? "enabled." : "disabled.");
                case "libraries":
                    return string.Join("\n", SourceData.loadLibraries().Keys.OrderBy(x => x));
                case "version":
                    return VersionInfo.VersionGit;
                case "reinstall":
                    PythonCompiler.Instance.Init(true, true).Forget();
                    return "Python and dependencies reinstalled.";
                default:
                    return HelpText;
            }
        }
    }
}
