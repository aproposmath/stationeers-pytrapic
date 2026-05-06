namespace StationeersPyTrapIC;

using System.Collections.Generic;
using StationeersIC10Editor;

public class PythonStaticFormatter : StaticFormatter
{
    static readonly Dictionary<string, uint> PythonKeywords = new()
    {
        { "def",      15 },
        { "import",   15 },
        { "from",     15 },
        { "as",       15 },
        { "class",    15 },
        { "try",      15 },
        { "except",   15 },
        { "finally",  15 },
        { "with",     15 },
        { "lambda",   15 },
        { "in",       15 },
        { "is",       15 },
        { "not",      15 },
        { "and",      15 },
        { "or",       15 },

        // Python constants
        { "True",     19 },
        { "False",    19 },
        { "None",     19 },

        // Types
        { "int",      1 },
        { "float",    1 },
        { "str",      1 },
        { "list",     1 },
        { "dict",     1 },
        { "set",      1 },
        { "tuple",    1 },

        { "return",   23 },
        { "if",       23 },
        { "else",     23 },
        { "elif",     23 },
        { "for",      23 },
        { "while",    23 },
        { "pass",     23 },
        { "break",    23 },
        { "continue", 23 },
    };

    public PythonStaticFormatter()
        : base(
            TokenSeparators: " \t()[]{}:.,+-*/%=<>!&|^~",
            StringDelimiters: "\"\'",
            CommentPrefix: "#",
            KeepWhitespaces: false,
            Keywords: PythonKeywords)
    {
        OnCodeChanged += () =>
        {
        };
    }
}
