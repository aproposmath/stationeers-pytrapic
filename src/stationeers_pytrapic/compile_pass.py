import logging
from dataclasses import dataclass, field
from typing import Literal

import astroid

from . import symbols, types
from .utils import is_builtin_name, is_constant, logger

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


@dataclass
class SymbolData:
    name: str
    scope: str = ""
    code_expr: str | types._BaseStructure | types._BaseStructures = ""

    nodes_reading: list[astroid.NodeNG] = field(default_factory=list)
    nodes_writing: list[astroid.NodeNG] = field(default_factory=list)

    @property
    def is_overwritten(self) -> int:
        return len(self.nodes_writing) > 1

    @property
    def is_written(self) -> int:
        return len(self.nodes_writing)

    @property
    def is_read(self) -> int:
        return len(self.nodes_reading)

    @property
    def is_builtin_object(self) -> bool:
        return isinstance(self.code_expr, types._BaseStructure) or isinstance(
            self.code_expr, types._BaseStructures
        )

    @property
    def is_register(self) -> bool:
        return isinstance(self.code_expr, str) and self.code_expr.startswith(
            "__register."
        )

@dataclass
class FunctionData:
    node: astroid.FunctionDef
    calling_nodes: list[astroid.Call] = field(default_factory=list)
    code: list[CodeLine] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self.node.name if self.node else ""

    @property
    def is_inlined(self) -> bool:
        return len(self.calling_nodes) == 1

    @property
    def is_called(self) -> bool:
        return len(self.calling_nodes) > 0

