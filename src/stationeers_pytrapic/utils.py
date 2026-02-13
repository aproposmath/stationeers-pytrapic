import logging
from enum import IntEnum

from astroid import nodes

logger = logging.getLogger("stationeers_pytrapic")


def calc_hash(name: str) -> int:
    import zlib

    val = zlib.crc32(name.encode())
    val = (val ^ 0x80000000) - 0x80000000
    return val


class OutputMode(IntEnum):
    """Defines the output mode for enum formatting, either keep their names or use their numbers."""

    VERBOSE = 0
    COMPACT = 1
    NUMERIC = 2


_output_mode = OutputMode.VERBOSE


def is_compact_output() -> bool:
    return _output_mode == OutputMode.COMPACT


def set_output_mode(mode: OutputMode):
    global _output_mode
    _output_mode = mode


def format_enum(enum_val) -> str | int:
    if _output_mode == OutputMode.VERBOSE:
        return enum_val.name
    else:
        return enum_val.value


_math_functions = {
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "atan2",
    "sqrt",
    "log",
    "exp",
}


def is_math_function(name: str) -> bool:
    return name in _math_functions


def is_builtin_function(name: str) -> bool:
    return name in ["HASH", "STR"]


def is_intrinsic_function(name: str) -> bool:
    from . import intrinsics

    return name in intrinsics.__dict__


def is_loadable_type(obj) -> bool:
    from . import symbols as sym

    if not hasattr(obj, "_load"):
        return False

    return isinstance(obj, (sym._DeviceLogicType, sym._StackValue, sym._DeviceSlotType))


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


def _e(value: int | float | str) -> float:
    from .types import compute_hash

    if isinstance(value, str) and value.startswith('HASH("'):
        value = compute_hash(value[6:-2], OutputMode.NUMERIC)
        return value

    if isinstance(value, str):
        raise CompilerError(f"Cannot evaluate non-hash string constant: {value}", None)

    return float(value)


def get_unop_instruction(op: str):
    return {
        "-": ("sub", lambda x: -_e(x)),
        "~": ("neg", lambda x: ~_e(x)),
        "not": ("seqz", lambda x: not _e(x)),
    }.get(op, (None, None))


def get_binop_instruction(op: str):
    comp = lambda op: "s" + get_comparison_suffix(op)
    return {
        "+": ("add", lambda x, y: _e(x) + _e(y)),
        "-": ("sub", lambda x, y: _e(x) - _e(y)),
        "*": ("mul", lambda x, y: _e(x) * _e(y)),
        "/": ("div", lambda x, y: _e(x) / _e(y)),
        "%": ("mod", lambda x, y: _e(x) % _e(y)),
        "**": ("pow", lambda x, y: _e(x) ** _e(y)),
        "and": ("and", lambda x, y: _e(x) and _e(y)),
        "or": ("or", lambda x, y: _e(x) and _e(y)),
        "^": ("xor", lambda x, y: int(_e(x)) ^ int(_e(y))),
        "&": ("and", lambda x, y: int(_e(x)) & int(_e(y))),
        ">>": ("srl", lambda x, y: int(_e(x)) >> int(_e(y))),
        "<<": ("sll", lambda x, y: int(_e(x)) << int(_e(y))),
        "==": (comp("=="), lambda x, y: x == y),
        "!=": (comp("!="), lambda x, y: x != y),
        "<": (comp("<"), lambda x, y: _e(x) < _e(y)),
        ">": (comp(">"), lambda x, y: _e(x) > _e(y)),
        "<=": (comp("<="), lambda x, y: _e(x) <= _e(y)),
        ">=": (comp(">="), lambda x, y: _e(x) >= _e(y)),
    }.get(op, (None, None))


