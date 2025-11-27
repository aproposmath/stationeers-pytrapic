namespace StationeersPyTrapIC
{
    using ImGuiNET;
    using UnityEngine;
    using StationeersIC10Editor;

    public class PythonFormatter : ICodeFormatter
    {
        private PythonCompiler.CompileResponse lastCompileResponse = null;

        public override Line ParseLine(string line)
        {
            return HighlightCode(line)[0];
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

        public FormattedText HighlightCode(string code)
        {
            var compiled = PythonCompiler.Instance.Compile(code);
            var lines = compiled.highlighted.Split('\n');

            const char TOKEN_SEP = (char)0x1E; // RS
            const char FIELD_SEP = (char)0x1F; // US

            var unformattedLines = code.Split('\n');

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
            {
                L.Info($"Adding empty line for index {i}.");
                result.Add(new Line());
            }
            L.Info("Code reset complete. Total lines: " + result.Count);

            return result;
        }

    }
}
