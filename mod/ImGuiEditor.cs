using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;
using Assets.Scripts;
using Assets.Scripts.Objects.Electrical;
using Assets.Scripts.Objects.Motherboards;
using Assets.Scripts.UI;
using Assets.Scripts.UI.ImGuiUi;
using Cysharp.Threading.Tasks;
using ImGuiNET;
using UI.ImGuiUi;
using UI.Tooltips;
using UnityEngine;

namespace StationeersPyTrapIC
{
    using Ed = ImGuiEditor;

    public struct TextRange
    {
        public TextPosition Start;
        public TextPosition End;

        public TextRange(TextPosition start, TextPosition end)
        {
            Start = start;
            End = end;
        }

        public TextRange Sorted()
        {
            TextRange range = this;
            if (End < Start)
            {
                range.Start = End;
                range.End = Start;
            }
            return range;
        }

        public void Reset()
        {
            Start.Reset();
            End.Reset();
        }

        public static explicit operator bool(TextRange range)
        {
            return (bool)range.Start && (bool)range.End && (range.Start != range.End);
        }

        public static bool operator true(TextRange range)
        {
            return (bool)range;
        }

        public static bool operator false(TextRange range)
        {
            return (bool)range;
        }
    }

    public struct IntRange
    {
        public int Start;
        public int Next;

        public IntRange(int start, int next)
        {
            Start = start;
            Next = next;
        }
    }

    public struct TextPosition
    {
        public int Line;
        public int Col;

        public static bool operator ==(TextPosition a, TextPosition b)
        {
            return a.Line == b.Line && a.Col == b.Col;
        }

        public static bool operator !=(TextPosition a, TextPosition b)
        {
            return !(a == b);
        }

        public static bool operator <(TextPosition a, TextPosition b)
        {
            if (a.Line < b.Line)
                return true;
            if (a.Line == b.Line && a.Col < b.Col)
                return true;
            return false;
        }

        public static bool operator >(TextPosition a, TextPosition b)
        {
            return !(a < b) && (a != b);
        }

        public TextPosition(int line = -1, int column = -1)
        {
            Line = line;
            Col = column;
        }

        public void Reset()
        {
            Line = -1;
            Col = -1;
        }

        public static explicit operator bool(TextPosition pos)
        {
            return pos.Line >= 0 && pos.Col >= 0;
        }

        public static bool operator true(TextPosition pos)
        {
            return (bool)pos;
        }

        public static bool operator false(TextPosition pos)
        {
            return (bool)pos;
        }
    }

    public abstract class ICodeFormatter
    {
        public static uint ColorError = ColorFromHTML("#ff0000");
        public static uint ColorComment = ColorFromHTML("#808080");
        public static uint ColorLineNumber = ColorFromHTML("#808080");
        public static uint ColorDefault = ColorFromHTML("#ffffff");
        public static uint ColorSelection = ColorFromHTML("#3388ff80");
        public static uint ColorNumber = ColorFromHTML("#20b2aa");

        public const int LineNumberOffset = 5;

        public abstract void ResetCode(string code);
        public abstract void RemoveLine(string line);
        public abstract void AddLine(string line);
        public abstract uint GetColor(string token);

        public static uint ColorFromHTML(string htmlColor)
        {
            htmlColor = htmlColor.TrimStart('#');
            uint rgb = uint.Parse(htmlColor, System.Globalization.NumberStyles.HexNumber);
            byte a = 0xFF;

            if (rgb > 0xFFFFFF)
            {
                a = (byte)(rgb & 0xFF);
                rgb = rgb >> 8;
            }

            byte r = (byte)((rgb >> 16) & 0xFF);
            byte g = (byte)((rgb >> 8) & 0xFF);
            byte b = (byte)(rgb & 0xFF);

            L.Debug(
                $"Parsed HTML color '{htmlColor}' to RGBA({r},{g},{b},{a}) => 0x{((uint)a << 24) | ((uint)b << 16) | ((uint)g << 8) | r:X8}"
            );

            return ((uint)a << 24) | ((uint)b << 16) | ((uint)g << 8) | r;
        }

