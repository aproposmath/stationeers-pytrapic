import logging
from dataclasses import dataclass
from typing import Literal

import astroid

from .utils import is_constant, logger


class CompilerError(Exception):
    def __init__(self, message, node=None):
        super().__init__(message)
        self.node = node

    def __str__(self):
        if self.node:
            return f"Compiler error at line {self.node.lineno}:{self.node.col_offset}:\n\t{super().__str__()}"
        return super().__str__()


@dataclass
class CodeLine:
    code: str = ""
    comment: str = ""
    indent: int = 0
    node: astroid.NodeNG = None


class CodeData:
    _symbol_counter: int = 0
    symbols: dict[astroid.NodeNG, dict[str, astroid.NodeNG]] = None
    symbols_by_name: dict[astroid.NodeNG, dict[str, astroid.NodeNG]] = None

    def __init__(self):
        self.symbols = {}
        self.scopes = {}
        self._symbol_counter = 0

    def get_symbol_name(self, node: astroid.NodeNG) -> str:
        if hasattr(node, "name") and node.name:
            return node.name

        name = f"symbol_{self._symbol_counter}"
        self._symbol_counter += 1
        return name

    def get_symbol(self, node: astroid.NodeNG) -> str:
        scope_name = node.scope().name

        if scope_name not in self.symbols:
            self.symbols[scope_name] = {}
            self.symbols_by_name[scope_name] = {}


class Symbol:
    def __init__(self, i, scope: str, name: str):
        self.id = i
        self.name = name
        self.scope = scope
        self.nodes_reading = set()
        self.nodes_writing = set()

    def __str__(self):
        return f"__symbol_{self.id:02}"

    def __repr__(self):
        return self.__str__()


class NodeData:
    CodeType = Literal["", "end", "else"]
    is_used: bool = None
    is_reachable: bool = None
    is_constant: bool = None
    is_constant_value: bool = None
    constant_value: str | float | None = None
    node: astroid.NodeNG = None
    code_data: CodeData = None
    indent: int = 0
    is_compiled = False

    code: dict[CodeType, list[CodeLine]] = None
    result = None

    scope: str = None
    symbol: str = None

    def __init__(self, node, code_data):
        self.code_data = code_data
        self.node = node
        self.is_used = None
        self.is_reachable = None
        self.is_constant = None
        self.is_constant_value = None
        self.constant_value = None

        self.code = {"": [], "end": [], "else": []}

    def _add(
        self, code: str, comment: str = "", indent: int = 0, code_type: CodeType = ""
    ):
        code_line = CodeLine(code, comment, node=self.node, indent=self.indent + indent)

        if code_type not in self.code:
            self.code[code_type] = []

        self.code[code_type].append(code_line)

    def add(self, code: str, comment: str = "", indent: int = 0):
        self._add(code, comment, indent, code_type="")

    def add_end(self, code: str, comment: str = "", indent: int = 0):
        self._add(code, comment, indent, code_type="end")

    def add_else(self, code: str, comment: str = "", indent: int = 0):
        self._add(code, comment, indent, code_type="else")

    def __str__(self):
        return f"NodeData(is_used={self.is_used}, is_reachable={self.is_reachable}, is_constant={self.is_constant}, is_constant_value={self.is_constant_value})"


