import asyncio
import atexit
import base64
import datetime
import json
import sys

from pygments import highlight as _highlight
from pygments.formatters import BBCodeFormatter
from pygments.lexers import LuaLexer, PythonLexer

from .compiler import compile_code

formatter = BBCodeFormatter(style="solarized-light")

replace = lambda s: s.replace("[", "<").replace("]", ">")
for ttype in formatter.styles:
    start, end = formatter.styles[ttype]
    if "657b83" in start or "657b83" in end:
        formatter.styles[ttype] = "", ""
    else:
        formatter.styles[ttype] = replace(start), replace(end)

_log_file = None  # Global log file handle
ENABLE_LOGGING = __name__ == "__main__"


def log(msg):
    global _log_file
    if ENABLE_LOGGING:
        if _log_file is None:
            _log_file = open("mod_daemon.log", "w")
        _log_file.write(f"{datetime.datetime.now().isoformat()} - {msg}\n")
        _log_file.flush()


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

        code = msg.get("code", None)
        if code is None:
            response = {"error": "No code provided"}
            return

        compact = msg.get("compact", False)
        append_version = msg.get("append_version", True)
        comments = msg.get("comments", False)
        response = compile_code(
            code,
            comments=comments,
            compact=compact,
            append_version=append_version,
        )
        error_line = None
        if response and "error" in response and "line" in response["error"]:
            error_line = response["error"]["line"]
        highlighted = highlight(code, error_line=error_line)
        response["highlighted"] = highlighted

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
    finally:
        if response is not None:
            log(f"Response: {response}")
            encoded = base64.b64encode(json.dumps(response).encode("utf-8")).decode(
                "ascii"
            )
            print(encoded, flush=True)


async def main():
    try:
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
        log(f"Exception in main loop: {e}")


if __name__ == "__main__":

    def at_exit_handler(*args, **kwargs):
        log(f"Exiting with args: {args}, kwargs: {kwargs}")
        if _log_file is not None:
            _log_file.close()

    atexit.register(at_exit_handler)

    token = sys.stdin.readline().strip()
    log(f"Token received: {token}")
    if token != "READY":
        log("Invalid token, exiting...")
        sys.exit(1)

    print("READY", flush=True)  # Notify parent that we are ready

    asyncio.run(main())