@dataclass
class CodeData:
    tree: astroid.Module
    symbols: dict[str, dict[str, SymbolData]]
    register_map: dict[str, str]
    functions: dict[str, FunctionData]

    def __init__(self, tree: astroid.Module):
        self.tree = tree
        self.symbols = {"": {}}
        self.register_map = None
        self.functions = {}

    def _scope_name(self, node: astroid.AssignName | astroid.Name) -> str:
        if isinstance(node.parent, astroid.Call):
            return ""  # no nested functions, all functions are global

        if isinstance(node, astroid.FunctionDef) or (
            isinstance(node, astroid.Name) and isinstance(node.parent, astroid.Call)
        ):
            return ""

        scope = node.scope()
        if hasattr(node, "name") and node.name not in scope.locals:
            return ""  # if the name is not in the local scope, it is a global name
        if scope.name not in self.symbols:
            self.symbols[scope.name] = {}
        return scope.name

    def get_tmp_sym_data(self, node: astroid.NodeNG, name: str) -> SymbolData:
        scope = self._scope_name(node)
        local_symbols = self.symbols[scope]
        local_symbols[name] = SymbolData(name)
        return local_symbols[name]

    def get_sym_data(
        self, node: astroid.AssignName | astroid.Name, new_if_not_existing: bool = False
    ) -> SymbolData:

        scope = self._scope_name(node)
        local_symbols = self.symbols[scope]
        name = node.name
        if name not in local_symbols:
            if new_if_not_existing:
                # print("create new name data for", name, "in scope", scope)
                local_symbols[name] = SymbolData(name)
            else:
                raise CompilerError(
                    f"Name '{name}' not found in scope '{scope}'",
                    node,
                )
        return local_symbols[name]

    def add_name(self, node: astroid.FunctionDef | astroid.Name | astroid.AssignName):
        if is_builtin_name(node.name):
            return
        self.get_sym_data(node, new_if_not_existing=True)

    def set_name_read(self, node: astroid.NodeNG):
        if is_builtin_name(node.name):
            return

        if not node._ndata.is_used:
            return

        self.get_sym_data(node).nodes_reading.append(node)

    def set_name_written(self, node):
        if is_builtin_name(node.name):
            raise CompilerError(
                f"Cannot write to built-in name '{node.name}'",
                node,
            )

        if not node._ndata.is_used:
            return

        self.get_sym_data(node).nodes_writing.append(node)


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
    def __init__(self, data: CodeData):
        self.data = data
        self.tree = data.tree

        self._handlers = {
            astroid.Pass: self.handle_pass,
            astroid.Global: self.handle_global,
            astroid.Module: self.handle_module,
            astroid.FunctionDef: self.handle_function_def,
            astroid.Keyword: self.handle_keyword,
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
            astroid.BoolOp: self.handle_binop,
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

    def handle_keyword(self, node: astroid.Keyword):
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
    def handle_node(self, node: astroid.NodeNG):
        if hasattr(node, "_ndata"):
            raise ValueError(
                f"Node {node} already has _ndata set. "
                "This pass should only be run once per node."
            )
        node._ndata = NodeData(node, self.data)


class CompilerPassFindNames(CompilerPass):
    def handle_node(self, node: astroid.NodeNG):
        if isinstance(node, (astroid.FunctionDef, astroid.Name, astroid.AssignName)):
            self.data.add_name(node)


class CompilerPassCheckConstValue(CompilerPass):
    def handle_module(self, node: astroid.NodeNG):
        pass

    def handle_node(self, node: astroid.NodeNG):
        data = node._ndata
        if node.parent._ndata.is_constant_value:
            # print('node parent is constant', type(node).__name__, type(node.parent).__name__)
            # data.is_constant_value = True
            return
        is_const, value = is_constant(node)

        data.is_constant_value = is_const

        if is_const:
            # print("is constant", node, value)
            node._ndata.constant_value = value
            node._ndata.result = value

    def run(self):
        super().run()
        for scope, symbols in self.data.symbols.items():
            for name, symbol_data in symbols.items():
                if (
                    len(symbol_data.nodes_writing) == 1
                    and symbol_data.nodes_writing[0]._ndata.is_constant_value
                ):
                    value = symbol_data.nodes_writing[0]._ndata.constant_value
                    # print("constant name", name, "in scope", scope, "value", value)
                    for node in symbol_data.nodes_reading:
                        data = node._ndata
                        data.is_constant_value = True
                        data.constant_value = value
                        data.result = value
                else:
                    for node in symbol_data.nodes_reading:
                        # print("not constant name", name, "in scope", scope)
                        data = node._ndata
                        data.is_constant = False
                        data.is_constant_value = None
                        data.result = None


class CompilerPassCheckUsed(CompilerPass):
    def __init__(self, tree: astroid.Module):
        super().__init__(tree)
        self._have_unset_nodes = True
        self._throw_on_unset = False

        self._functions = {}

    def handle_node(self, node: astroid.NodeNG):
        data = node._ndata

        if isinstance(node, astroid.FunctionDef):
            self._functions[node.name] = node
            data.is_used = data.is_used or False
            self._have_unset_nodes = True

        if data.is_used is None:
            if self._throw_on_unset:
                raise CompilerError(
                    f"Node has no used flag set: {node}",
                    node,
                )
            self._have_unset_nodes = True
            return

        if isinstance(node, astroid.Call):
            if node.func.name in self._functions:
                func = self._functions[node.func.name]
                func._ndata.is_used = func._ndata.is_used or data.is_used
            elif node.func.name not in symbols.__dict__:
                print(
                    f"Call to undefined function '{node.func.name}' in {node.lineno}:{node.col_offset}"
                )

        for child in node.get_children():
            child._ndata.is_used = data.is_used

        if isinstance(node, (astroid.If, astroid.While)):
            test_data = node.test._ndata
            if test_data.is_constant_value:
                test_data.is_used = False

    def handle_module(self, node: astroid.Module):
        node._ndata.is_used = True

        for child in node.get_children():
            if not isinstance(child, astroid.FunctionDef):
                child._ndata.is_used = True

    def run(self):
        for _ in range(10):
            self._have_unset_nodes = False
            self._visit_node_recursive(self.tree)
            if not self._have_unset_nodes:
                break

        self._throw_on_unset = True
        self._have_unset_nodes = False
        self._visit_node_recursive(self.tree)


class CompilerPassResetReadWritten(CompilerPass):
    def handle_node(self, node: astroid.NodeNG):
        pass

    def handle_assign_name(self, node: astroid.AssignName):
        if not is_builtin_name(node.name):
            sym_data = self.data.get_sym_data(node)
            sym_data.nodes_writing.clear()
            sym_data.nodes_reading.clear()

    def handle_name(self, node: astroid.Name):
        if not is_builtin_name(node.name):
            sym_data = self.data.get_sym_data(node)
            sym_data.nodes_writing.clear()
            sym_data.nodes_reading.clear()

    def run(self):
        # print(f"pass {type(self).__name__} run")
        # print(f"symbols: {self.data.symbols}")
        self._visit_node_recursive(self.tree)


class CompilerPassSetReadWritten(CompilerPassResetReadWritten):
    def handle_assign_name(self, node: astroid.AssignName):
        self.data.set_name_written(node)

    def handle_name(self, node: astroid.Name):
        self.data.set_name_read(node)

    def handle_function_def(self, node: astroid.FunctionDef):
        self.data.set_name_written(node)


class CompilerPassCheckReadWritten(CompilerPassResetReadWritten):
    def handle_assign_name(self, node: astroid.AssignName):
        if node._ndata.is_used and not is_builtin_name(node.name):
            sym_data = self.data.get_sym_data(node)
            if sym_data.is_read == 0:
                print(f"mark unused name '{node.name}' in scope '{sym_data.scope}'")
                node._ndata.is_used = False

    def handle_name(self, node: astroid.Name):
        pass
        # if node._ndata.is_used and not is_builtin_name(node.name):
        #     parent = node.parent
        #     if isinstance(parent, astroid.Call):
        #         self.data.set_function_called(node.name)
        #     else:
        #         self.data.set_name_read(node.scope(), node.name)


class CompilerPassListSymbols(CompilerPass):
    def run(self):
        print("Listing symbols")
        for scope, symbols in self.data.symbols.items():
            print(f"Scope: {scope}")
            for name, symbol_data in symbols.items():
                print(
                    f"  {name}: {symbol_data.is_read} reads, {symbol_data.is_written} writes"
                )


class CompilerPassAssignSymbols(CompilerPass):
    def handle_module(self, node: astroid.FunctionDef):
        self.tree._ndata.symbols[node] = node.locals.copy()

    def handle_function_def(self, node: astroid.FunctionDef):
        self.tree._ndata.symbols[node] = node.locals.copy()

    def handle_node(self, node: astroid.Assign):
        pass
