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
using BepInEx;
using BepInEx.Logging;
using Cysharp.Threading.Tasks;
using HarmonyLib;
using Newtonsoft.Json;
using UI.Tooltips;
using UnityEngine;
using Util.Commands;

namespace StationeersPyTrapIC
{
    public static class Editor
    {
        public enum Mode
        {
            EditIC10,
            EditPython,
            ViewIC10,
        }

        public static string compileMode = "compact"; // "compact" or "verbose"

        public static Mode mode = Mode.EditIC10;
        public static PythonCompiler.CompileResponse compiledCode = null;

        private static string ic10Code = "";
        private static string pythonCode = "";
        private static string[] highlightedLines = null;
        private static CancellationTokenSource debounceCts;

        public static void ToggleCompileMode()
        {
            if (mode == Mode.EditIC10)
                return;

            if (compileMode == "compact")
                compileMode = "verbose";
            else
                compileMode = "compact";
            bool isCompact = compileMode == "compact";
            PythonCompiler.options.remove_labels = isCompact;
            PythonCompiler.options.compact = isCompact;
            PythonCompiler.options.generated_comments = !isCompact;

            var pyCode = mode == Mode.EditPython ? InputSourceCode.Copy() : pythonCode;
            TriggerCompile(pyCode, 0);
        }

        public static void TogglePreview()
        {
            L.Debug($"TogglePreview from mode={mode}");

            if (mode == Mode.EditIC10)
                return;

            UITooltipManager.ClearTooltip();

            if (mode == Mode.EditPython)
            {
                if (compiledCode == null)
                    return;
                if (compiledCode.error != null)
                {
                    ShowErrorTooltip();
                    return;
                }
            }

            mode = mode == Mode.ViewIC10 ? Mode.EditPython : Mode.ViewIC10;
            L.Debug($"New mode={mode}");
            UpdateFormattedCode(true);
            UpdateTooltip();

            // bool activateInput = mode == Mode.EditPython;
            //
            // var lines = InputSourceCode.Instance.LinesOfCode;
            // for (int i = 0; i < lines.Count; i++)
            // {
            //     if (activateInput)
            //         lines[i].InputField.ActivateInputField();
            //     else
            //         lines[i].InputField.DeactivateInputField();
            // }
        }

        public static bool IsReadOnly()
        {
            return mode == Mode.ViewIC10;
        }

        public static void HandleTabKey(int lineno, int column)
        {
            L.Debug($"HandleTabKey at {lineno}:{column} in mode={mode}");
            if (mode != Mode.EditPython)
            {
                L.Debug("Ignore Tab key - not in EditPython mode");
                return;
            }

            var isc = InputSourceCode.Instance;
            if (isc == null)
                return;
            L.Debug("InputSourceCode instance found");

            // var line = isc.LinesOfCode[lineno];
            var line = isc.CurrentLine;
            var inputField = line.InputField;
            var text = inputField.text;
            L.Debug($"Line text: '{text}'");
            var before = text.Substring(0, column);
            var after = text.Substring(column);
            L.Debug($"HandleTabKey at {lineno}:{column}, before='{before}', after='{after}'");

            bool insertTab = string.IsNullOrEmpty(before.Trim());
            L.Debug($"InsertTab={insertTab}");

            if (insertTab)
            {
                line.Text = before + "    " + after;
                inputField.stringPosition = column + 4;
            }
            else
            {
                if (compiledCode.completion?.Length > 0)
                {
                    int prefixLength = compiledCode.completion_prefix_length;
                    string newText =
                        before.Substring(0, before.Length - prefixLength)
                        + compiledCode.completion
                        + after;
                    L.Debug($"Apply completion: '{compiledCode.completion}'");
                    L.Debug($"New text: '{newText}'");
                    line.Text = newText;
                    line.ReformatText();
                    inputField.stringPosition =
                        column + compiledCode.completion.Length - prefixLength;
                }
            }
            isc._previousCaretPosition = isc.CaretPosition;
        }

        public static void TriggerCompile(string code, int delayMs = 300)
        {
            // trigger compile in thread
            debounceCts?.Cancel();
            debounceCts = new CancellationTokenSource();
            CompileInThread(code, delayMs, (debounceCts.Token)).Forget();
        }

        public static void SetPythonCode(string code)
        {
            if (code == pythonCode)
                return;

            TriggerCompile(code);
        }

        public static void SetIC10Code(string code)
        {
            code = code ?? "";

            if (code == ic10Code)
                return;

            ic10Code = code;
            L.Debug("SetInputCode - no need to compile ${code.Length} chars");
            L.Debug($"First 100 chars:\n{code.Substring(0, Math.Min(100, code.Length))}");

            if (mode == Mode.EditIC10)
            {
                // reset python code since we are editing IC10 directly
                pythonCode = "";
                compiledCode = null;
                highlightedLines = null;
            }
        }

        public static string FormatSize(int num, int max, string label)
        {
            return (
                    num > max ? $"<color=red>{num}</color>"
                    : num > max * 0.9 ? $"<color=yellow>{num}</color>"
                    : $"{num}"
                ) + $"/{max} {label}";
        }

