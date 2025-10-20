using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;
using Assets.Scripts.Networking;
using Assets.Scripts.Networking.Transports;
using Assets.Scripts.Objects;
using Assets.Scripts.Objects.Electrical;
using Assets.Scripts.Objects.Motherboards;
using Assets.Scripts.UI;
using Assets.Scripts.UI.ImGuiUi;
using BepInEx;
using BepInEx.Logging;
using Cysharp.Threading.Tasks;
using HarmonyLib;
using ImGuiNET;
using Newtonsoft.Json;
// using UI.ImGuiUi.ImGuiWindows;
using UI.Tooltips;
using UnityEngine;
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

        public static ConditionalWeakTable<ISourceCode, SourceData> Data =
            new ConditionalWeakTable<ISourceCode, SourceData>();

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
            public bool compact = true;

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
            public string tooltip;
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
            return;
#if DEBUG
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
            return;
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

        public PythonCompiler()
        {
            Init().Forget();
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

        public CompileResponse Compile(string pythonCode)
        {
            if (!IsRunning())
            {
                L.Error("Python compiler is not running, cannot compile");
                return new CompileResponse
                {
                    error = { description = "Python compiler is not running" },
                };
            }
            int lineno = -1;
            int column = -1;
            GetPosition(out lineno, out column);
            L.Debug($"Compiling code at {lineno}:{column}");

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

        public string SendData(string data)
        {
            if (data == lastInput)
                return lastOutput;

            try
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
            catch (Exception ex)
            {
                L.Error($"Error sending Python data: {ex}");
                return $"Error: {ex.Message}";
            }
        }
    }

    [HarmonyPatch]
    public static class PyTrapICPatches
    {
        private static bool isPasting = false; // fix for faster pasting

        [HarmonyPatch(typeof(Stationpedia), nameof(Stationpedia.Regenerate)), HarmonyPostfix]
        public static void Stationpedia_Regenerate()
        {
            if (PythonCompiler.Instance != null)
                PythonCompiler.Instance.AddStationpediaPages();
        }

        [
            HarmonyPatch(
                typeof(ProgrammableChip),
                nameof(ProgrammableChip.SetSourceCode),
                new[] { typeof(string) }
            ),
            HarmonyPrefix
        ]
        public static void ProgrammableChip_SetSourceCode(
            ProgrammableChip __instance,
            ref string sourceCode
        )
        {
            L.Debug($"Setting source code for chip {__instance.ReferenceId}:\n{sourceCode}");
            if (SourceData.NeedsCompile(sourceCode))
            {
                var ic10code = PythonCompiler.Instance.Compile(sourceCode).code;
                var sourceData = PythonCompiler.Data.GetOrCreateValue(__instance);
                sourceData.IC10Code = ic10code;
                sourceData.PythonCode = sourceCode;
                sourceCode = ic10code;
                L.Debug($"Compiled IC10 code:\n{ic10code}");
            }
        }

        [
            HarmonyPatch(typeof(ProgrammableChip), nameof(ProgrammableChip.GetSourceCode)),
            HarmonyPostfix
        ]
        public static void ProgrammableChip_GetSourceCode(
            ProgrammableChip __instance,
            ref AsciiString __result
        )
        {
            var sourceData = new SourceData { };
            if (PythonCompiler.Data.TryGetValue(__instance, out sourceData))
            {
                __result = AsciiString.Parse(sourceData.PythonCode);
            }
        }

        [
            HarmonyPatch(
                typeof(ProgrammableChipMotherboard),
                nameof(ProgrammableChipMotherboard.SetSourceCode)
            ),
            HarmonyPostfix
        ]
        public static void ProgrammableChipMotherboard_SetSourceCode(
            ProgrammableChipMotherboard __instance,
            ref string sourceCode
        )
        {
            if (SourceData.NeedsCompile(sourceCode))
            {
                // Editor.mode = Editor.Mode.EditPython;
                // Editor.SetPythonCode(sourceCode);
                // __instance.SourceCode.text = PythonCompiler.Instance.Highlight(sourceCode);
                var sourceCodeObj = AccessTools
                    .Field(__instance.GetType(), "SourceCode")
                    .GetValue(__instance);
                var textProp = AccessTools.Property(sourceCodeObj.GetType(), "text");
                textProp.SetValue(sourceCodeObj, PythonCompiler.Instance.Highlight(sourceCode));
            }
        }

        [
            HarmonyPatch(
                typeof(EditorLineOfCode),
                nameof(EditorLineOfCode.ReformatText),
                new[] { typeof(string) }
            ),
            HarmonyPrefix
        ]
        public static bool EditorLineOfCode_ReformatText(
            EditorLineOfCode __instance,
            string inputString
        )
        {
            // L.Debug($"Reformatting line: {inputString}");
            string newCode = InputSourceCode.Copy();
            // L.Debug($"Have code");
            if (SourceData.NeedsCompile(newCode))
            {
                // L.Debug($"Needs compile");
                // just set the current line to white color
                int nr = Int32.Parse(__instance.LineNumber.text.TrimEnd('.'));
                // __instance.FormattedText.text = $"<color=white>{inputString}</color>";
                InputSourceCode.Instance.LinesOfCode[nr].FormattedText.text =
                    $"<color=white>{inputString}</color>";

                // and trigger full reformat of the code asynchronously
                Editor.mode = Editor.Mode.EditPython;
                // L.Debug($"Call SetPythonCode");
                Editor.SetPythonCode(newCode);
                // L.Debug($"done SetPythonCode");

                return false;
            }

            // run original method, but only if we are not pasting (performance fix)
            return !isPasting;
        }

        [
            HarmonyPatch(typeof(InputSourceCode), nameof(InputSourceCode.UpdateFileSize)),
            HarmonyPrefix
        ]
        public static bool PatchInputSourceCodeUpdateFileSize()
        {
            if (Editor.mode == Editor.Mode.EditIC10 || Editor.mode == Editor.Mode.ViewIC10)
                return true; // run original method

            Editor.SetStatusText();
            return false;
        }

        [HarmonyPatch(typeof(InputSourceCode), "HandleInput"), HarmonyPrefix]
        public static bool InputSourceCode_HandleInputPrefix()
        {
            bool ctrlPressed =
                Input.GetKey(KeyCode.LeftControl) || Input.GetKey(KeyCode.RightControl);

            if (ctrlPressed && Input.GetKeyDown(KeyCode.I))
            {
                L.Debug("Toggling preview");
                Editor.TogglePreview();
                return false;
            }

            if (ctrlPressed && Input.GetKeyDown(KeyCode.M))
            {
                L.Debug("Toggling preview");
                Editor.ToggleCompileMode();
                return false;
            }

            if (Input.GetKeyDown(KeyCode.Tab))
            {
                int lineno,
                    column;
                PythonCompiler.GetPosition(out lineno, out column);
                // either insert 4 spaces, or trigger autocomplete
                Editor.HandleTabKey(lineno - 1, column);
                return false;
            }

            // UITooltipManager.ClearTooltip();

            return true;
        }

        [HarmonyPatch(typeof(InputSourceCode), "HandleInput"), HarmonyPostfix]
        public static void InputSourceCode_HandleInput()
        {
            // L.Debug("Post HandleInput");
            // if (Editor.mode == Editor.Mode.EditPython)
            //     Editor.SetPythonCode(InputSourceCode.Copy());

            Editor.UpdateTooltip();
        }

        [HarmonyPatch(typeof(InputSourceCode), nameof(InputSourceCode.Paste)), HarmonyPrefix]
        public static void PatchInputSourceCodePastePrefix()
        {
            isPasting = true;
        }

        [HarmonyPatch(typeof(InputSourceCode), nameof(InputSourceCode.Paste)), HarmonyPostfix]
        public static void PatchInputSourceCodePastePostfix()
        {
            var instance = InputSourceCode.Instance;
            if (instance == null)
                return;
            isPasting = false;

            string newCode = InputSourceCode.Copy();
            if (SourceData.NeedsCompile(newCode))
            {
                Editor.mode = Editor.Mode.EditPython;
                Editor.SetPythonCode(newCode);
            }
            else
            {
                Editor.mode = Editor.Mode.EditIC10;
                Editor.SetIC10Code(newCode);
                using (new Timer("Formatting code"))
                    for (int i = 0; i < instance.LinesOfCode.Count; i++)
                        instance.LinesOfCode[i].ReformatText();
            }
        }

        [HarmonyPatch(typeof(ProgrammableChip), "SerializeSave"), HarmonyPostfix]
        static void ProgrammableChip_SerializeSave(
            ProgrammableChip __instance,
            ref ThingSaveData __result
        )
        {
            var data = __result as ProgrammableChipSaveData;
            if (data == null)
            {
                L.Debug("Save data is not of type ProgrammableChipSaveData");
                return;
            }

            var sourceData = new SourceData { };
            if (!PythonCompiler.Data.TryGetValue(__instance, out sourceData))
            {
                L.Debug($"No chip data found for ID {data.ReferenceId}");
                return;
            }

            L.Debug($"Saving Python code: {sourceData.PythonCode}");
            L.Debug($"Saving IC10 code: {sourceData.IC10Code}");
            if (data.AliasesKeys == null)
            {
                data.AliasesKeys = new[] { sourceData.Serialize() };
            }
            else
            {
                var listData = new List<string>(data.AliasesKeys);
                listData.Add(sourceData.Serialize());
                data.AliasesKeys = listData.ToArray();
            }
            // make sure the IC10 code is set as the main source code
            // such that the save game can be loaded without this mod
            data.SourceCode = sourceData.IC10Code;
        }

        [HarmonyPatch(typeof(ProgrammableChip), "DeserializeSave"), HarmonyPrefix]
        static void ProgrammableChip_DeserializeSave(
            ref ThingSaveData savedData,
            ProgrammableChip __instance
        )
        {
            var data = savedData as ProgrammableChipSaveData;
            if (data == null)
            {
                L.Error("Load data is not of type ProgrammableChipSaveData");
                return;
            }

            if (data.AliasesKeys == null)
            {
                return;
            }

            try
            {
                L.Debug($"Loading source data for ID {data.ReferenceId}");
                if (
                    data.AliasesValues == null
                    || data.AliasesKeys.Length > data.AliasesValues.Length
                )
                {
                    SourceData sourceData = PythonCompiler.Data.GetOrCreateValue(__instance);
                    sourceData.Deserialize(data.AliasesKeys[data.AliasesKeys.Length - 1]);
                    L.Debug($"Loaded Python code: {sourceData.PythonCode}");
                    L.Debug($"Loaded IC10 code: {sourceData.IC10Code}");
                    data.AliasesKeys = data.AliasesKeys.Take(data.AliasesKeys.Length - 1).ToArray();
                }
                else
                {
                    L.Debug($"No python sources data found for ID {data.ReferenceId}");
                }
            }
            catch (Exception ex)
            {
                L.Error($"Error loading source data for ID ${data.ReferenceId}: {ex}");
            }
        }

        [HarmonyPatch(typeof(ImguiCreativeSpawnMenu))]
        [HarmonyPatch(nameof(ImguiCreativeSpawnMenu.Draw))]
        [HarmonyPostfix]
        static void ImguiCreativeSpawnMenuDrawPatch_Postfix()
        {
            ImGuiEditor.Draw();
        }
    }

    [BepInPlugin(pluginGuid, pluginName, pluginVersion)]
    public class PyTrapICPlugin : BaseUnityPlugin
    {
        public const string pluginGuid = "3f6a33e3-915f-4e35-90b0-2f07b29a91af";
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

                var harmony = new Harmony(pluginGuid);
                harmony.PatchAll();

                sw.Stop();
                L.Info(
                    $"PyTrapIC {VersionInfo.VersionGit} initialized in {sw.ElapsedMilliseconds}ms"
                );
            }
            catch (Exception ex)
            {
                L.Error($"Error during PyTrapIC {VersionInfo.VersionGit} init: {ex}");
            }
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
