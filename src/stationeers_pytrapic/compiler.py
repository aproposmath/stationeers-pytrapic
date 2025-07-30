import astroid

from .compile_pass import *
from .generate_code import CompilerPassGatherCode, CompilerPassGenerateCode


class Compiler:
    def __init__(self):
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
            CompilerPassGenerateCode,
            # CompilerPassAssignRegisters,
            CompilerPassGatherCode,
        ]

    def compile(
        self, src: str, comments: bool = False, compact: bool = False
    ):
        try:
            self.tree = astroid.parse(src)
            self.data = CodeData(self.tree)
            for pass_cls in self.passes:
                compiler_pass = pass_cls(self.data)
                compiler_pass.run()
            if isinstance(compiler_pass, CompilerPassGatherCode):
                return compiler_pass.get_code(
                    original_code=src,
                    comments=comments,
                    compact=compact,
                )
            return {"code": "No code generated"}
        except CompilerError as e:
            return {"error": str(e)}
        except astroid.AstroidSyntaxError as e:
            return {"error": f"Syntax error: {str(e)}"}
        except Exception as e:
            import traceback

            stack_trace = traceback.format_exc()
            return {
                "error": f"Internal compiler error: {str(e)}",
                "stack_trace": stack_trace,
            }


def compile_code(
    src: str, comments: bool = False, compact: bool = False
):
    return Compiler().compile(
        src, comments=comments, compact=compact
    )
