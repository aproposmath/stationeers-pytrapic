import sys

_stdout = sys.stdout
sys.stdout = sys.stderr

import asyncio
import atexit
import base64
import datetime
import json
import sys

import time

from .compiler import CompileOptions, compile_code

# from .stationpedia import get_pages_encoded

_log_file = None  # Global log file handle
_err_file = None  # Global error file handle
ENABLE_LOGGING = __name__ == "__main__"
ENABLE_LOGGING = False


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
        if action not in ["compile"]:
            response = {"error": f"Invalid action '{action}'"}
            return

        modules = msg.get("code", None)
        if modules is None:
            response = {"error": "No code provided"}
            return

        log(f"got modules {list(modules.keys())}")

        options = CompileOptions(**(msg.get("options", {})))
        t1 = time.time()
        response = compile_code(
            modules,
            options,
        )
        t2 = time.time()

        stack_trace = response.get("error", {}).get("stack_trace", None)
        if stack_trace is not None:
            error("Error: " + response.get("error", {}).get("description", ""))
            error("stack_trace: \n" + str(stack_trace))

        t3 = time.time()
        log(
            f"Processing times: parse {1000*(t1 - t0):.1f} ms, compile {1000*(t2 - t1):.1f} ms, jedi {1000*(t3 - t2):.1f} ms"
        )

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
        # print(get_pages_encoded(), flush=True, file=_stdout)
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

    atexit.register(at_exit_handler)
    asyncio.run(main())
