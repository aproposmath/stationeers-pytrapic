_last_time = None
_DO_TIMING = False


def time(s=""):
    if not _DO_TIMING:
        return
    import time

    global _last_time

    if _last_time is None:
        _last_time = time.time()
        return

    now = time.time()
    d = now - _last_time
    print(f"{s:30}: {1000*d:.0f} ms")
    _last_time = now


time()
import astroid

from . import types
from .compile_pass import *
from .generate_code import CompilerPassGatherCode, CompilerPassGenerateCode
from .utils import set_output_mode, OutputMode

time("import")


class Compiler:
    _raise_exceptions = False

    def __init__(self, options: CompileOptions):
        self.passes = [
            CompilerPassSetModuleNames,
            CompilerPassHandleConstexpr,
            CompilerPassBoolOpToBinOp,
            CompilerPassSetNodeData,
            CompilerPassCreateFunctionData,
            CompilerPassCheckConstValue,
            CompilerPassCheckUsed,
            CompilerPassFindNames,
            CompilerPassResetReadWritten,
            CompilerPassSetReadWritten,
            CompilerPassCheckReadWritten,
            CompilerPassCheckConstValueAssign,
            # CompilerPassListSymbols,
            CompilerPassCheckReturnValues,
            CompilerPassGenerateCode,
            CompilerPassGatherCode,
        ]
        self.options = options

    def _parse(self, src: str):
        src_stripped = src.lstrip()
        if src_stripped.startswith("require") or src_stripped.startswith("--"):
            from .parse_lua import parse_lua

            return parse_lua(src)
        else:
            return astroid.parse(src)

    def compile(self, src: str | dict):
        time("start")
        try:
            if isinstance(src, str):
                src = {"": src}

            code = src[""]
            modules = {k: self._parse(v) for k, v in src.items()}
            self.tree = modules.pop("")

            time("parse")
            self.data = CodeData(code, self.tree, self.options, modules=modules)
            time("codedata")
            for pass_cls in self.passes:
                compiler_pass = pass_cls(self.data)
                compiler_pass.run()
                time("pass " + pass_cls.__name__)
            return self.data.result
        except CompilerError as e:
            if self._raise_exceptions:
                raise e
            msg = {"description": str(e)}
            if e.node:
                msg["line"] = e.node.lineno
                msg["column"] = e.node.col_offset
                msg["line_end"] = e.node.end_lineno
                msg["column_end"] = e.node.end_col_offset
            return {
                "error": msg,
            }
        except astroid.AstroidSyntaxError as e:
            if self._raise_exceptions:
                raise e

            d = {
                "error": {
                    "description": f"Syntax error: {str(e)}",
                }
            }
            if isinstance(e.error, SyntaxError):
                d["error"].update(
                    {
                        "line": e.error.lineno,
                        "column": e.error.offset,
                    }
                )
            return d
        except Exception as e:
            if self._raise_exceptions:
                raise e
            import traceback

            stack_trace = traceback.format_exc()
            return {
                "error": {
                    "description": f"Internal compiler error: {str(e)}",
                    "stack_trace": stack_trace,
                }
            }


def compile_code(
    src: str | dict,
    options: CompileOptions | dict,
):
    if isinstance(options, dict):
        options = CompileOptions(**options)

    main_module = src[""] if isinstance(src, dict) else src
    if "pytrapic:" in main_module:
        for line in main_module.splitlines():
            if "pytrapic:" not in line:
                continue
            line = line.strip()
            if not line.startswith("#"):
                continue
            tokens = line.split("#", 1)
            if len(tokens) < 2:
                continue
            tokens = tokens[1].split("pytrapic:", 1)
            if len(tokens) < 2:
                continue
            tokens = tokens[1].strip().split(",")
            for tag in tokens:
                tag = tag.strip().replace("-", "_")
                value = not tag.startswith("no_")
                if not value:
                    tag = tag[3:].strip()

                if hasattr(options, tag):
                    setattr(options, tag, value)

    set_output_mode(OutputMode.COMPACT if options.compact else OutputMode.VERBOSE)
    return Compiler(options).compile(src)
