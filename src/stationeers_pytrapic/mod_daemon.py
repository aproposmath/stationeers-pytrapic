import sys

_stdout = sys.stdout
sys.stdout = sys.stderr

import asyncio
import atexit
import base64
import datetime
import json
import sys
import tempfile
import time
from pathlib import Path

from pygments import highlight as _highlight
from pygments.formatters import BBCodeFormatter
from pygments.lexers import LuaLexer, PythonLexer
from pygments.style import Style

from .compiler import CompileOptions, compile_code
from .stationpedia import get_pages_encoded

from . import symbols
from . import types_generated


_logic_types = set()

f = open("/tmp/logic_types.txt", "w")

for t in dir(types_generated):
    # check if t is a class and is a subclass of enum
    attr = getattr(types_generated, t)
    if isinstance(attr, type):
        # add all enum members to the set
        for member in dir(attr):
            if not member.startswith("_") and member[:1].isupper():
                _logic_types.add(member)
                f.write(member + "\n")



def _get_ignore_symbol_names():
    import jedi

    s = jedi.Script("")
    completions = s.complete(1, 0)
    names = set((c.name for c in completions))
    for n in ["True", "False", "while", "if", "else", "def", "pow", "abs"]:
        if n in names:
            names.remove(n)
    return names

class MyStyle(Style):
    from pygments.token import Token, Comment, Keyword, Name, String, Error, Generic, Number, Operator
    # public static uint ColorError = ColorFromHTML("#ff0000");
    # public static uint ColorWarning = ColorFromHTML("#ff8f00");
    # public static uint ColorComment = ColorFromHTML("#808080");
    # public static uint ColorLineNumber = ColorFromHTML("#808080");
    # public static uint ColorDefault = ColorFromHTML("#ffffff");
    # public static uint ColorSelection = ColorFromHTML("#1a44b0ff");
    # public static uint ColorNumber = ColorFromHTML("#20b2aa");
    #     public static uint ColorInstruction = ColorFromHTML("#ffff00");
    #
    #     public static uint ColorDevice = ColorFromHTML("#00ff00");
    #     public static uint ColorLogicType = ColorFromHTML("#ff8000");
    #     public static uint ColorRegister = ColorFromHTML("#0080ff");
    #     public static uint ColorBasicEnum = ColorFromHTML("#20b2aa");
    #
    #     public static uint ColorDefine = ColorNumber;
    #     public static uint ColorAlias = ColorFromHTML("#4d4dcc");
    #     public static uint ColorLabel = ColorFromHTML("#800080");

    styles = {
        Name.Constant:   '#20b2aa',
        Token.Literal.Number:   '#20b2aa',
        Token:                  '#ffffff',
        Comment:                '#808080',
        Keyword:                '#ffff00',
        Name:                   '#ffffff',
        Name.Class:             '#00ff00',
        Name.Function:          '#0080ff',
        Name.Property:          '#ff8000',
        String:                 '#20b2aa',
    }

formatter = BBCodeFormatter(style=MyStyle)

replace = lambda s: s.replace("[", "<").replace("]", ">")
for ttype in formatter.styles:
    start, end = formatter.styles[ttype]
    if "657b83" in start or "657b83" in end:
        formatter.styles[ttype] = "", ""
    else:
        formatter.styles[ttype] = replace(start), replace(end)

_log_file = None  # Global log file handle
_err_file = None  # Global error file handle
ENABLE_LOGGING = __name__ == "__main__"
ENABLE_LOGGING = False

_ignore_symbol_names = _get_ignore_symbol_names()
_symbols_names = set(dir(symbols)) - _ignore_symbol_names

_jedi_project_dir = tempfile.mkdtemp(prefix="jedi_project_")


def format_completion(c):
    col = token_color(c.type, c.name)
    return f"{c.name}{FIELD_SEP}{col}{FIELD_SEP}{c.type}"

def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