        public static void SetStatusText()
        {
            if (compiledCode == null)
                return;

            if (mode == Mode.EditIC10)
                return;

            L.Debug($"SetStatusText {InputSourceCode.Instance}");
            var sizeText = InputSourceCode.Instance.SizeText;
            string statusText =
                $"{FormatSize(compiledCode.num_registers, 16, "registers")}, {FormatSize(compiledCode.num_lines, 128, "lines")}, {FormatSize(compiledCode.num_bytes, 4096, "bytes")}";
            string modeText = mode == Mode.EditPython ? "Python" : "IC10 preview";
            modeText += $", <color=\"yellow\">{compileMode}</color> mode";
            statusText += $"\n<color=\"yellow\">{modeText}</color>";
            sizeText.text = statusText;
            sizeText.color = Color.white;
        }

        public static void UpdateFormattedCode(bool resetInput = false)
        {
            L.Debug($"UpdateFormattedCode in mode={mode}");
            StackTrace stackTrace = new StackTrace();
            StackFrame frame = stackTrace.GetFrame(1); // 0 is this method, 1 is the caller
            var method = frame.GetMethod();

            L.Debug($"Called by: {method.DeclaringType.FullName}.{method.Name}");

            var isc = InputSourceCode.Instance;
            if (isc == null)
                return;

            string code = mode == Mode.EditPython ? pythonCode : ic10Code;
            string[] lines = code.Split('\n');
            for (int i = 0; i < isc.LinesOfCode.Count; i++)
            {
                EditorLineOfCode line = isc.LinesOfCode[i];
                string lineText = ((i >= lines.Length) ? string.Empty : lines[i].TrimEnd());
                if (line.InputField.text != lineText)
                {
                    if (resetInput)
                        line.InputField.text = lineText;
                    else
                        return; // don't update if user is editing
                }
            }

            if (mode == Mode.EditPython)
            {
                L.Debug($"Update formatted code to Python ({pythonCode.Length} chars)");
                if (highlightedLines == null)
                    return;
                for (int i = 0; i < isc.LinesOfCode.Count; i++)
                    isc.LinesOfCode[i].FormattedText.text =
                        i < highlightedLines.Length ? highlightedLines[i] : "";
            }

            if (mode == Mode.ViewIC10 || mode == Mode.EditIC10)
            {
                L.Debug($"Set IC10 code ({ic10Code.Length} chars)");
                using (new Timer("Formatting code"))
                    for (int i = 0; i < isc.LinesOfCode.Count; i++)
                        isc.LinesOfCode[i].ReformatText();
            }

            SetStatusText();
        }

        private static async UniTaskVoid CompileInThread(
            string sourceCode,
            int delayMs,
            CancellationToken token
        )
        {
            try
            {
                string newCode = String.Copy(sourceCode);
                pythonCode = newCode;
                L.Debug($"Debounced compile of {newCode.Length} chars");
                await UniTask.Delay(delayMs, cancellationToken: token);
                token.ThrowIfCancellationRequested();

                var compileResponse = await UniTask.Run(() =>
                {
                    return PythonCompiler.Instance.Compile(newCode);
                });

                // Switch to main thread for Unity API calls
                await UniTask.SwitchToMainThread();

                // chip.SetSourceCode(ic10code);
                compiledCode = compileResponse;
                ic10Code = compiledCode.code;
                ;
                highlightedLines = compiledCode.highlighted.Split(
                    new[] { '\n' },
                    StringSplitOptions.None
                );
                if (pythonCode != newCode)
                {
                    L.Debug("Input code changed during compile, ignoring result");
                    return;
                }

                if (mode == Mode.EditPython || mode == Mode.ViewIC10)
                    UpdateFormattedCode(mode == Mode.ViewIC10);
            }
            catch (OperationCanceledException)
            {
                L.Debug("Debounced compile canceled");
                // Debounce canceled — ignore
            }
            catch (Exception ex)
            {
                L.Error($"[DebouncedCompileAsync] Exception: {ex}");
            }
        }

        public static void ShowErrorTooltip()
        {
            var error = compiledCode.error;
            string pos = error.line != -1 ? $" at line {error.line - 1}:{error.column}" : "";
            string tooltip = $"<color=red>{error.description}{pos}</color>";
            UITooltipManager.SetTooltip(tooltip);
        }

        public static void UpdateTooltip()
        {
            if (mode != Mode.EditPython)
                return;
            UITooltipManager.ClearTooltip();
            if (compiledCode != null)
            {
                int lineno,
                    column;
                PythonCompiler.GetPosition(out lineno, out column);
                if (
                    compiledCode.tooltip != null
                    && compiledCode.tooltip.Length > 0
                    && lineno == compiledCode.input.lineno
                    && column == compiledCode.input.column
                )
                {
                    UITooltipManager.SetTooltip(compiledCode.tooltip);
                }
                else if (compiledCode.error != null)
                    ShowErrorTooltip();
            }
        }
    }
}
