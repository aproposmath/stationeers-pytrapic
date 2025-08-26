import astroid

from . import types
from .compile_pass import *
from .generate_code import CompilerPassGatherCode, CompilerPassGenerateCode


class Compiler:
    def __init__(self, options: CompileOptions):
        self.passes = [
            CompilerPassSetNodeData,
            CompilerPassCheckUsed,
            CompilerPassFindNames,
            CompilerPassResetReadWritten,
            CompilerPassSetReadWritten,
            CompilerPassCheckReadWritten,
            # CompilerPassListSymbols,
            # CompilerPassCheckConstValue,
            # CompilerPassCheckConstValue,
            # CompilerPassCheckRead,
            CompilerPassCheckReturnValues,
            CompilerPassCreateFunctionData,
            CompilerPassGenerateCode,
            # CompilerPassAssignRegisters,
            CompilerPassGatherCode,
        ]
        self.options = options

    def compile(self, src: str):
        try:
            src_stripped = src.lstrip()
            if src_stripped.startswith("require") or src_stripped.startswith("--"):
                from .parse_lua import parse_lua

                self.tree = parse_lua(src)
            else:
                self.tree = astroid.parse(src)
            self.data = CodeData(src, self.tree, self.options)
            for pass_cls in self.passes:
                compiler_pass = pass_cls(self.data)
                compiler_pass.run()
            return self.data.result
        except CompilerError as e:
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
            import traceback

            stack_trace = traceback.format_exc()
            return {
                "error": {
                    "description": f"Internal compiler error: {str(e)}",
                    "stack_trace": stack_trace,
                }
            }


def compile_code(
    src: str,
    comments: bool = False,
    compact: bool = False,
    append_version: bool = False,
):
    original_code_as_comment = comments and not compact
    inline_functions = compact
    remove_labels = compact
    options = CompileOptions(
        original_code_as_comment=original_code_as_comment,
        inline_functions=inline_functions,
        remove_labels=remove_labels,
        append_version=append_version,
    )

    types.hash_mode = types.HashMode.COMPACT if compact else types.HashMode.VERBOSE

    return Compiler(options).compile(src)