def format_completions(completions):
    t0 = time.time()
    completions = [c for c in completions if not c.name.startswith("_")]
    completions = [c for c in completions if c.name not in _ignore_symbol_names]
    if not completions:
        return {}  # "completion":"", "tooltip":""}

    common_prefix = longest_common_prefix([c.name for c in completions])
    lengths = set([c.get_completion_prefix_length() for c in completions])
    if len(lengths) != 1:
        log(
            f"Warning: Inconsistent completion prefix lengths: {lengths}, completions: {[c.name for c in completions]}"
        )
        completion = ""
        prefix_len = 0
    else:
        prefix_len = lengths.pop()
        completion = common_prefix

    result = ""
    if completions:
        suffix = ""
        if len(completions) > 20:
            suffix = f"\n\n... and {len(completions) - 20} more"
            completions = completions[:20]
        comp_texts = [format_completion(c) for c in completions]
        result = "\n".join(comp_texts) + suffix
    t1 = time.time()
    log(f"Formatted {len(completions)} completions in {1000*(t1 - t0):.1f} ms")
    return {
        "suggestions": result,
        "completion_prefix_length": prefix_len,
        "completion": completion,
    }


def log(msg):
    global _log_file
    if ENABLE_LOGGING:
        if _log_file is None:
            _log_file = open("mod_daemon.log", "w")
        _log_file.write(f"{datetime.datetime.now().isoformat()} - {msg}\n")
        _log_file.flush()


def error(msg):
    global _err_file
    if ENABLE_LOGGING:
        if _err_file is None:
            _err_file = open("mod_daemon.err", "w")
        _err_file.write(f"{datetime.datetime.now().isoformat()} - {msg}\n")
        _err_file.flush()


log(f"Started")

_lexer = {
    "python": PythonLexer(),
    "lua": LuaLexer(),
}


def get_languate(code):
    return "lua" if code.lstrip().startswith("require") else "python"


def get_lexer(code):
    return _lexer[get_languate(code)]


# def highlight(code, error_line=None):
#     lines = _highlight(code, get_lexer(code), formatter).splitlines()
#     for i, line in enumerate(lines):
#         if error_line is not None and i + 1 == error_line:
#             lines[i] = "<color=#ff0000>" + line + "</color>"
#         else:
#             lines[i] = "<color=#ffffff>" + line + "</color>"
#     return "\n".join(lines)

TOKEN_SEP = "\x1E"   # RS
FIELD_SEP = "\x1F"   # US

from pygments import lex
from pygments.token import Token


from pygments import lex
from pygments.token import Token

style = formatter.style
def token_color(tokentype, text=""):
    if text in _symbols_names:
        if isinstance(getattr(symbols, text), type):
            return "#00ff00"  # ColorLogicType
        elif callable(getattr(symbols, text)):
            return "#0080ff"  # ColorRegister
        else:
            return "#20b2aa"  # ColorBasicEnum
    if text in _logic_types:
        return "#ff8000"  # ColorLogicType
    try:
        style_def = style.style_for_token(tokentype)
        return style_def.get("color", "ffffff").lower().rjust(6, "0")
    except:
        return "#ffffff"


def highlight(code, error_line=None):
    lexer = get_lexer(code)
    """
    Returns a string where:
        - Each token is encoded as "col@@#color@@text"
        - Tokens are separated by "@@@"
        - NEWLINES in the original code are kept exactly (not tokenized),
          so splitting by '\n' recovers the original code lines.
    """
    tokens = []
    col = 0  # column offset within current line

    iline = 0
    for tok_type, text in lex(code, lexer):
        if text == "":
            continue

        if "\n" in text:
            # Emit tokens for text *before* the newline
            parts = text.split("\n")

            # Handle all chunks before newline
            for i, chunk in enumerate(parts):
                if chunk:
                    color = "#" + token_color(tok_type, chunk)
                    if error_line is not None and iline + 1 == error_line:
                        color = "#ff0000"
                    token_repr = f"{col}@@{color}@@{chunk}"
                    tokens.append(token_repr)
                    col += len(chunk)

                if i < len(parts) - 1:
                    # Here comes a newline → emit it literally
                    tokens.append("\n")
                    iline += 1
                    col = 0

            continue

        # Normal token (no newline)
        color = "#" + token_color(tok_type, text)
        if error_line is not None and iline + 1 == error_line:
            color = "#ff0000"
        token_repr = f"{col}{FIELD_SEP}{color}{FIELD_SEP}{text}"
        tokens.append(token_repr)

        col += len(text)

    return TOKEN_SEP.join(tokens)


