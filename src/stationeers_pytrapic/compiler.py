import astroid

from .compile_pass import *
from .generate_code import CompilerPassGenerateCode, CompilerPassGatherCode


class Compiler:
    def __init__(self):
        self.passes = [
            CompilerPassSetNodeData,
            CompilerPassCheckUsed,
            # CompilerPassAssignScope,
            # CompilerPassAssignSymbols,
            CompilerPassCheckConstValue,
            CompilerPassGenerateCode,
            CompilerPassGatherCode,
        ]

    def compile(self, src: str, append_original_line: bool = False):
        try:
            self.tree = astroid.parse(src)
            passes = [cls(self.tree) for cls in self.passes]
            for compiler_pass in passes:
                compiler_pass.run()
            return passes[-1].get_code(
                original_code=src, append_original_line=append_original_line
            )
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


def compile_code(src: str, append_original_line: bool = False):
    return Compiler().compile(src, append_original_line=append_original_line)