        public void ReplaceLine(string oldLine, string newLine)
        {
            RemoveLine(oldLine);
            AddLine(newLine);
        }

        public string TrimToken(string token)
        {
            return token.TrimEnd(':');
        }

        public static List<string> Tokenize(string text, bool keepWhitespace = false)
        {
            var tokens = new List<string>();
            if (string.IsNullOrEmpty(text))
                return tokens;

            int i = 0;
            while (i < text.Length)
            {
                int start = i;
                bool isWhitespace = char.IsWhiteSpace(text[i]);
                i++;
                while (i < text.Length && char.IsWhiteSpace(text[i]) == isWhitespace)
                    i++;

                if (keepWhitespace || !isWhitespace)
                    tokens.Add(text.Substring(start, i - start));
            }

            return tokens;
        }

        public void DrawLine(int lineIndex, string line, TextRange selection = default)
        {
            float charWidth = ImGui.CalcTextSize("M").x;
            var codeComment = line.Split('#');
            string code = codeComment[0];
            var tokens = Tokenize(code, true);
            Vector2 pos = ImGui.GetCursorScreenPos();
            ImGui
                .GetWindowDrawList()
                .AddText(pos, ColorLineNumber, lineIndex.ToString().PadLeft(3) + ".");
            pos.x += LineNumberOffset * charWidth;

            int selectionMin = -1,
                selectionMax = -1;

            if (selection)
            {
                float lineHeight = ImGui.GetTextLineHeightWithSpacing();
                if (selection.Start.Line <= lineIndex && selection.End.Line >= lineIndex)
                {
                    selectionMin = lineIndex == selection.Start.Line ? selection.Start.Col : 0;
                    selectionMax =
                        lineIndex == selection.End.Line ? selection.End.Col : line.Length;

                    selectionMin = Mathf.Clamp(selectionMin, 0, line.Length);
                    selectionMax = Mathf.Clamp(selectionMax, 0, line.Length);

                    Vector2 selStart = new Vector2(pos.x + charWidth * selectionMin, pos.y);
                    Vector2 selEnd = new Vector2(
                        pos.x + charWidth * selectionMax,
                        pos.y + lineHeight
                    );

                    ImGui
                        .GetWindowDrawList()
                        .AddRectFilled(selStart, selEnd, ICodeFormatter.ColorSelection);
                }
            }
            foreach (var token in tokens)
            {
                if (!string.IsNullOrWhiteSpace(token))
                    ImGui.GetWindowDrawList().AddText(pos, GetColor(token), token);
                pos.x += charWidth * token.Length;
            }
            if (codeComment.Length > 1)
            {
                string token = "#" + codeComment[1];
                ImGui.GetWindowDrawList().AddText(pos, ColorComment, token);
            }
        }
    }

    public class IC10CodeFormatter : ICodeFormatter
    {
        public static uint ColorInstruction = ColorFromHTML("#ffff00");

        // todo: recognize data type of tokens
        public static uint ColorDevice = ColorFromHTML("#00ff00");
        public static uint ColorLogicType = ColorFromHTML("#ff8000");
        public static uint ColorRegister = ColorFromHTML("#0080ff");

        public static uint ColorDefine = ColorNumber;
        public static uint ColorAlias = ColorFromHTML("#4d4dcc");
        public static uint ColorLabel = ColorFromHTML("#800080");

        HashSet<string> errors = new HashSet<string>(); // tokens that are marked as errors (used as alias and define for instance)

        Dictionary<string, int> defines = new Dictionary<string, int>();
        Dictionary<string, int> aliases = new Dictionary<string, int>();
        Dictionary<string, int> labels = new Dictionary<string, int>();
        Dictionary<string, string> instructions = new Dictionary<string, string>();
        HashSet<string> logicTypes = new HashSet<string>();
        HashSet<string> registers = new HashSet<string>();
        HashSet<string> devices = new HashSet<string>();

