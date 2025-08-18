import astroid

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
            CompilerPassGenerateCode,
            # CompilerPassAssignRegisters,
            CompilerPassGatherCode,
        ]
        self.options = options

    def compile(self, src: str):
        try:
            self.tree = astroid.parse(src)
            self.data = CodeData(src, self.tree, self.options)
            for pass_cls in self.passes:
                compiler_pass = pass_cls(self.data)
                compiler_pass.run()
            return self.data.result
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


def compile_code(src: str, comments: bool = False, compact: bool = False):
    original_code_as_comment = comments and not compact
    inline_functions = compact
    remove_labels = compact
    options = CompileOptions(
        original_code_as_comment=original_code_as_comment,
        inline_functions=inline_functions,
        remove_labels=remove_labels,
    )

    return Compiler(options).compile(src)
