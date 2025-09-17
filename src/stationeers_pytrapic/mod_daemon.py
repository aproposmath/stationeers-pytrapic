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

from .compiler import CompileOptions, compile_code
from .stationpedia import get_pages_encoded


def _get_ignore_symbol_names():
    import jedi

    s = jedi.Script("")
    completions = s.complete(1, 0)
    names = set((c.name for c in completions))
    for n in ["True", "False", "while", "if", "else", "def", "pow", "abs"]:
        if n in names:
            names.remove(n)
    return names


formatter = BBCodeFormatter(style="solarized-light")

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

_jedi_project_dir = tempfile.mkdtemp(prefix="jedi_project_")


def format_completion(c):
    name = f"<b>{c.name}</b>"
    type_ = f"<color=#8888ff><i>{c.type}</i></color>"
    return f"{name} - {type_}"


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
        "tooltip": result,
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


def highlight(code, error_line=None):
    lines = _highlight(code, get_lexer(code), formatter).splitlines()
    for i, line in enumerate(lines):
        if error_line is not None and i + 1 == error_line:
            lines[i] = "<color=#ff0000>" + line + "</color>"
        else:
            lines[i] = "<color=#ffffff>" + line + "</color>"
    return "\n".join(lines)


def process_input(line):
    log(f"Received line: {line}")
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
        response = compile_code(
            modules,
            options,
        )
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
                    response.update(format_completions(completions))
            except Exception as e:
                log(f"Jedi exception: {e}")
                error(f"Jedi exception: {e}")

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