        public IC10CodeFormatter()
        {
            foreach (ScriptCommand cmd in EnumCollections.ScriptCommands.Values)
            {
                string cmdName = Enum.GetName(typeof(ScriptCommand), cmd);
                instructions[cmdName] = cmdName;
            }

            foreach (LogicType lt in EnumCollections.LogicTypes.Values)
            {
                string ltName = Enum.GetName(typeof(LogicType), lt);
                logicTypes.Add(ltName);
            }

            for (int i = 0; i < 16; i++)
                registers.Add($"r{i}");
            registers.Add("sp");
            registers.Add("ra");

            for (int i = 0; i < 6; i++)
                devices.Add($"d{i}");
            devices.Add("db");
        }

        public override void ResetCode(string code)
        {
            defines.Clear();
            aliases.Clear();
            labels.Clear();
            errors.Clear();

            var lines = code.Split('\n');
            foreach (var line in lines)
                AddLine(line);
        }

        public void CalcIsError(string token)
        {
            int count = 0;
            if (defines.ContainsKey(token))
                count += defines[token];
            if (aliases.ContainsKey(token))
                count += 1; // multiple aliaes are allowed, thus only count as 1
            if (labels.ContainsKey(token))
                count += labels[token];
            if (instructions.ContainsKey(token))
                count += 1;

            if (count > 1)
                errors.Add(token);
            else
                errors.Remove(token);
        }

        void AddDictEntry(Dictionary<string, int> dict, string key)
        {
            if (!dict.ContainsKey(key))
                dict[key] = 0;
            dict[key]++;
            CalcIsError(key);
        }

        void RemoveDictEntry(Dictionary<string, int> dict, string key)
        {
            dict[key]--;
            if (dict[key] == 0)
                dict.Remove(key);
            CalcIsError(key);
        }

        public override void AddLine(string line)
        {
            if (string.IsNullOrWhiteSpace(line))
                return;

            L.Debug($"Tokenized '{line}' to [{string.Join("''", Tokenize(line, true))}]");
            var tokens = Tokenize(line);

            if (tokens.Count > 1)
            {
                if (tokens[0] == "define")
                    AddDictEntry(defines, tokens[1]);

                if (tokens[0] == "alias")
                    AddDictEntry(aliases, tokens[1]);
            }

            if (tokens[0].EndsWith(":"))
                AddDictEntry(labels, tokens[0].Substring(0, tokens[0].Length - 1));
        }

        public override void RemoveLine(string line)
        {
            if (string.IsNullOrWhiteSpace(line))
                return;

            var tokens = Tokenize(line);

            if (tokens.Count > 1)
            {
                if (tokens[0] == "define")
                    RemoveDictEntry(defines, tokens[1]);

                if (tokens[0] == "alias")
                    RemoveDictEntry(aliases, tokens[1]);
            }

            if (tokens[0].EndsWith(":"))
                RemoveDictEntry(labels, tokens[0].Substring(0, tokens[0].Length - 1));
        }

        public override uint GetColor(string token)
        {
            if (double.TryParse(token, out double number))
                return ColorNumber;
            token = TrimToken(token);
            if (errors.Contains(token))
                return ColorError;
            else if (defines.ContainsKey(token))
                return ColorDefine;
            else if (aliases.ContainsKey(token))
                return ColorAlias;
            else if (labels.ContainsKey(token))
                return ColorLabel;
            else if (instructions.ContainsKey(token))
                return ColorInstruction;
            else if (devices.Contains(token))
                return ColorDevice;
            else if (logicTypes.Contains(token))
                return ColorLogicType;
            else if (registers.Contains(token))
                return ColorRegister;
            else
                return ColorDefault;
        }
    }

    public struct EditorState
    {
        public string Code;
        public TextPosition CaretPos;
    }

    public class ImGuiEditor
    {
        public ICodeFormatter CodeFormatter = new IC10CodeFormatter();

