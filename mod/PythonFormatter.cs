namespace StationeersPyTrapIC
{
    using ImGuiNET;
    using System;
    using System.Threading.Tasks;
    using UnityEngine;
    using StationeersIC10Editor;
    using StationeersIC10Editor.IC10;
    using Cysharp.Threading.Tasks;
    using System.Threading;

    public class PythonFormatter : ICodeFormatter
    {
        private PythonCompiler.CompileResponse lastCompileResponse = null;

        private IC10CodeFormatter IC10Formatter = new IC10CodeFormatter();

        private long _DebounceCounter = 0;
        public int DebounceDelayMs = 100;
        private System.Object _Mutex = new System.Object();

        public PythonFormatter()
          : base()
        {
            OnCodeChanged += () =>
            {
                UniTask.RunOnThreadPool(() => ResetCodeDebounced(RawText));
            };
        }

        public async UniTaskVoid ResetCodeDebounced(string code)
        {
            if (string.IsNullOrWhiteSpace(code))
                return;
            await PythonCompiler.Instance.WaitForReadyAsync();
            var counter = ++_DebounceCounter;
            // await UniTask.SwitchToThreadPool();
            L.Info($"Debouncing code reset... {counter}, waiting {DebounceDelayMs} ms");
            await Task.Delay(DebounceDelayMs);

            if (counter != _DebounceCounter)
            {
                L.Info("Newer debounce task detected, cancelling this one.");
                return;
            }

            // try
            // {
            //     L.Info($"Waiting for {DebounceDelayMs} ms debounce delay...");
            //     await UniTask.Delay(DebounceDelayMs, cancellationToken: token);
            // }
            // catch (OperationCanceledException)
            // {
            //     L.Info("Debounce delay cancelled — new input arrived.");
            //     return;
            // }
            //
            // if (token.IsCancellationRequested)
            // {
            //     L.Info("Cancellation requested after delay.");
            //     return;
            // }

            // make sure this is run in a mutex
            lock (_Mutex)
            {
                if (counter != _DebounceCounter)
                {
                    L.Info("Newer debounce task detected, cancelling this one.");
                    return;
                }
                L.Info($"Debounce delay elapsed, proceeding with code reset.");

                L.Info($"Resetting code {code.Length} chars");
                var sw = System.Diagnostics.Stopwatch.StartNew();
                lastCompileResponse = PythonCompiler.Instance.Compile(code);
                var compiled = lastCompileResponse.code ?? "";
                sw.Stop();
                L.Info($"Compilation took {sw.ElapsedMilliseconds} ms");
                L.Info($"got compiled code {compiled.Length} chars");
                IC10Formatter.ResetCode(compiled);
                Lines = ParseHighlightResponse(lastCompileResponse);
            }

            // ResetCode(code);
        }

        public override void ResetCode(string code)
        {
            Lines.Clear();
            var lines = code.Split('\n');
            foreach (var line in lines)
                Lines.Add(new Line(line));
            // ResetCodeDebounced(code).Forget();
            // L.Info($"Resetting code {code.Length} chars");
            // var sw = System.Diagnostics.Stopwatch.StartNew();
            // lastCompileResponse = PythonCompiler.Instance.Compile(code);
            // var compiled = lastCompileResponse.code ?? "";
            // sw.Stop();
            // L.Info($"Compilation took {sw.ElapsedMilliseconds} ms");
            // L.Info($"got compiled code {compiled.Length} chars");
            // IC10Formatter.ResetCode(compiled);
            // Lines = ParseHighlightResponse(lastCompileResponse);
            //
            // while (Lines.Count < IC10Formatter.Lines.Count)
            //     Lines.Add(new Line());
            // base.ResetCode(code);
        }

        public override void DrawLine(int lineIndex, TextRange selection, bool drawLineNumbers)
        {
            Vector2 cursorPos = ImGui.GetCursorScreenPos();
            Vector2 space = ImGui.GetContentRegionAvail();
            base.DrawLine(lineIndex, selection, drawLineNumbers);

            var charWidth = Settings.CharWidth;

            var width = Mathf.Max(Lines.Width + 10.0f + LineNumberOffset * charWidth, space.x / 2);

            ImGui.GetWindowDrawList().AddLine(
                new Vector2(cursorPos.x + width + 4.5f * charWidth, cursorPos.y),
                new Vector2(cursorPos.x + width + 4.5f * charWidth, cursorPos.y + space.y + Settings.LineHeight),
                ColorLineNumber, 1.0f
            );

            cursorPos.x += width;
            ImGui.SetCursorScreenPos(cursorPos);
            if (lineIndex < IC10Formatter.Lines.Count)
                IC10Formatter.DrawLine(lineIndex, new TextRange(), true);
        }

        public override Line ParseLine(string line)
        {
            // ResetCodeDebounced(RawText).Forget();
            return new Line(line);
            // return HighlightCode(line)[0];
        }

        public void DrawStatus(IEditor ed, TextPosition caret)
        {
            var error = lastCompileResponse?.error;
            if (error == null)
                return;

            // join lines
            var oneline = error.description.Replace('\n', ' ');
            ImGui.TextColored(new Vector4(1, 0, 0, 1), oneline);
        }

        public FormattedText ParseHighlightResponse(PythonCompiler.CompileResponse compiled)
        {
            var lines = compiled.highlighted.Split('\n');

            const char TOKEN_SEP = (char)0x1E; // RS
            const char FIELD_SEP = (char)0x1F; // US

            var unformattedLines = compiled.input.code[""].Split('\n');

            L.Info($"Total lines to process: {lines.Length}");
            L.Info($"Total unformatted lines: {unformattedLines.Length}");

            var result = new FormattedText();

            for (int i = 0; i < lines.Length; i++)
            {
                if (i >= unformattedLines.Length)
                {
                    L.Info($"Line index {i} exceeds unformatted lines length {unformattedLines.Length}. Skipping.");
                    break;
                }
                var line = new Line();
                if (string.IsNullOrWhiteSpace(lines[i]))
                {
                    result.Add(line);
                    continue;
                }
                var tokens = lines[i].Split(TOKEN_SEP);
                foreach (var token in tokens)
                {
                    if (string.IsNullOrWhiteSpace(token))
                        continue;
                    var fields = token.Split(FIELD_SEP);
                    if (fields.Length < 3)
                    {
                        continue;
                    }

                    var t = new Token(fields[2], int.Parse(fields[0]), ICodeFormatter.ColorFromHTML(fields[1]));
                    t.Tooltip = compiled.tooltip + ", " + compiled.completion + ", " + compiled.error;
                    line.Add(t);
                }
                result.Add(line);
            }

            for (int i = lines.Length; i < unformattedLines.Length; i++)
                result.Add(new Line());
            L.Info("Code reset complete. Total lines: " + result.Count);

            return result;
        }

    }
}
