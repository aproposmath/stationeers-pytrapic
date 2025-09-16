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


def get_comparison_suffix(op: str):
    return {
        "==": "eq",
        "!=": "ne",
        "<": "lt",
        "<=": "le",
        ">": "gt",
        ">=": "ge",
    }[op]


def get_negated_comparison_suffix(op: str):
    return {
        "==": "ne",
        "!=": "eq",
        "<": "ge",
        "<=": "gt",
        ">": "le",
        ">=": "lt",
    }[op]


def get_unop_instruction(op: str):
    return {
        "-": ("sub", lambda x: -x),
        "~": ("neg", lambda x: ~x),
        "not": ("seqz", lambda x: not x),
    }.get(op, (None, None))


def get_binop_instruction(op: str):
    comp = lambda op: "s" + get_comparison_suffix(op)
    return {
        "+": ("add", lambda x, y: x + y),
        "-": ("sub", lambda x, y: x - y),
        "*": ("mul", lambda x, y: x * y),
        "/": ("div", lambda x, y: x / y),
        "%": ("mod", lambda x, y: x % y),
        "**": ("pow", lambda x, y: x**y),
        "and": ("and", lambda x, y: x and y),
        "or": ("or", lambda x, y: x and y),
        "==": (comp("=="), lambda x, y: x == y),
        "!=": (comp("!="), lambda x, y: x != y),
        "<": (comp("<"), lambda x, y: x < y),
        ">": (comp(">"), lambda x, y: x > y),
        "<=": (comp("<="), lambda x, y: x <= y),
        ">=": (comp(">="), lambda x, y: x >= y),
    }.get(op, (None, None))


def get_scope_name(node):
    if hasattr(node, "name") and is_builtin_name(node.name):
        return ""
    sc = node.scope()
    parents = []
    while sc and not isinstance(sc, astroid.Module):
        parents.append(sc.name)
        sc = sc.parent.scope() if sc.parent else None

    if isinstance(node, astroid.FunctionDef) or (
        isinstance(node, astroid.Name)
        and isinstance(node.parent, astroid.Call)
        and node == node.parent.func
    ):
        parents = parents[1:]

    if sc.name:
        parents.append(sc.name)

    scope_name = ".".join(reversed(parents))
    scope = node.scope()

    if hasattr(node, "name") and node.name not in scope.locals:
        scope_name = (
            sc.name
        )  # if the name is not in the local scope, it is a global name

    # print("scope name", scope_name, node)
    return scope_name


def get_function_name(node):
    scope = get_scope_name(node)
    if scope:
        scope += "."

    if isinstance(node, astroid.FunctionDef):
        return scope + node.name
    elif isinstance(node, astroid.Attribute):
        return scope + node.expr.name + "." + node.attrname
    elif isinstance(node, astroid.Name):
        return scope + node.name
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

    return name != "__name__" and name in symbols.__dict__


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