        public List<string> Lines = new List<string>();
        public string Code => string.Join("\n", Lines);
        public EditorState State
        {
            get { return new EditorState { Code = Code, CaretPos = caretPos }; }
            set
            {
                ClearCode();
                Insert(value.Code);
                caretPos = value.CaretPos;
            }
        }

        public LinkedList<EditorState> UndoList = new LinkedList<EditorState>();
        public bool scrollToCaret = false;

        public void PushUndoState()
        {
            var state = State;
            if (UndoList.Count > 0 && state.Code == UndoList.First.Value.Code)
                return;
            UndoList.AddFirst(State);
            while (UndoList.Count > 100)
                UndoList.RemoveLast();
        }

        public void Undo()
        {
            if (UndoList.Count == 0)
                return;

            State = UndoList.First.Value;
            UndoList.RemoveFirst();
        }

        public string CurrentLine
        {
            get { return Lines[caretLine]; }
            set
            {
                if (value == Lines[caretLine])
                    return;
                CodeFormatter.ReplaceLine(CurrentLine, value);
                Lines[caretLine] = value;
            }
        }

        public bool show = true;
        public bool isInitialized = false;
        public TextPosition caretPos = new TextPosition(0, 0);
        public int caretLine
        {
            get { return caretPos.Line; }
            set { caretPos.Line = value; }
        }
        public int caretCol
        {
            get { return caretPos.Col; }
            set { caretPos.Col = value; }
        }

        public TextRange Selection;

        public void CaretToEndOfLine()
        {
            caretCol = Lines[caretLine].Length;
        }

        public void CaretToStartOfLine()
        {
            caretCol = 0;
        }

        public void CaretUp()
        {
            MoveCaret(0, -1, true);
        }

        public void CaretDown()
        {
            MoveCaret(0, 1, true);
        }

        public void CaretLeft()
        {
            MoveCaret(-1, 0, true);
        }

        public void CaretRight()
        {
            MoveCaret(1, 0, true);
        }

        public void MoveCaret(
            int horizontal = 0,
            int vertical = 0,
            bool isRelative = true,
            bool isSelecting = false
        )
        {
            scrollToCaret = true;
            Selection.Reset();
            TextPosition newPos = caretPos;
            if (isRelative)
            {
                newPos.Line += vertical;
                newPos.Col += horizontal;
            }
            else
            {
                newPos.Line = vertical;
                newPos.Col = horizontal;
            }

            if (newPos.Line < 0)
                newPos.Line = 0;
            if (newPos.Line >= Lines.Count)
                newPos.Line = Lines.Count - 1;
            if (newPos.Col < 0)
                newPos.Col = 0;
            if (newPos.Col > Lines[newPos.Line].Length)
                newPos.Col = Lines[newPos.Line].Length;

            if (caretPos == newPos)
                return;

            if (isSelecting)
                Selection.End = newPos;
            else
                Selection.Reset();
            caretPos = newPos;
        }

        public void SelectAll()
        {
            Selection.Start = new TextPosition(0, 0);
            Selection.End = new TextPosition(Lines.Count - 1, Lines[Lines.Count - 1].Length);
        }

        public void Cut()
        {
            GameManager.Clipboard = string.Join("\n", Lines);
        }

        public void Copy()
        {
            string code = SelectedCode;
            if (code != null)
                GameManager.Clipboard = code;
        }

        public void Paste()
        {
            DeleteSelectedCode();
            Insert(GameManager.Clipboard.Replace("\r", ""));
        }

        public void ClearCode()
        {
            PushUndoState();
            Lines.Clear();
            Lines.Add("");
            CodeFormatter.ResetCode("");
            caretLine = 0;
            caretCol = 0;
            Selection.Reset();
        }

        public void Insert(string code)
        {
            var newLines = new List<string>(code.Split('\n'));
            if (newLines.Count == 0)
                return;

            CurrentLine += newLines[0];
            newLines.RemoveAt(0);
            Lines.InsertRange(caretLine, newLines);
            foreach (var line in newLines)
                CodeFormatter.AddLine(line);
            MoveCaret(0, newLines.Count, true);
        }

