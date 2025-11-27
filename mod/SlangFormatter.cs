namespace StationeersPyTrapIC
{
    using StationeersIC10Editor;

    public class SlangFormatter : ICodeFormatter
    {

        public static bool IsKeyword(string word)
        {
            var keywords = new string[]
            {
                "if", "else", "while", "for", "return", "function", "var", "let", "const"
            };
            foreach (var keyword in keywords)
            {
                if (word == keyword)
                {
                    return true;
                }
            }
            return false;
        }

        public static bool IsNumber(string word)
        {
            return float.TryParse(word, out _);
        }

        public static bool isValidIdentifyer(string word)
        {
            if (string.IsNullOrEmpty(word))
                return false;

            if (!char.IsLetter(word[0]) && word[0] != '_')
                return false;

            for (int i = 1; i < word.Length; i++)
            {
                if (!char.IsLetterOrDigit(word[i]) && word[i] != '_')
                    return false;
            }

            return true;
        }

        public override Line ParseLine(string line)
        {
            var words = line.Split(' ');
            var result = new Line();
            int column = 0;

            foreach (var word in words)
            {
                var token = new Token(word, column);
                if (IsKeyword(word))
                    token.Color = ColorFromHTML("#569CD6");
                else if (IsNumber(word))
                    token.Color = ColorNumber;
                else if (isValidIdentifyer(word))
                    token.Color = ColorDefault;
                else
                {
                    token.Color = ColorError;
                    token.Error = "Unrecognized token";
                }

                column += word.Length + 1;
                result.Add(token);
            }
            return result;
        }

        public override string Compile()
        {
            // Do your magic here
            return "hcf";
        }
    }
}
