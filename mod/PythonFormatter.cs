namespace StationeersPyTrapIC
{
    using ImGuiNET;
    using System.Threading.Tasks;
    using UnityEngine;
    using StationeersIC10Editor;
    using StationeersIC10Editor.IC10;
    using Cysharp.Threading.Tasks;

    public class PythonFormatter : ICodeFormatter
    {
        private PythonCompiler.CompileResponse lastCompileResponse = null;

        private IC10CodeFormatter IC10Formatter = new IC10CodeFormatter();

        private long _DebounceCounter = 0;
        public int DebounceDelayMs = 100;
        private System.Object _Mutex = new System.Object();

        public static double MatchingScore(string code)
        {
            L.Info("Calculating matching score for PythonFormatter...");
            if (code.StartsWith("from stationeers_pytrapic.symbols import *"))
            {
                L.Info("High confidence match for PythonFormatter.");
                return 1.0;
            }

            if (code.Contains("pytrapic"))
            {
                L.Info("Medium confidence match for PythonFormatter.");
                return 0.5;
            }

            L.Info("Low confidence match for PythonFormatter.");
            return 0.0;
        }

        public PythonFormatter()
          : base()
        {
            OnCodeChanged += () =>
            {
                UniTask.RunOnThreadPool(() => ResetCodeDebounced(RawText));
                lastCompileResponse = null;
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
            PythonCompiler.CompileResponse response;
            lock (_Mutex)
            {
                if (counter != _DebounceCounter)
                {
                    L.Info("Newer debounce task detected, cancelling this one.");
                    return;
                }
                L.Info($"Debounce delay elapsed, proceeding with code reset.");

                var sw = System.Diagnostics.Stopwatch.StartNew();
                response = PythonCompiler.Instance.Compile(code, _lastCaretPos.Line + 1, _lastCaretPos.Col);
                sw.Stop();
                L.Info($"Compilation took {sw.ElapsedMilliseconds} ms");
            }

            if (counter != _DebounceCounter)
            {
                L.Info("Newer debounce task detected after compilation, cancelling this one.");
                return;
            }
            lastCompileResponse = response;
            var compiled = lastCompileResponse.code ?? "";
            await UniTask.SwitchToThreadPool();
            IC10Formatter.ResetCode(compiled);
            Lines = ParseHighlightResponse(lastCompileResponse);
            ParseAutocomplete(lastCompileResponse);

            // ResetCode(code);
        }

        public void ParseAutocomplete(PythonCompiler.CompileResponse compiled)
        {
            L.Info($"Parsing autocomplete entries... {compiled.completion} chars");
            if (compiled.completion == null)
                return;
        }

        public override void ResetCode(string code)
        {
            Lines.Clear();
            var lines = code.Split('\n');
            foreach (var line in lines)
                Lines.Add(new Line(line));
            ResetCodeDebounced(code).Forget();
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

        public override void PerformAutocomplete()
        {
            var line = CurrentLine;
            if (line == null)
                return;
            if (lastCompileResponse?.completion == null)
                return;

            if (lastCompileResponse.completion.Length == 0)
                return;

            if (line.Text.Length < _lastCaretPos.Col)
                return;

            var completion = lastCompileResponse.completion;
            var prefixLength = lastCompileResponse.completion_prefix_length;

            var col = _lastCaretPos.Col - prefixLength;

            var newLine = line.Text.Substring(0, col) + completion + line.Text.Substring(_lastCaretPos.Col);
            Editor.ReplaceLine(_lastCaretPos.Line, newLine);
            Editor.CaretPos = new TextPosition(_lastCaretPos.Line, col + completion.Length);
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
                if (string.IsNullOrWhiteSpace(lines[i]))
                {
                    result.Add(new Line(lines[i]));
                    continue;
                }
                var tokens = lines[i].Split(TOKEN_SEP);
                string lineText = unformattedLines[i];
                var line = new Line(lineText);
                foreach (var token in tokens)
                {
                    if (string.IsNullOrWhiteSpace(token))
                        continue;
                    var fields = token.Split(FIELD_SEP);
                    if (fields.Length < 3)
                    {
                        continue;
                    }

                    var t = new SemanticToken(i, int.Parse(fields[0]), (int)fields[2].Length, ICodeFormatter.ColorFromHTML(fields[1]), 0);
                    t.Data = compiled.tooltip + ", " + compiled.completion + ", " + compiled.error;
                    line.AddToken(t);
                }
                result.Add(line);
            }

            for (int i = lines.Length; i < unformattedLines.Length; i++)
                result.Add(new Line(""));
            L.Info("Code reset complete. Total lines: " + result.Count);

            return result;
        }

    }
}