        public void Export()
        {
            L.Debug("Export invoked");
        }

        public bool HaveSelection => (bool)Selection;

        public string GetCode(TextRange range)
        {
            var start = range.Start;
            var end = range.End;

            if (start.Line == end.Line)
                return Lines[start.Line].Substring(start.Col, end.Col - start.Col);

            string code = Lines[start.Line].Substring(start.Col);
            for (int i = start.Line + 1; i < end.Line; i++)
                code += '\n' + Lines[i];
            code += '\n' + Lines[end.Line].Substring(0, end.Col);
            return code;
        }

        public string SelectedCode => GetCode(Selection.Sorted());

        public bool DeleteRange(TextRange range)
        {
            if (!(bool)range)
                return false;

            PushUndoState();

            var start = range.Start;
            var end = range.End;
            if (start.Line == end.Line)
            {
                string line = Lines[start.Line];
                string newLine =
                    line.Substring(0, start.Col) + line.Substring(end.Col, line.Length - end.Col);
                CurrentLine = newLine;
            }
            else
            {
                string firstLine = Lines[start.Line];
                string lastLine = Lines[end.Line];
                string newFirstLine = firstLine.Substring(0, start.Col);
                string newLastLine = lastLine.Substring(end.Col, lastLine.Length - end.Col);
                CurrentLine = newFirstLine + newLastLine;

                for (int i = end.Line; i > start.Line; i--)
                {
                    CodeFormatter.RemoveLine(Lines[i]);
                    Lines.RemoveAt(i);
                }
            }

            caretLine = start.Line;
            caretCol = start.Col;
            return true;
        }

        public bool DeleteSelectedCode()
        {
            if (DeleteRange(Selection))
            {
                Selection.Reset();
                return true;
            }
            return false;
        }

        public void HandleInput()
        {
            var io = ImGui.GetIO();
            io.ConfigWindowsMoveFromTitleBarOnly = true;
            bool ctrlDown = io.KeyCtrl;
            bool shiftDown = io.KeyShift;
            if (ctrlDown)
            {
                if (ImGui.IsKeyPressed(ImGuiKey.V))
                    Paste();
                if (ImGui.IsKeyPressed(ImGuiKey.A))
                    SelectAll();
                if (ImGui.IsKeyPressed(ImGuiKey.C))
                    Copy();
                if (ImGui.IsKeyPressed(ImGuiKey.X))
                {
                    GameManager.Clipboard = SelectedCode;
                    DeleteSelectedCode();
                }
                if (ImGui.IsKeyPressed(ImGuiKey.Z))
                    Undo();
            }
            else
            {
                // if (ImGui.IsKeyPressed(ImGuiKey.Escape)) CurrentLine += "<esc>";

                if (ImGui.IsKeyPressed(ImGuiKey.Backspace))
                {
                    if (DeleteSelectedCode())
                        return;

                    PushUndoState();
                    if (CurrentLine.Length > 0 && caretCol > 0)
                    {
                        CurrentLine = CurrentLine.Remove(caretCol - 1, 1);
                        caretCol--;
                    }
                    else if (caretCol == 0 && caretLine > 0)
                    {
                        // Merge with previous line
                        int prevLineLength = Lines[caretLine - 1].Length;
                        CurrentLine = Lines[caretLine - 1] + CurrentLine;
                        Lines.RemoveAt(caretLine - 1);
                        CodeFormatter.RemoveLine(Lines[caretLine - 1]);
                        caretLine--;
                        caretCol = prevLineLength;
                    }
                }
                if (ImGui.IsKeyPressed(ImGuiKey.Enter))
                {
                    PushUndoState();
                    string newLine = CurrentLine.Substring(caretCol);
                    CurrentLine = CurrentLine.Substring(0, caretCol);
                    Lines.Insert(caretLine + 1, newLine);
                    MoveCaret(0, caretLine + 1, false);
                }
                if (ImGui.IsKeyPressed(ImGuiKey.LeftArrow))
                    CaretLeft();
                if (ImGui.IsKeyPressed(ImGuiKey.RightArrow))
                    CaretRight();
                if (ImGui.IsKeyPressed(ImGuiKey.UpArrow))
                    CaretUp();
                if (ImGui.IsKeyPressed(ImGuiKey.DownArrow))
                    CaretDown();
                if (ImGui.IsKeyPressed(ImGuiKey.Home))
                    CaretToStartOfLine();
                if (ImGui.IsKeyPressed(ImGuiKey.End))
                    CaretToEndOfLine();
                if (ImGui.IsKeyPressed(ImGuiKey.PageUp))
                    MoveCaret(0, -20, true);
                if (ImGui.IsKeyPressed(ImGuiKey.PageDown))
                    MoveCaret(0, 20, true);

                string input = "";
                for (int i = 0; i < io.InputQueueCharacters.Size; i++)
                {
                    char c = (char)io.InputQueueCharacters[i];
                    input += c;
                }
                if (input.Length > 0)
                {
                    if (!DeleteSelectedCode())
                        PushUndoState();
                    CurrentLine = CurrentLine.Insert(caretCol, input);
                    caretCol += input.Length;
                }
            }
        }

