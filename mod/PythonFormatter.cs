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
        private long _lastResponseVersion = 0;

        private IC10CodeFormatter IC10Formatter = new IC10CodeFormatter();

        private long _DebounceCounter = 0;
        public int DebounceDelayMs = 100;
        private System.Object _Mutex = new System.Object();

        public static double MatchingScore(string code)
        {
            if (code.StartsWith("from stationeers_pytrapic.symbols import *"))
                return 1.0;

            if (code.Contains("# PYTRAPIC_SOURCE:"))
                return 1.0;

            if (code.Contains("stationeers_pytrapic"))
                return 0.7;

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
            await Task.Delay(DebounceDelayMs);

            if (counter != _DebounceCounter)
                return;

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
            _lastResponseVersion = counter;
            var compiled = lastCompileResponse.code ?? "";
            await UniTask.SwitchToThreadPool();
            L.Info($"got compiled code {compiled.Length} chars |{compiled}|");
            IC10Formatter.Editor = Editor;
            IC10Formatter.ResetCode(compiled);
            Lines = ParseHighlightResponse(lastCompileResponse);
            ParseAutocomplete(lastCompileResponse);
            ParseError(lastCompileResponse);
        }

        private const char FIELD_SEP = (char)0x1F;

        static public Token ParseToken(string tokenStr)
        {
            var parts = tokenStr.Split(FIELD_SEP);
            if (parts.Length != 3)
                return null;
            var color = ICodeFormatter.ColorFromHTML(parts[1]);
            return new Token(int.Parse(parts[0]), parts[2], color);
        }

        public void ParseError(PythonCompiler.CompileResponse compiled)
        {
            if (compiled.error == null)
                return;

            var error = compiled.error;

            var errText = new StyledText();
            foreach (var errLine in error.description.Split('\n'))
                errText.Add(StyledText.ErrorText(errLine)[0]);

            L.Info($"Parsing error at line {error.line}, column {error.column}");
            if (error.line < 1 || error.line > Lines.Count)
                return;

            var line = Lines[error.line - 1];
            var col = error.column - 1;

            foreach (var token in line)
            {
                if (col >= line.Text.Length || (col >= token.Column && col < token.Column + token.Length))
                {
                    token.Error = errText;
                    token.Tooltip = errText;
                }
            }
        }

        public void ParseAutocomplete(PythonCompiler.CompileResponse compiled)
        {
            _autocomplete = null;
            _autocompleteInsertText = null;

            if (compiled.suggestions == null || compiled.suggestions.Length == 0)
                return;

            var suggestions = compiled.suggestions.Split('\n');

            if (suggestions.Length == 1 && compiled.completion_prefix_length == suggestions[0].IndexOf(FIELD_SEP))
                return;

            if (string.IsNullOrWhiteSpace(compiled.completion))
                return;

            var autocomplete = new StyledText();
            foreach (var line in suggestions)
            {
                if (string.IsNullOrWhiteSpace(line))
                    continue;

                if (line.Contains($"{FIELD_SEP}"))
                {
                    var fields = line.Split(FIELD_SEP);
                    var styledLine = new StyledLine(fields[0]);
                    var token = new Token(0, fields[0], ICodeFormatter.ColorFromHTML(fields[1]));
                    styledLine.Add(token);
                    autocomplete.Add(styledLine);
                }
                else
                    autocomplete.Add(new StyledLine(line));
            }

            _autocomplete = autocomplete;

            var prefixLength = lastCompileResponse.completion_prefix_length;
            var col = _lastCaretPos.Col - prefixLength;
            _autocompleteInsertText = compiled.completion.Substring(prefixLength);
        }

        public override void ResetCode(string code)
        {
            Lines.Clear();

            if (code.Contains("# PYTRAPIC_SOURCE:"))
            {
                var parts = code.Split(new string[] { "# PYTRAPIC_SOURCE:" }, System.StringSplitOptions.None);
                if (parts.Length >= 2)
                    code = DecodeSource(parts[1].Trim());
            }
            var lines = code.Split('\n');
            foreach (var line in lines)
                Lines.Add(new StyledLine(line));
            ResetCodeDebounced(code).Forget();
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

        public override StyledLine ParseLine(string line)
        {
            return new StyledLine(line);
        }

        public override void DrawStatus(Vector2 pos)
        {
            var error = lastCompileResponse?.error;
            if (error == null)
                return;

            var oneline = error.description.Replace('\n', ' ');
            ImGui.TextColored(new Vector4(1, 0, 0, 1), oneline);
        }

        public StyledText ParseHighlightResponse(PythonCompiler.CompileResponse compiled)
        {
            var lines = compiled.highlighted.Split('\n');

            const char TOKEN_SEP = (char)0x1E; // RS
            const char FIELD_SEP = (char)0x1F; // US

            var unformattedLines = compiled.input.code[""].Split('\n');

            var result = new StyledText();

            for (int i = 0; i < lines.Length; i++)
            {
                if (i >= unformattedLines.Length)
                {
                    L.Info($"Line index {i} exceeds unformatted lines length {unformattedLines.Length}. Skipping.");
                    break;
                }
                if (string.IsNullOrWhiteSpace(lines[i]))
                {
                    result.Add(new StyledLine(lines[i]));
                    continue;
                }
                var tokens = lines[i].Split(TOKEN_SEP);
                string lineText = unformattedLines[i];
                var line = new StyledLine(lineText);
                foreach (var token in tokens)
                {
                    if (string.IsNullOrWhiteSpace(token))
                        continue;
                    var fields = token.Split(FIELD_SEP);
                    if (fields.Length < 3)
                    {
                        continue;
                    }

                    var t = new Token(int.Parse(fields[0]), fields[2], ICodeFormatter.ColorFromHTML(fields[1]));
                    line.Add(t);
                }
                result.Add(line);
            }

            for (int i = lines.Length; i < unformattedLines.Length; i++)
                result.Add(new StyledLine(""));
            return result;
        }

        public override string Compile()
        {
            for (var i = 0; i < 10; i++)
            {
                if (_lastResponseVersion == _DebounceCounter && lastCompileResponse != null)
                    break;
                System.Threading.Thread.Sleep(100);
            }

            if (_lastResponseVersion == _DebounceCounter && lastCompileResponse != null)
            {
                var code = lastCompileResponse.code;
                code += "\n# PYTRAPIC_SOURCE: " + EncodeSource(RawText);
                return code;
            }

            L.Info("Compile called but no up-to-date compile response is available.");
            return "";
        }
    }
}