def process_input(line):
    log(f"Received line: {line}")
    t0 = time.time()
    if not line:
        return

    response = None
    try:
        msg = json.loads(base64.b64decode(line).decode("utf-8"))
        log(f"Received message: {msg}, {type(msg)}")

        action = msg.get("action", None)
        if action not in ["compile", "highlight"]:
            response = {"error": f"Invalid action '{action}'"}
            return

        modules = msg.get("code", None)
        if modules is None:
            response = {"error": "No code provided"}
            return

        code = modules[""]
        log(f"got modules {list(modules.keys())}")

        options = CompileOptions(**(msg.get("options", {})))
        t1 = time.time()
        response = compile_code(
            modules,
            options,
        )
        t2 = time.time()
        error_line = None
        if response and "error" in response and "line" in response["error"]:
            error_line = response["error"]["line"]
        highlighted = highlight(code, error_line=error_line)
        response["highlighted"] = highlighted

        stack_trace = response.get("error", {}).get("stack_trace", None)
        if stack_trace is not None:
            error("Error: " + response.get("error", {}).get("description", ""))
            error("stack_trace: \n" + str(stack_trace))

        lineno = msg.get("lineno", -1)
        column = msg.get("column", -1)
        if lineno >= 0 and column > 0:
            try:
                import jedi

                if len(modules) > 1:
                    tmpdir = Path(_jedi_project_dir)
                    (tmpdir / "__init__.py").write_text("", encoding="utf-8")
                    lib_path = tmpdir / "library"
                    lib_path.mkdir(exist_ok=True)
                    (lib_path / "__init__.py").write_text("", encoding="utf-8")

                    for mod_name, code in modules.items():
                        if mod_name == "":
                            path = tmpdir / "script.py"
                        else:
                            path = lib_path / (mod_name + ".py")
                        log("write module " + str(path))
                        log(code)
                        path.write_text(code, encoding="utf-8")

                    project = jedi.Project(path=tmpdir, added_sys_path=str(tmpdir))
                    script = jedi.Script(modules[""], path="script.py", project=project)
                else:
                    # no library modules, just use jedi.Script directly
                    script = jedi.Script(modules[""], path="script.py")

                # line_shift = len(all_code.splitlines()) - len(code.splitlines())
                # script = jedi.Script(all_code, path="script.py")
                log(f"Getting completions at {lineno}:{column}")
                completions = script.complete(line=lineno, column=column)
                log(f"Got {len(completions)} completions")
                if completions:
                    log(f"First completion: {completions[0].name} ({completions[0].type})")
                    response.update(format_completions(completions))
            except Exception as e:
                log(f"Jedi exception: {e}")
                error(f"Jedi exception: {e}")
        t3 = time.time()
        log(f"Processing times: parse {1000*(t1 - t0):.1f} ms, compile {1000*(t2 - t1):.1f} ms, jedi {1000*(t3 - t2):.1f} ms")

    except json.JSONDecodeError:
        response = {"error": {"message": "Invalid JSON format"}}
    except Exception as e:
        import traceback

        stack_trace = traceback.format_exc()
        response = {
            "error": {
                "description": f"Internal compiler error: {str(e)}",
                "stack_trace": stack_trace,
            }
        }
        error(f"Exception: {e}\n{stack_trace}")
    finally:
        if response is not None:
            log(f"Response: {response}")
            encoded = base64.b64encode(json.dumps(response).encode("utf-8")).decode(
                "ascii"
            )
            print(encoded, flush=True, file=_stdout)


async def main():
    try:
        print(get_pages_encoded(), flush=True, file=_stdout)
        log("Importing jedi")
        import jedi

        log("Imported jedi")

        jedi.preload_module("stationeers_pytrapic.symbols")
        log("Jedi preloaded successfully")
        while True:
            line = sys.stdin.readline()

            if not line:
                log("EOF reached, exiting...")
                break

            line = line.strip()
            if line == "EXIT":
                log("Received EXIT signal, quitting...")
                break

            process_input(line)
    except Exception as e:
        import traceback

        stack_trace = traceback.format_exc()
        log(f"Exception in main loop: {e}")
        error(f"Exception in main loop: {e}\n{stack_trace}")


if __name__ == "__main__":

    def at_exit_handler(*args, **kwargs):
        log(f"Exiting with args: {args}, kwargs: {kwargs}")
        if _log_file is not None:
            _log_file.close()
        if _err_file is not None:
            _err_file.close()
        if Path(_jedi_project_dir).exists():
            import shutil

            shutil.rmtree(_jedi_project_dir)

    atexit.register(at_exit_handler)
    asyncio.run(main())