        public void DrawHeader()
        {
            if (ImGui.Button("Clear"))
                ClearCode();
            ImGui.SameLine();

            if (ImGui.Button("Copy"))
                GameManager.Clipboard = string.Join("\n", Lines);
            ImGui.SameLine();

            if (ImGui.Button("Paste"))
            {
                ClearCode();
                Insert(GameManager.Clipboard);
            }
            ImGui.SameLine();

            if (ImGui.Button("s(x)")) { }
            ImGui.SameLine();

            if (ImGui.Button("x")) { }
            ImGui.SameLine();

            if (ImGui.Button("f")) { }
            ImGui.SameLine();

            if (ImGui.Button("Pause")) { }
        }

        public void DrawFooter()
        {
            ImGui.Text(
                $"Lines: {Lines.Count}  Caret: ({caretLine},{caretCol})  Undo: {UndoList.Count}"
            );
            ImGui.SameLine();

            ImGui.SetCursorPosX(ImGui.GetWindowWidth() - 200);
            if (ImGui.Button("Cancel")) { }
            ImGui.SameLine();
            if (ImGui.Button("Confirm")) { }
        }

        bool MouseIsInsideTextArea(Vector2 mousePos, Vector2 textOrigin)
        {
            float textAreaHeight = ImGui.GetTextLineHeightWithSpacing() * Lines.Count;
            float textAreaWidth = ImGui.GetContentRegionAvail().x; // or full width

            return mousePos.x >= textOrigin.x
                && mousePos.x <= textOrigin.x + textAreaWidth
                && mousePos.y >= textOrigin.y
                && mousePos.y <= textOrigin.y + textAreaHeight;
        }

