using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Reflection;
using System.Reflection.Emit;
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

    public class ChipData
    {
        public string PythonCode { get; set; }
        public string IC10Code { get; set; }
    }

    public class UploadData : ChipData
    {
        public string OldIC10Code { get; set; }
    }

    public static class F
    {
        private static readonly string FilePath = Path.Combine(
            Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
            "..",
            "..",
            "pytrapic.log"
        );

        public static void Log(string message)
        {
            File.AppendAllText(FilePath, $"{DateTime.Now}: {message}\n");
        }
    }

    public class PythonCompiler
    {
        public static readonly PythonCompiler Instance = new PythonCompiler();

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
            F.Log("Dying PythonCompiler instance");
            if (!_process.HasExited)
            {
                _stdin?.WriteLine("EXIT");
                _process.Kill();
            }
        }

        public PythonCompiler()
        {
            F.Log($"new pyhton compiler");
            var pythonPath = Path.Combine(
                Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
                "..",
                "pytrapic",
                "venv",
                "python.exe"
            );
            F.Log($"have path ${pythonPath}");
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
            F.Log($"have process");

            _process.Start();
            F.Log($"started process");
            _stdin = _process.StandardInput;
            _stdout = _process.StandardOutput;
            if (_process.HasExited)
            {
                F.Log($"Python compiler process exited unexpectedly");
                throw new InvalidOperationException("Python compiler process exited unexpectedly");
            }
            if (_stdout == null || _stdin == null)
            {
                F.Log($"Failed to get standard input/output streams from Python compiler");
                throw new InvalidOperationException("Failed to get standard input/output streams");
            }
            _stdin.WriteLine("READY");
            string line = _stdout.ReadLine();
            F.Log($"Python compiler response: {line}");
            if (line != "READY")
            {
                F.Log($"Python compiler did not respond with READY, got: {line}");
                throw new InvalidOperationException("Python compiler did not start correctly");
            }
            F.Log($"Python compiler ready");
        }

        public CompileResponse Compile(string pythonCode, CompileOptions options)
        {
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
            if (pythonCode.Length == 0)
                return pythonCode;

            var data = JsonConvert.DeserializeObject<HighlightResponse>(
                SendData(
                    JsonConvert.SerializeObject(new { action = "highlight", code = pythonCode })
                )
            );

            if (data == null || data.error != null)
            {
                F.Log($"Error highlighting code: {data?.error}");
                return pythonCode; // Return original code if error
            }

            return "<color=#ffffff>" + data.highlighted + "</color>";
        }

        public void Send(string message)
        {
            // Prefix with length so Python knows where message ends
            var data = Convert.ToBase64String(Encoding.UTF8.GetBytes(message));
            F.Log($"Sending encoded to Python compiler: {data}");
            _stdin.WriteLine(data);
            _stdin.Flush();
        }

        public string Receive()
        {
            string line = _stdout.ReadLine();
            if (line == null)
                return null;
            byte[] raw = Convert.FromBase64String(line);
            return Encoding.UTF8.GetString(raw);
        }

        public string SendData(string data)
        {
            try
            {
                F.Log($"Sending data to Python compiler: {data}");
                // SendAsync(data).Wait();
                // var response = ReceiveAsync().Result;
                Send(data);
                var response = Receive();
                F.Log($"Response from python: {response}");
                if (response == null)
                {
                    return "Error: No response from Python compiler";
                }
                return response;
            }
            catch (Exception ex)
            {
                F.Log($"Error sending Python data: {ex}");
                return $"Error: {ex.Message}";
            }
        }
    }

    [HarmonyPatch]
    public static class ProgrammableChipMotherboardPath
    {
        [HarmonyPatch(
            typeof(ProgrammableChipMotherboard),
            nameof(ProgrammableChipMotherboard.SetSourceCode)
        )]
        public static void Prefix(ref string sourceCode)
        {
            sourceCode = PythonCompiler.Instance.Compile(sourceCode, new CompileOptions()).code;
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
            F.Log($"Highlighting input string: {inputString}");
            F.Log($"Old input: {inputString}");
            foreach (EditorLineOfCode item in __instance.Parent.LinesOfCode)
            {
                if (item.FormattedText.text.TrimEnd().Length > 0)
                {
                    F.Log($"{item.LineNumber.text} {item.InputText.text.TrimEnd()}");
                    F.Log($"{item.LineNumber.text} {item.FormattedText.text.TrimEnd()}");
                }
                // item.FormattedText.text = line[item.LineNumber];
            }
            __instance.FormattedText.text = PythonCompiler.Instance.Highlight(inputString);
            return false;
        }
    }

    [HarmonyPatch]
    public static class ChipPatch
    {
        public static Dictionary<long, ChipData> ChipsData = new Dictionary<long, ChipData>();

        [HarmonyPatch(typeof(ProgrammableChip), "SerializeSave")]
        static void Postfix(ProgrammableChip __instance, ref ThingSaveData __result)
        {
            var data = __result as ProgrammableChipSaveData;
            if (data == null)
            {
                F.Log("Save data is not of type ProgrammableChipSaveData");
                return;
            }

            if (ChipsData.ContainsKey(data.ReferenceId))
            {
                var chipData = ChipsData[data.ReferenceId];
                F.Log($"Saving Python code: {chipData.PythonCode}");
                F.Log($"Saving IC10 code: {chipData.IC10Code}");
                var concatData = new[] { JsonConvert.SerializeObject(chipData) };
                if (data.AliasesKeys == null)
                {
                    data.AliasesKeys = concatData;
                }
                else
                {
                    var listData = new List<string>(data.AliasesKeys);
                    listData.AddRange(concatData);
                    data.AliasesKeys = listData.ToArray();
                }
            }
            else
            {
                F.Log($"No chip data found for ID {data.ReferenceId}");
            }
        }

        [HarmonyPatch(typeof(ProgrammableChip), "DeserializeSave")]
        static void Prefix(ref ThingSaveData savedData, ProgrammableChip __instance)
        {
            var data = savedData as ProgrammableChipSaveData;
            if (data == null)
            {
                F.Log("Load data is not of type ProgrammableChipSaveData");
                return;
            }

            if (data.AliasesKeys == null)
            {
                return;
            }

            try
            {
                F.Log($"Load data {data}");
                F.Log($"ReferenceId {data.ReferenceId}");
                F.Log($"AliasesKeys {data.AliasesKeys}");
                F.Log($"AliasesValues {data.AliasesValues}");
                if (
                    data.AliasesValues == null
                    || data.AliasesKeys.Length > data.AliasesValues.Length
                )
                {
                    var chipData = JsonConvert.DeserializeObject<ChipData>(
                        data.AliasesKeys[data.AliasesKeys.Length - 1]
                    );
                    ChipsData[data.ReferenceId] = chipData;
                    F.Log($"Loaded Python code: {chipData.PythonCode}");
                    F.Log($"Loaded IC10 code: {chipData.IC10Code}");
                    data.AliasesKeys = data.AliasesKeys.Take(data.AliasesKeys.Length - 1).ToArray();
                }
                else
                {
                    F.Log($"No chip data found for ID {data.ReferenceId}");
                }
            }
            catch (Exception ex)
            {
                F.Log($"Error deserializing chip data: {ex}");
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
            F.Log("Mylog called!!!");

            var harmony = new Harmony(pluginGuid);
            harmony.PatchAll();

            // trigger startup of Python compiler
            PythonCompiler.Instance.Highlight("");
        }
    }
}