def get_scope_name(node):
    if hasattr(node, "name") and is_builtin_name(node.name):
        return ""
    sc = node.scope()
    parents = []
    while sc and not isinstance(sc, nodes.Module):
        parents.append(sc.name)
        sc = sc.parent.scope() if sc.parent else None

    if isinstance(node, nodes.FunctionDef) or (
        isinstance(node, nodes.Name)
        and isinstance(node.parent, nodes.Call)
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

    if isinstance(node, nodes.FunctionDef):
        return scope + node.name
    elif isinstance(node, nodes.Attribute):
        return scope + node.expr.name + "." + node.attrname
    elif isinstance(node, nodes.Name):
        return scope + node.name
    else:
        raise CompilerError("Cannot get function name", node)


class CompilerError(Exception):
    def __init__(self, message, node=None):
        super().__init__(message)
        self.node = node

    def __str__(self):
        if self.node:
            return f"Compiler error at line {self.node.lineno}:{self.node.col_offset}: {super().__str__()}\n  {self.node.lineno:>6} | {self.node.as_string()}\n"
        return super().__str__()


def get_function_parent(node):
    for par in node.node_ancestors():
        if isinstance(par, nodes.FunctionDef):
            return par
    raise CompilerError("No parent function found", node)


def is_builtin_name(name: str) -> bool:
    from . import symbols

    return name != "__name__" and name in symbols.__dict__


def is_builtin_structure(val):
    from . import symbols, types, types_generated

    type_ = type(val)
    type_name = type_.__name__

    is_enum = not type_name.startswith("_") and type_name in types_generated.__dict__

    return is_enum or isinstance(
        val,
        (
            symbols._DeviceLogicType,
            symbols._DevicesLogicType,
            symbols._GenericStructures,
            symbols._GenericStructure,
            types._BaseStructure,
            types._BaseStructures,
            types.Stack,
        ),
    )


def get_loop_ancestor(node):
    for par in node.node_ancestors():
        if isinstance(par, nodes.FunctionDef):
            return node
        if isinstance(par, (nodes.For, nodes.While)):
            return par
    return node


def is_constant(node, data):
    from .types import constants

    if hasattr(node, "_ndata") and node._ndata.is_constant:
        return True, node._ndata.constant_value

    if isinstance(node, (int, float, str)):
        return True, node

    if isinstance(node, nodes.Const):
        return True, node.value

    if isinstance(node, nodes.Call):
        if not isinstance(node.func, nodes.Name):
            return False, None

        fname = node.func.name
        if fname in data.functions:
            if data.functions[fname].is_constexpr:
                value = eval_constexpr(data, node)
                return True, value
        if is_math_function(node.func.name):
            import math

            args = []
            for arg in node.args:
                arg_const, arg_value = is_constant(arg, data)
                if not arg_const:
                    return False, None
                args.append(arg_value)
            func = getattr(math, node.func.name, None)
            if func:
                try:
                    return True, func(*args)
                except Exception:
                    return False, None
            else:
                return False, None
        elif is_builtin_function(node.func.name):
            from . import symbols

            return True, getattr(symbols, node.func.name)(node.args[0].value)
        else:
            return False, None

    if isinstance(node, nodes.Name) and node.name in constants:
        return True, constants[node.name]

    if isinstance(node, nodes.BinOp):
        left_const, left_value = is_constant(node.left, data)
        right_const, right_value = is_constant(node.right, data)
        if left_const and right_const:
            _, func = get_binop_instruction(node.op)
            if func:
                try:
                    return True, func(left_value, right_value)
                except Exception:
                    return False, None

    if isinstance(node, nodes.UnaryOp):
        operand_const, operand_value = is_constant(node.operand, data)
        if operand_const:
            _, func = get_unop_instruction(node.op)
            if func:
                try:
                    return True, func(operand_value)
                except Exception:
                    return False, None

    if isinstance(node, (nodes.List, nodes.Tuple)):
        elements_value = []
        for el in node.elts:
            el_const, el_value = is_constant(el, data)
            if not el_const:
                return False, None
            elements_value.append(el_value)

        return True, elements_value

    if isinstance(node, nodes.Subscript):
        value_const, value_value = is_constant(node.value, data)
        slice_const, slice_value = is_constant(node.slice, data)
        if value_const and slice_const:
            try:
                return True, value_value[slice_value]
            except Exception:
                return False, None

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
        if isinstance(par, (nodes.For, nodes.While)):
            # print("no constant in loop", inferred, node)
            return False, None
        if isinstance(par, nodes.FunctionDef):
            break

    if isinstance(inferred, nodes.Const):
        return True, inferred.value

    return False, None
    if res:
        try:
            lookup = node.lookup(node.name)
            if len(lookup[1]) > 1:
                res = False
        except:
            res = False
    if res and isinstance(node, nodes.Name):
        print(res, "check const", node, inferred)
        # print("scope", node.scope())
        print("lookup", node.lookup(node.name))
    elif res and isinstance(inferred[0], nodes.Name):
        print(res, "check const", node, inferred)
        # print("scope", node.scope())
        print("lookup", inferred[0].lookup(inferred[0].name))
    elif res:
        print(res, "check const", node, inferred)
    return res


_all_hashes = set()


def format_int(value):
    if not _all_hashes:
        from . import symbols

        for name in dir(symbols):
            val = getattr(symbols, name)
            if hasattr(val, "_hash"):
                h = val._hash
                if isinstance(h, int):
                    _all_hashes.add(h)

    if value <= 10000 or value in _all_hashes:
        return str(value)

    return f"${value:X}"


_eval_constexpr_cache = {}

try:
    import js as _js

    _is_pyodide = True
except ImportError:
    _is_pyodide = False


def eval_constexpr(data, call_node):
    if data.constexpr_functions_code is None:
        code = ""
        for scope, funcs in data.constexpr_functions.items():
            if scope == "":
                code += funcs
            else:
                code += f"class {scope}:\n"
                for line in funcs.splitlines():
                    code += "    " + line + "\n"
            code += "\n"
        data.constexpr_functions_code = code

    code = f"""
from stationeers_pytrapic.types import *
from stationeers_pytrapic.types_generated import *
from stationeers_pytrapic.utils import calc_hash as HASH

def constexpr(f):
    return f

{data.constexpr_functions_code}

"""
    if _is_pyodide:
        code += f"\nresult = {call_node.as_string()}\n"
    else:
        code += f"\nprint({call_node.as_string()})\n"
    if code in _eval_constexpr_cache:
        return _eval_constexpr_cache[code]

    if _is_pyodide:
        vars = {}
        try:
            exec(code, vars, vars)
            result = vars["result"]
        except Exception as e:
            raise CompilerError(
                f"Error during evaluating constexpr function call {call_node.as_string()}:\n{e}",
                call_node,
            )
        try:
            result = int(result)
            result = format_int(result)
        except ValueError:
            pass
        _eval_constexpr_cache[code] = result
        return result

    # run this in a separate process to avoid side effects and have a timeout and proper cleanup
    import subprocess
    import sys

    process = subprocess.Popen(
        [sys.executable, "-c", code],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        stdout, stderr = process.communicate(timeout=1)

    except subprocess.TimeoutExpired:
        raise CompilerError(
            f"Timeout during evaluating constexpr function call {call_node.as_string()}",
            call_node,
        )
    if process.returncode != 0:
        raise CompilerError(
            f"Error during evaluating constexpr function call {call_node.as_string()}:\n{stderr.decode()}",
            call_node,
        )
    result = stdout.decode().strip()
    try:
        result = int(result)
        result = format_int(result)
    except ValueError:
        pass

    _eval_constexpr_cache[code] = result
    return result
