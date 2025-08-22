using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Reflection;
using System.Reflection.Emit;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Xml.Serialization;
using Assets.Scripts;
using Assets.Scripts.Atmospherics;
using Assets.Scripts.Inventory;
using Assets.Scripts.Objects;
using Assets.Scripts.Objects.Appliances;
using Assets.Scripts.Objects.Clothing;
using Assets.Scripts.Objects.Electrical;
using Assets.Scripts.Objects.Entities;
using Assets.Scripts.Objects.Items;
using Assets.Scripts.Objects.Motherboards;
using Assets.Scripts.Objects.Pipes;
using Assets.Scripts.UI;
using BepInEx;
using HarmonyLib;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Objects.Items;
using Objects.Rockets;
using Reagents;
using UnityEngine;
using Util.Commands;
using Object = UnityEngine.Object;

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
        public static bool IsPython(string code)
        {
            return code.StartsWith("from stationeers_pytrapic.symbols import *");
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

    public static class F
    {
        private static readonly string FilePath = Path.Combine(
            Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
            "..",
            "..",
            "pytrapic.log"
        );

        public static void Log(string message, string type = "[LOG]   ")
        {
            File.AppendAllText(FilePath, $"[LOG]   {DateTime.Now}:   {message}\n");
        }

        [Conditional("DEBUG")]
        public static void Debug(string message)
        {
            Log(message, "[DEBUG]");
        }

        public static void Error(string message)
        {
            Log(message, "[ERROR]");
        }
    }

    public class PythonCompiler
    {
        public static readonly PythonCompiler Instance = new PythonCompiler();

        public static ConditionalWeakTable<ISourceCode, SourceData> Data =
            new ConditionalWeakTable<ISourceCode, SourceData>();

        private readonly Process _process;
        private readonly StreamWriter _stdin;
        private readonly StreamReader _stdout;

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

        ~PythonCompiler()
        {
            F.Log("Stopping PythonCompiler instance");
            if (!_process.HasExited)
            {
                _stdin?.WriteLine("EXIT");
                _process.Kill();
            }
        }

        public PythonCompiler()
        {
            F.Log($"Starting PythonCompiler instance");
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
                F.Error($"Tried to run python compiler at: ${pythonPath}");
                F.Error($"Python compiler process exited unexpectedly");
                throw new InvalidOperationException("Python compiler process exited unexpectedly");
            }
            if (_stdout == null || _stdin == null)
            {
                F.Error($"Tried to run python compiler at: ${pythonPath}");
                F.Error($"Failed to get standard input/output streams from Python compiler");
                throw new InvalidOperationException("Failed to get standard input/output streams");
            }
            _stdin.WriteLine("READY");
            string line = _stdout.ReadLine();
            if (line != "READY")
            {
                F.Error($"Python compiler did not respond with READY, got: {line}");
                throw new InvalidOperationException("Python compiler did not start correctly");
            }
            F.Log($"PythonCompiler running");
        }

        public CompileResponse Compile(string pythonCode, CompileOptions options = null)
        {
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
            F.Debug($"Highlighting code: {pythonCode}");
            if (pythonCode.Length == 0)
                return pythonCode;

            var data = JsonConvert.DeserializeObject<HighlightResponse>(
                SendData(
                    JsonConvert.SerializeObject(new { action = "highlight", code = pythonCode })
                )
            );

            if (data == null || data.error != null)
            {
                F.Error($"Error highlighting code: {data?.error}");
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
            F.Debug($"Received encoded from Python compiler: {line}");
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
                    F.Error($"No response from Python compiler, was sent: {data}");
                    return "Error: No response from Python compiler";
                }
                return response;
            }
            catch (Exception ex)
            {
                F.Error($"Error sending Python data: {ex}");
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
            F.Debug($"Setting source code for chip {__instance.ReferenceId}: {sourceCode}");
            if (SourceData.IsPython(sourceCode))
            {
                var ic10code = PythonCompiler.Instance.Compile(sourceCode).code;
                var sourceData = PythonCompiler.Data.GetOrCreateValue(__instance);
                sourceData.IC10Code = ic10code;
                sourceData.PythonCode = sourceCode;
                sourceCode = ic10code;
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
            if (SourceData.IsPython(sourceCode))
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
            if (!SourceData.IsPython(sourceCode))
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
                F.Debug("Save data is not of type ProgrammableChipSaveData");
                return;
            }

            var sourceData = new SourceData { };
            if (PythonCompiler.Data.TryGetValue(__instance, out sourceData))
            {
                F.Debug($"Saving Python code: {sourceData.PythonCode}");
                F.Debug($"Saving IC10 code: {sourceData.IC10Code}");
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
                F.Debug($"No chip data found for ID {data.ReferenceId}");
            }
        }

        [HarmonyPatch(typeof(ProgrammableChip), "DeserializeSave")]
        static void Prefix(ref ThingSaveData savedData, ProgrammableChip __instance)
        {
            var data = savedData as ProgrammableChipSaveData;
            if (data == null)
            {
                F.Error("Load data is not of type ProgrammableChipSaveData");
                return;
            }

            if (data.AliasesKeys == null)
            {
                return;
            }

            try
            {
                F.Debug($"Loading source data for ID {data.ReferenceId}");
                if (
                    data.AliasesValues == null
                    || data.AliasesKeys.Length > data.AliasesValues.Length
                )
                {
                    SourceData sourceData = PythonCompiler.Data.GetOrCreateValue(__instance);
                    sourceData.Deserialize(data.AliasesKeys[data.AliasesKeys.Length - 1]);
                    F.Debug($"Loaded Python code: {sourceData.PythonCode}");
                    F.Debug($"Loaded IC10 code: {sourceData.IC10Code}");
                    data.AliasesKeys = data.AliasesKeys.Take(data.AliasesKeys.Length - 1).ToArray();
                }
                else
                {
                    F.Debug($"No python sources data found for ID {data.ReferenceId}");
                }
            }
            catch (Exception ex)
            {
                F.Error($"Error loading source data for ID ${data.ReferenceId}: {ex}");
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
            F.Log("PyTrapIC loaded");

            var harmony = new Harmony(pluginGuid);
            harmony.PatchAll();

            // trigger startup of Python compiler
            PythonCompiler.Instance.Highlight("");
        }
    }
}
