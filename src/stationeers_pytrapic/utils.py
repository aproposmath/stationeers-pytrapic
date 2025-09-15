import logging

import astroid

logger = logging.getLogger("stationeers_pytrapic")


def is_builtin_function(name: str) -> bool:
    return name in ["HASH", "STR"]


def is_intrinsic_function(name: str) -> bool:
    from . import intrinsics

    return name in intrinsics.__dict__


def is_loadable_type(obj) -> bool:
    from . import symbols as sym

    return hasattr(obj, "_load") and isinstance(
        obj, (sym._DeviceLogicType, sym._StackValue, sym._DeviceSlotType)
    )


def is_storable_type(obj) -> bool:
    from . import symbols as sym

    return hasattr(obj, "_load") and isinstance(
        obj, (sym._DeviceLogicType, sym._StackValue, sym._DeviceSlotType)
    )


def get_unop_instruction(op: str):
    return {
        "-": ("sub", lambda x: -x),
        "~": ("neg", lambda x: ~x),
        "not": ("seqz", lambda x: not x),
    }.get(op, (None, None))


def get_binop_instruction(op: str):
    return {
        "+": ("add", lambda x, y: x + y),
        "-": ("sub", lambda x, y: x - y),
        "*": ("mul", lambda x, y: x * y),
        "/": ("div", lambda x, y: x / y),
        "%": ("mod", lambda x, y: x % y),
        "**": ("pow", lambda x, y: x**y),
        "and": ("and", lambda x, y: x and y),
        "or": ("or", lambda x, y: x and y),
    }.get(op, (None, None))


def get_function_name(node):
    if isinstance(node, astroid.FunctionDef):
        scope = node.parent.scope()
        if scope.name:
            return scope.name + "." + node.name
        return node.name
    elif isinstance(node, astroid.Attribute):
        return node.expr.name + "." + node.attrname
    elif isinstance(node, astroid.Name):
        return node.name
    else:
        raise CompilerError("Cannot get function name", node)


class CompilerError(Exception):
    def __init__(self, message, node=None):
        super().__init__(message)
        self.node = node

    def __str__(self):
        if self.node:
            return f"Compiler error at line {self.node.lineno}:{self.node.col_offset}:\n\t{super().__str__()}"
        return super().__str__()


def get_function_parent(node):
    for par in node.node_ancestors():
        if isinstance(par, astroid.FunctionDef):
            return par
    raise CompilerError("No parent function found", node)


def is_builtin_name(name: str) -> bool:
    from . import symbols

    return name in symbols.__dict__


def is_builtin_structure(val):
    from . import symbols, types

    return isinstance(
        val,
        (
            symbols._GenericStructures,
            symbols._GenericStructure,
            types._BaseStructure,
            types._BaseStructures,
            types.Stack,
        ),
    )


def get_loop_ancestor(node):
    for par in node.node_ancestors():
        if isinstance(par, astroid.FunctionDef):
            return node
        if isinstance(par, (astroid.For, astroid.While)):
            return par
    return node


def is_constant(node):
    from .types import constants

    if isinstance(node, (int, float, str)):
        return True, node

    if isinstance(node, astroid.Const):
        return True, node.value

    if isinstance(node, astroid.Call):
        if isinstance(node.func, astroid.Name) and is_builtin_function(node.func.name):
            from . import symbols

            return True, getattr(symbols, node.func.name)(node.args[0].value)
        else:
            return False, None

    if isinstance(node, astroid.Name) and node.name in constants:
        return True, constants[node.name]

    try:
        inferred = node.inferred()
    except Exception:
        return False, None

    return False, None

    if len(inferred) > 1 or len(inferred) == 0:
        return False, None

    inferred = inferred[0]

    # check if a parent is a while or for loop -> take care! the var could be ovewritten multiple times
    for par in node.node_ancestors():
        if isinstance(par, (astroid.For, astroid.While)):
            # print("no constant in loop", inferred, node)
            return False, None
        if isinstance(par, astroid.FunctionDef):
            break

    if isinstance(inferred, astroid.Const):
        return True, inferred.value

    return False, None
    if res:
        try:
            lookup = node.lookup(node.name)
            if len(lookup[1]) > 1:
                res = False
        except:
            res = False
    if res and isinstance(node, astroid.Name):
        print(res, "check const", node, inferred)
        # print("scope", node.scope())
        print("lookup", node.lookup(node.name))
    elif res and isinstance(inferred[0], astroid.Name):
        print(res, "check const", node, inferred)
        # print("scope", node.scope())
        print("lookup", inferred[0].lookup(inferred[0].name))
    elif res:
        print(res, "check const", node, inferred)
    return res


import re


def extract_library_imports(source: str) -> list[str]:
    """
    Find 'from library import xyz' statements using regex.
    Returns a list of module names like 'library.xyz'.
    """
    pattern = re.compile(r"^\s*from\s+library\s+import\s+(\w+)", re.MULTILINE)
    matches = pattern.findall(source)
    return [f"library.{name}" for name in matches]


def wrap_module(name: str, source: str) -> str:
    """
    Wrap the given module source code in a class named after the module.
    """
    class_name = name.split(".")[-1]
    lines = source.strip().splitlines()
    indented = "\n".join("    " + line if line.strip() else "" for line in lines)
    return f"class {class_name}:\n{indented}\n"


def inject_modules_simple(modules: dict[str, str]) -> str:
    """
    Injects imported library modules as class-wrapped code into the main module.
    """
    main_source = modules.get("", "")
    imported_modules = extract_library_imports(main_source)

    seen = set()
    injected_parts = []

    for mod in imported_modules:
        if mod not in modules:
            raise ValueError(f"Module '{mod}' not found in modules dictionary.")
        if mod in seen:
            continue
        seen.add(mod)
        injected_parts.append(wrap_module(mod, modules[mod]))

    # Finally add the main source
    src = "from stationeers_pytrapic.symbols import *\n"
    for line in main_source.splitlines():
        if line.strip().startswith("from library import"):
            continue
        if line.strip().startswith("from stationeers_pytrapic.symbols import *"):
            continue
        src += line + "\n"

    injected_parts.append(src)

    return "\n\n".join(injected_parts)