class CompilerPass:
    def __init__(self, tree: astroid.Module):
        self.tree = tree

        self._handlers = {
            astroid.Pass: self.handle_pass,
            astroid.Global: self.handle_global,
            astroid.Module: self.handle_module,
            astroid.FunctionDef: self.handle_function_def,
            astroid.Expr: self.handle_expr,
            astroid.Import: self.handle_import,
            astroid.While: self.handle_while,
            astroid.IfExp: self.handle_ifexp,
            astroid.Attribute: self.handle_attribute,
            astroid.Compare: self.handle_compare,
            astroid.ImportFrom: self.handle_import_from,
            astroid.Call: self.handle_call,
            astroid.Name: self.handle_name,
            astroid.Const: self.handle_const,
            astroid.Assign: self.handle_assign,
            astroid.AssignName: self.handle_assign_name,
            astroid.AssignAttr: self.handle_assign_attr,
            astroid.Subscript: self.handle_subscript,
            astroid.If: self.handle_if,
            astroid.BinOp: self.handle_binop,
            astroid.Arguments: self.handle_arguments,
        }

    def _log(self, level, *args):
        if logger.isEnabledFor(level):
            logger.log(level, f"{type(self).__name__}: " + " ".join(map(str, args)))

    def _info(self, *args):
        self._log(logging.INFO, *args)

    def _debug(self, *args):
        self._log(logging.DEBUG, *args)

    def _error(self, *args):
        self._log(logging.ERROR, *args)

    def _warning(self, *args):
        self._log(logging.WARNING, *args)

    def ignore_nodes(self, *node_types):
        for node_type in node_types:
            if node_type in self._handlers:
                self._handlers[node_type] = self.handle_ignore

    def _visit_node_recursive(self, node: astroid.NodeNG):
        self._debug("_visit_node_recursive", node)
        self._visit_node(node)
        for child in node.get_children():
            self._visit_node_recursive(child)

    def _visit_node(self, node: astroid.NodeNG):
        self._debug("_visit_node", node)
        if type(node) not in self._handlers:
            raise CompilerError(
                f"Unsupported node type '{type(node)}' in compiler pass '{type(self).__name__}'",
                node,
            )
        self._handlers[type(node)](node)

    def run(self):
        self._info("run")
        self._visit_node_recursive(self.tree)

    def handle_arguments(self, node: astroid.Arguments):
        self.handle_node(node)

    def handle_node(self, node):
        raise NotImplementedError(
            f"Unsupported node type '{type(node)}' in compiler pass '{type(self).__name__}'"
        )

    def handle_pass(self, node: astroid.Pass):
        self.handle_node(node)

    def handle_module(self, node: astroid.Module):
        self.handle_node(node)

    def handle_function_def(self, node: astroid.FunctionDef):
        self.handle_node(node)

    def handle_expr(self, node: astroid.Expr):
        self.handle_node(node)

    def handle_import(self, node: astroid.Import):
        self.handle_node(node)

    def handle_while(self, node: astroid.While):
        self.handle_node(node)

    def handle_ifexp(self, node: astroid.IfExp):
        self.handle_node(node)

    def handle_attribute(self, node: astroid.Attribute):
        self.handle_node(node)

    def handle_compare(self, node: astroid.Compare):
        self.handle_node(node)

    def handle_import_from(self, node: astroid.ImportFrom):
        self.handle_node(node)

    def handle_call(self, node: astroid.Call):
        self.handle_node(node)

    def handle_name(self, node: astroid.Name):
        self.handle_node(node)

    def handle_const(self, node: astroid.Const):
        self.handle_node(node)

    def handle_assign_name(self, node: astroid.AssignName):
        self.handle_node(node)

    def handle_assign_attr(self, node: astroid.AssignAttr):
        self.handle_node(node)

    def handle_assign(self, node: astroid.Assign):
        self.handle_node(node)

    def handle_subscript(self, node: astroid.Subscript):
        self.handle_node(node)

    def handle_if(self, node: astroid.If):
        self.handle_node(node)

    def handle_binop(self, node: astroid.BinOp):
        self.handle_node(node)

    def handle_ignore(self, node: astroid.NodeNG):
        pass

    def handle_global(self, node: astroid.Global):
        self.handle_node(node)


class CompilerPassSetNodeData(CompilerPass):
    def __init__(self, tree: astroid.Module):
        super().__init__(tree)
        self.code_data = CodeData()

    def handle_node(self, node: astroid.NodeNG):
        if hasattr(node, "_ndata"):
            raise ValueError(
                f"Node {node} already has _ndata set. "
                "This pass should only be run once per node."
            )
        node._ndata = NodeData(node, self.code_data)


def check_used(node: astroid.NodeNG):
    data = node._ndata
    if data.is_used is not None:
        return data.is_used

    if isinstance(node, astroid.While):
        if isinstance(node.test, astroid.Const):
            data.is_used = node.test.value
            return data.is_used
        else:
            data.is_used = True

    if isinstance(node, astroid.Module):
        data.is_used = True

    data.is_used = True

    return data.is_used


def mark_used_nodes(node: astroid.NodeNG, used: bool | None = None) -> None:
    data = node._ndata
    if isinstance(node, astroid.Module):
        used = True
        data.used = True

    if data.is_used is None:
        used = used and check_used(node)
        data.is_used = used

    for child in node.get_children():
        mark_used_nodes(child, data.is_used)


class CompilerPassCheckConstValue(CompilerPass):
    def handle_node(self, node: astroid.Module):
        is_const, value = is_constant(node)
        node._ndata.is_constant_value = is_const
        if is_const:
            node._ndata.constant_value = value


class CompilerPassCheckUsed(CompilerPass):
    def handle_node(self, node: astroid.NodeNG):
        pass

    def handle_module(self, node: astroid.Module):
        node._ndata.is_used = True
        mark_used_nodes(node)


class CompilerPassAssignSymbols(CompilerPass):
    def handle_module(self, node: astroid.FunctionDef):
        self.tree._ndata.symbols[node] = node.locals.copy()

    def handle_function_def(self, node: astroid.FunctionDef):
        self.tree._ndata.symbols[node] = node.locals.copy()

    def handle_node(self, node: astroid.Assign):
        pass