        public unsafe void DrawCodeArea()
        {
            Vector2 availSize = ImGui.GetContentRegionAvail();
            float statusLineHeight = ImGui.GetTextLineHeightWithSpacing() * 2;
            float scrollHeight =
                availSize.y - statusLineHeight - ImGui.GetStyle().FramePadding.y * 2;

            ImGui.BeginChild("ScrollRegion", new Vector2(0, scrollHeight), true);

            ImGuiListClipperPtr clipper = new ImGuiListClipperPtr(
                ImGuiNative.ImGuiListClipper_ImGuiListClipper()
            );

            clipper.Begin(Lines.Count);

            Vector2 textAreaOrigin = ImGui.GetCursorScreenPos(); // Store this before drawing lines
            Vector2 mousePos = ImGui.GetMousePos();

            if (ImGui.IsMouseClicked(0)) // Left click
            {
                if (MouseIsInsideTextArea(mousePos, textAreaOrigin))
                {
                    caretPos = GetTextPositionFromMouse(mousePos, textAreaOrigin);
                    Selection.Start = caretPos;
                    Selection.End.Reset();
                }
            }
            if ((bool)Selection.Start && (ImGui.IsMouseDown(0) || ImGui.IsMouseReleased(0)))
                Selection.End = GetTextPositionFromMouse(mousePos, textAreaOrigin);

            if (scrollToCaret)
            {
                float lineHeight = ImGui.GetTextLineHeightWithSpacing();
                float lineSpacing = ImGui.GetStyle().ItemSpacing.y;

                float scrollY = ImGui.GetScrollY();
                float pageHeight = Lines.Count * lineHeight - ImGui.GetScrollMaxY();
                float viewTop = scrollY;
                float viewBottom = scrollY + pageHeight;

                float caretTop = caretLine * lineHeight;
                float caretBottom = caretTop + lineHeight;

                if (caretTop < viewTop)
                    scrollY = caretTop;
                else if (caretBottom > viewBottom)
                    scrollY = caretBottom - pageHeight + lineSpacing;

                ImGui.SetScrollY(Math.Min(scrollY, ImGui.GetScrollMaxY()));
                scrollToCaret = false;
            }

            var selection = Selection.Sorted();
            while (clipper.Step())
                for (int i = clipper.DisplayStart; i < clipper.DisplayEnd; i++)
                {
                    if (i == caretLine)
                        DrawCaret(ImGui.GetCursorScreenPos());
                    CodeFormatter.DrawLine(i, Lines[i], selection);
                    ImGui.NewLine();
                }
            clipper.End();
            ImGui.EndChild();
        }

        public void DrawCaret(Vector2 linePos)
        {
            bool blinkOn = ((int)(ImGui.GetTime() * 2) % 2) == 0;

            if (blinkOn)
            {
                var drawList = ImGui.GetWindowDrawList();
                var pos = ImGui.GetCursorScreenPos();
                pos.x += ImGui.CalcTextSize("M").x * (caretCol + ICodeFormatter.LineNumberOffset);
                var lineHeight = ImGui.GetTextLineHeight();

                // Draw a vertical line as the cursor
                drawList.AddLine(
                    pos,
                    new Vector2(pos.x, pos.y + lineHeight),
                    ImGui.ColorConvertFloat4ToU32(new Vector4(1, 1, 1, 1)),
                    1.5f
                );
            }
        }

        public void Draw()
        {
            ImGui.PushStyleColor(ImGuiCol.WindowBg, new Vector4(0.1f, 0.1f, 0.1f, 1.0f));
            ImGui.GetStyle().Colors[(int)ImGuiCol.WindowBg] = new Vector4(0.1f, 0.1f, 0.1f, 1.0f);
            ImGui.Begin("IC10 Editor", ref show, 0);

            if (!isInitialized)
            {
                var displaySize = ImGui.GetIO().DisplaySize;
                var windowSize = new Vector2(
                    Math.Min(1200, displaySize.x - 100),
                    displaySize.y - 100
                );
                var windowPos = 0.5f * (displaySize - windowSize);

                Lines.Clear();
                Lines.Add("");
                ImGui.SetNextWindowSize(windowSize);
                ImGui.SetNextWindowPos(windowPos);
                isInitialized = true;
            }

            HandleInput();

            DrawHeader();
            DrawCodeArea();
            DrawFooter();

            ImGui.End();
            ImGui.PopStyleColor();
        }

        TextPosition GetTextPositionFromMouse(Vector2 mousePos, Vector2 origin)
        {
            float charWidth = ImGui.CalcTextSize("M").x;
            float lineHeight = ImGui.GetTextLineHeightWithSpacing();

            int line = (int)((mousePos.y - origin.y) / lineHeight);
            int column =
                (int)((mousePos.x - origin.x) / charWidth) - ICodeFormatter.LineNumberOffset;

            line = Mathf.Clamp(line, 0, Lines.Count - 1);
            string lineText = Lines[line];
            column = Mathf.Clamp(column, 0, lineText.Length);

            return new TextPosition(line, column);
        }
    }
}
