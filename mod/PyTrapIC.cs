using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.RegularExpressions;
using Assets.Scripts.Networking;
using Assets.Scripts.Networking.Transports;
using Assets.Scripts.Objects;
using Assets.Scripts.Objects.Electrical;
using Assets.Scripts.Objects.Motherboards;
using Assets.Scripts.UI;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using Newtonsoft.Json;
using Util.Commands;

namespace StationeersPyTrapIC
{
    public class CompileOptions
    {
        public bool Comments { get; set; } = false;
        public bool Compact { get; set; } = false;
        public bool AppendVersion { get; set; } = true;
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
                return @"^\s*import\s+library\.(\w+)\s*$";
            }
            if (IsLuaCode(code))
            {
                return @"require\s*[""']library\.(?:[A-Za-z0-9_]+\.)*([A-Za-z0-9_]+)[""']";
            }
            return @"$^"; // matches nothing
        }

        public static Dictionary<string, SteamTransport.ItemWrapper> loadLibraries()
        {
            var sw = Stopwatch.StartNew();

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

            sw.Stop();

            L.Debug($"Loaded {libraries.Count} libraries in {sw.ElapsedMilliseconds}ms");

            return libraryMap;
        }

        public static string ReplaceLibraryCode(string code)
        {
            // Regex to capture lines of the form "import library.something"
            var regex = new Regex(getImportRegex(code), RegexOptions.Multiline);

            var matches = regex.Matches(code);

            if (matches.Count == 0)
            {
                return code; // No library imports found
            }

            var libraries = loadLibraries();

            foreach (Match match in matches)
            {
                string libName = match.Groups[1].Value.ToLowerInvariant();

                if (!libraries.ContainsKey(libName))
                {
                    L.Error($"Library {libName} not found in library map, skipping import");
                    continue; // Library not found, skip replacement
                }

                var lib = libraries[libName];
                L.Log($"Found matching library {libName}: {lib.FilePathFullName}");
                InstructionData instructionData = InstructionData.GetFromFile(lib.FilePathFullName);
                code = code.Replace(match.Value, instructionData.Instructions);
            }

            return code;
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
        private static bool _debugEnabled = true;

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
            _logger?.LogMessage(message?.ToString());
        }

        public static void Info(object msg)
        {
            _logger?.LogInfo(msg?.ToString());
        }

        public static void Error(object msg)
        {
            _logger?.LogError(msg?.ToString());
        }

        public static void Debug(object msg)
        {
            if (!_debugEnabled)
                return;
            _logger?.LogDebug(msg?.ToString());
        }
    }

    public class PythonCompiler
    {
        public static readonly PythonCompiler Instance = new PythonCompiler();

        public static ConditionalWeakTable<ISourceCode, SourceData> Data =
            new ConditionalWeakTable<ISourceCode, SourceData>();

        private Process _process;
        private StreamWriter _stdin;
        private StreamReader _stdout;

        public class HighlightResponse
        {
            public string error { get; set; }
            public string highlighted { get; set; }
        }

        public class CompileResponse
        {
            public string error { get; set; }
            public string code { get; set; }
            public int num_lines { get; set; }
            public int num_registers { get; set; }
            public int num_bytes { get; set; }
        }

        private void StopProcess()
        {
            L.Log("Stopping PythonCompiler instance");
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

        public void Init(bool forceRestart = false)
        {
            if (IsRunning())
            {
                if (!forceRestart)
                    return;

                StopProcess();
            }
            L.Log($"Starting PythonCompiler instance");
            var pythonPath = Path.Combine(
                Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
                "..",
                "pytrapic",
                "venv",
                "python.exe"
            );
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
                throw new InvalidOperationException("Python compiler process exited unexpectedly");
            }
            if (_stdout == null || _stdin == null)
            {
                L.Error($"Tried to run python compiler at: ${pythonPath}");
                L.Error($"Failed to get standard input/output streams from Python compiler");
                throw new InvalidOperationException("Failed to get standard input/output streams");
            }
            _stdin.WriteLine("READY");
            string line = _stdout.ReadLine();
            if (line != "READY")
            {
                L.Error($"Python compiler did not respond with READY, got: {line}");
                throw new InvalidOperationException("Python compiler did not start correctly");
            }
            L.Log($"PythonCompiler running");
        }

        public PythonCompiler()
        {
            Init();
        }

        public CompileResponse Compile(string pythonCode, CompileOptions options = null)
        {
            if (!IsRunning())
            {
                L.Error("Python compiler is not running, cannot compile");
                return new CompileResponse { error = "Python compiler is not running" };
            }
            pythonCode = SourceData.ReplaceLibraryCode(pythonCode);
            options ??= new CompileOptions();
            return JsonConvert.DeserializeObject<CompileResponse>(
                SendData(
                    JsonConvert.SerializeObject(
                        new
                        {
                            action = "compile",
                            code = pythonCode,
                            comments = options.Comments,
                            compact = options.Compact,
                            append_version = options.AppendVersion,
                        }
                    )
                )
            );
        }

        public string Highlight(string pythonCode)
        {
            if (!IsRunning())
            {
                L.Error("Python compiler is not running, cannot highlight");
                return pythonCode;
            }
            // L.Debug($"Highlighting code: {pythonCode}");
            if (pythonCode.Length == 0)
                return pythonCode;

            var data = JsonConvert.DeserializeObject<HighlightResponse>(
                SendData(
                    JsonConvert.SerializeObject(new { action = "highlight", code = pythonCode })
                )
            );

            if (data == null || data.error != null)
            {
                L.Error($"Error highlighting code: {data?.error}");
                return pythonCode; // Return original code if error
            }

            return data.highlighted;
        }

        public void Send(string message)
        {
            // Prefix with length so Python knows where message ends
            var data = Convert.ToBase64String(Encoding.UTF8.GetBytes(message));
            _stdin.WriteLine(data);
            _stdin.Flush();
        }

        public string Receive()
        {
            string line = _stdout.ReadLine();
            if (line == null)
                return null;
            L.Debug($"Received encoded from Python compiler: {line}");
            byte[] raw = Convert.FromBase64String(line);
            return Encoding.UTF8.GetString(raw);
        }

        public string SendData(string data)
        {
            try
            {
                Send(data);
                var response = Receive();
                if (response == null)
                {
                    L.Error($"No response from Python compiler, was sent: {data}");
                    return "Error: No response from Python compiler";
                }
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
    public static class Patch_ProgrammableChip
    {
        [HarmonyPatch(
            typeof(ProgrammableChip),
            nameof(ProgrammableChip.SetSourceCode),
            new[] { typeof(string) }
        )]
        public static void Prefix(ProgrammableChip __instance, ref string sourceCode)
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

        [HarmonyPatch(typeof(ProgrammableChip), nameof(ProgrammableChip.GetSourceCode))]
        public static void Postfix(ProgrammableChip __instance, ref AsciiString __result)
        {
            var sourceData = new SourceData { };
            if (PythonCompiler.Data.TryGetValue(__instance, out sourceData))
            {
                __result = AsciiString.Parse(sourceData.PythonCode);
            }
        }
    }

    [HarmonyPatch(
        typeof(ProgrammableChipMotherboard),
        nameof(ProgrammableChipMotherboard.SetSourceCode)
    )]
    public static class PatchProgrammableChipMotherboardSetSourceCode
    {
        static readonly FieldInfo privateSourceCode = AccessTools.Field(
            typeof(ProgrammableChipMotherboard),
            "SourceCode"
        );

        public static void Postfix(ProgrammableChipMotherboard __instance, ref string sourceCode)
        {
            if (SourceData.NeedsCompile(sourceCode))
            {
                var sourceCodeObj = privateSourceCode.GetValue(__instance);
                var textProp = AccessTools.Property(sourceCodeObj.GetType(), "text");
                textProp.SetValue(sourceCodeObj, PythonCompiler.Instance.Highlight(sourceCode));
            }
        }
    }

    [HarmonyPatch]
    public static class HighlightPatch
    {
        [HarmonyPatch(
            typeof(EditorLineOfCode),
            nameof(EditorLineOfCode.ReformatText),
            new[] { typeof(string) }
        )]
        public static bool Prefix(EditorLineOfCode __instance, string inputString)
        {
            string sourceCode = InputSourceCode.Copy();
            if (!SourceData.NeedsCompile(sourceCode))
            {
                return true; // run original method
            }
            var highlighted = PythonCompiler.Instance.Highlight(sourceCode);
            var lines = highlighted.Split(new[] { '\n' }, StringSplitOptions.None);
            for (int i = 0; i < lines.Length; i++)
            {
                __instance.Parent.LinesOfCode[i].FormattedText.text = lines[i];
            }
            return false;
        }
    }

    [HarmonyPatch]
    public static class ChipPatch
    {
        [HarmonyPatch(typeof(ProgrammableChip), "SerializeSave")]
        static void Postfix(ProgrammableChip __instance, ref ThingSaveData __result)
        {
            var data = __result as ProgrammableChipSaveData;
            if (data == null)
            {
                L.Debug("Save data is not of type ProgrammableChipSaveData");
                return;
            }

            var sourceData = new SourceData { };
            if (PythonCompiler.Data.TryGetValue(__instance, out sourceData))
            {
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
            else
            {
                L.Debug($"No chip data found for ID {data.ReferenceId}");
            }
        }

        [HarmonyPatch(typeof(ProgrammableChip), "DeserializeSave")]
        static void Prefix(ref ThingSaveData savedData, ProgrammableChip __instance)
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
    }

    [BepInPlugin(pluginGuid, pluginName, pluginVersion)]
    public class PyTrapICPlugin : BaseUnityPlugin
    {
        private const string pluginGuid = "io.inp.stationeers.stationeers_pytrapic";
        private const string pluginName = "PyTrapIC";
        private const string pluginVersion = "0.0.1";

        private void Awake()
        {
            var sw = Stopwatch.StartNew();
            L.Initialize(Logger);

            var harmony = new Harmony(pluginGuid);
            harmony.PatchAll();

            PythonCompiler.Instance.Init();
            CommandLine.AddCommand("pytrapic", new PyTrapICCommand());
            sw.Stop();
            L.Log($"PyTrapIC initialized in {sw.ElapsedMilliseconds}ms");
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
                    PythonCompiler.Instance.Init(true);
                    return "Python daemon restarted.";
                case "status":
                    return PythonCompiler.Instance.IsRunning()
                        ? "Python daemon is running."
                        : "Python daemon is not running.";
                case "debug_logging":
                    return "Debug logging " + (L.ToggleDebug() ? "enabled." : "disabled.");
                case "libraries":
                    return string.Join("\n", SourceData.loadLibraries().Keys.OrderBy(x => x));
                default:
                    return HelpText;
            }
        }
    }
}
