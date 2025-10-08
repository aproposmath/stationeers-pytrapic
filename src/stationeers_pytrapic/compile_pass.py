import logging
from dataclasses import dataclass, field
from typing import Literal

import astroid

from . import symbols
from .types import IC10Instruction, IC10Register
from .utils import (
    CompilerError,
    get_binop_instruction,
    get_function_name,
    get_function_parent,
    get_scope_name,
    get_unop_instruction,
    is_builtin_name,
    is_constant,
    logger,
)


@dataclass
class FunctionData:
    node: astroid.FunctionDef
    sym_data: IC10Register
    code: list[IC10Instruction] = field(default_factory=list)
    args: list[IC10Register] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self.node.name if self.node else ""

    @property
    def can_inline(self) -> bool:
        return self.node and self.sym_data.is_read == 1

    @property
    def is_called(self) -> bool:
        return self.node is None or self.sym_data.is_read > 0

    @property
    def has_return_value(self) -> bool:
        return self.node and self.node._ndata.func_has_return_value


@dataclass
class CompileOptions:
    original_code_as_comment: bool = False
    generated_comments: bool = False
    inline_functions: bool = True
    remove_labels: bool = False
    append_version: bool = True
    compact: bool = False


@dataclass
class CodeData:
    original_code: list[str]
    tree: astroid.Module
    options: CompileOptions
    symbols: dict[str, dict[str, IC10Register]]
    register_map: dict[str, str]
    functions: dict[str, FunctionData]
    result: dict[str, str | int]
    structures: dict[str, dict[str, object]] = field(default_factory=dict)
    modules: dict[str, astroid.Module] = field(default_factory=dict)

    def __init__(
        self, code: str, tree: astroid.Module, options: CompileOptions, modules=None
    ):
        self.original_code = code.splitlines()
        self.tree = tree
        self.options = options
        self.symbols = {"": {}}
        self.register_map = None
        self.functions = {}
        self.result = {"code": "No code generated"}
        self.structures = {}
        self.modules = modules if modules is not None else {}

    def get_tmp_sym_data(self, node: astroid.NodeNG, name: str) -> IC10Register:
        scope = get_scope_name(node)
        if scope not in self.symbols:
            self.symbols[scope] = {}
        local_symbols = self.symbols[scope]
        local_symbols[name] = IC10Register(name)
        return local_symbols[name]

    def get_sym_data(
        self, node: astroid.AssignName | astroid.Name, new_if_not_existing: bool = False
    ) -> IC10Register:

        name = node.name
        if name in ("ra", "sp"):
            return IC10Register(name, "", name)
        scope = get_scope_name(node)
        if scope not in self.symbols:
            self.symbols[scope] = {}
        local_symbols = self.symbols[scope]
        if name not in local_symbols:
            if new_if_not_existing:
                # print(f"Creating new symbol '{name}' in scope '{scope}'")
                local_symbols[name] = IC10Register(name, scope=scope)
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
        if is_builtin_name(node.name) and node.name not in ("ra", "sp"):
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
    is_constant: bool = None
    constant_value: str | float | None = None
    node: astroid.NodeNG = None
    code_data: CodeData = None
    indent: int = 0
    is_compiled = False
    start_label: str = None
    end_label: str = None

    code: dict[CodeType, list[IC10Instruction]] = None
    result = None

    scope: str = None

    func_has_return_value: bool = False

    def __init__(self, node, code_data):
        self.code_data = code_data
        self.node = node
        self.is_used = None
        self.is_constant = None
        self.constant_value = None

        self.code = {"": [], "end": [], "else": []}

    def set_constant(self, value):
        self.is_constant = True
        self.constant_value = value
        self.result = value

    def _add(self, line: IC10Instruction, code_type: CodeType = ""):
        if not isinstance(line, IC10Instruction):
            raise ValueError("line must be an instance of IC10Instruction")

        line.node = self.node
        line.indent += self.indent

        if code_type not in self.code:
            self.code[code_type] = []

        self.code[code_type].append(line)

    def add(self, line: IC10Instruction):
        self._add(line)

    def add_end(self, line: IC10Instruction):
        self._add(line, code_type="end")

    def add_else(self, line: IC10Instruction):
        self._add(line, code_type="else")

    def __str__(self):
        return f"NodeData(is_used={self.is_used}, is_constant={self.is_constant}, constant_value={self.constant_value})"


class CompilerPass:
    skip_unused_nodes: bool = False

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
            astroid.UnaryOp: self.handle_unop,
            astroid.Arguments: self.handle_arguments,
            astroid.Return: self.handle_return,
            astroid.Continue: self.handle_continue,
            astroid.Break: self.handle_break,
            astroid.AugAssign: self.handle_immediate_op,
            astroid.List: self.handle_node,
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
        if self.skip_unused_nodes and hasattr(node, "_ndata"):
            if node._ndata.is_used is False:
                self._debug("Skipping unused node", node)
                return
        self._visit_node(node)
        for child in node.get_children():
            self._visit_node_recursive(child)

    def _visit_node(self, node: astroid.NodeNG):
        self._debug("_visit_node", node)
        if self.skip_unused_nodes and hasattr(node, "_ndata"):
            if node._ndata.is_used is False:
                self._debug("Skipping unused node", node)
                return

        if type(node) not in self._handlers:
            raise CompilerError(
                f"Unsupported node type '{type(node)}' in compiler pass '{type(self).__name__}'",
                node,
            )
        self._handlers[type(node)](node)

    def run(self):
        self._info("run")
        for module in self.data.modules.values():
            self._visit_node_recursive(module)
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

    def handle_immediate_op(self, node: astroid.AugAssign):
        self.handle_node(node)

    def handle_subscript(self, node: astroid.Subscript):
        self.handle_node(node)

    def handle_if(self, node: astroid.If):
        self.handle_node(node)

    def handle_binop(self, node: astroid.BinOp):
        self.handle_node(node)

    def handle_unop(self, node: astroid.UnaryOp):
        self.handle_node(node)

    def handle_ignore(self, node: astroid.NodeNG):
        pass

    def handle_global(self, node: astroid.Global):
        self.handle_node(node)

    def handle_return(self, node: astroid.Return):
        self.handle_node(node)

    def handle_continue(self, node: astroid.Continue):
        self.handle_node(node)

    def handle_break(self, node: astroid.Break):
        self.handle_node(node)


class CompilerPassSetModuleNames(CompilerPass):
    def handle_node(self, node: astroid.NodeNG):
        pass

    def handle_import_from(self, node: astroid.ImportFrom):
        if node.modname != "library":
            return
        for name, alias in node.names:
            new_name = alias if alias else name
            module = self.data.modules[name]
            module.name = new_name
            self._renamed_modules[new_name] = module

    def run(self):
        self._renamed_modules = {}
        self._info("run")
        for module in self.data.modules.values():
            self._visit_node_recursive(module)
        self._visit_node_recursive(self.tree)
        self.data.modules = self._renamed_modules


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


class CompilerPassBoolOpToBinOp(CompilerPass):
    def handle_node(self, node: astroid.NodeNG):
        pass

    def handle_binop(self, node: astroid.BinOp):
        def make_node_from_rest(
            parent_node: astroid.BoolOp, other: tuple[astroid.NodeNG]
        ):
            node = astroid.BinOp(
                parent_node.op,
                parent_node.lineno,
                parent_node.col_offset,
                parent_node,
                end_col_offset=parent_node.end_col_offset,
                end_lineno=parent_node.end_lineno,
            )
            if len(other) == 2:
                node.postinit(other[0], other[1])
            else:
                node.postinit(other[0], make_node_from_rest(node, other[1:]))
            return node

        children = tuple(node.get_children())
        for child in children:
            self._visit_node(child)
        if not isinstance(node, astroid.BoolOp):
            return
        if len(children) <= 2:
            return
        node.values = [children[0], make_node_from_rest(node, children[1:])]


class CompilerPassCheckConstValue(CompilerPass):
    def handle_module(self, node: astroid.NodeNG):
        for child in node.get_children():
            self._visit_node(child)

    def handle_compare(self, node: astroid.Compare):
        left = node.left
        right = node.ops[0][1]
        self._visit_node(left)
        self._visit_node(right)
        op = node.ops[0][0]

        if left._ndata.is_constant and right._ndata.is_constant:
            _, func = get_binop_instruction(op)
            val = func(left._ndata.constant_value, right._ndata.constant_value)
            node._ndata.set_constant(val)

    def handle_binop(self, node: astroid.BinOp):
        data = node._ndata

        if data.is_constant:
            return

        left, right = node.get_children()
        self._visit_node(left)
        self._visit_node(right)

        if left._ndata.is_constant and right._ndata.is_constant:
            _, func = get_binop_instruction(node.op)
            val = func(left._ndata.constant_value, right._ndata.constant_value)
            data.set_constant(val)
            # self._visit_node(node.parent)
        else:
            data.is_constant = False

    def handle_unop(self, node: astroid.UnaryOp):
        data = node._ndata
        if data.is_constant:
            return
        self._visit_node(node.operand)
        if node.operand._ndata.is_constant:
            _, func = get_unop_instruction(node.op)
            node._ndata.set_constant(func(node.operand._ndata.constant_value))
            # self._visit_node(node.parent)

    def handle_name(self, node: astroid.Name):
        if node.name == "__name__":
            scope_name = get_scope_name(node)
            mod_name = scope_name.split(".")[0]
            if mod_name == "":
                mod_name = "__main__"
            node._ndata.set_constant(mod_name)
        else:
            self.handle_node(node)

    def handle_node(self, node: astroid.NodeNG):
        data = node._ndata

        if data.is_constant:
            return

        if node.parent._ndata.is_constant:
            return

        for child in node.get_children():
            self._visit_node(child)

        is_const, value = is_constant(node)

        update_parent = data.is_constant == False and is_const
        if is_const:
            data.set_constant(value)

        if update_parent:
            self._visit_node(node.parent)

    def run(self):
        self._info("run")
        for module in self.data.modules.values():
            self._visit_node(module)
        self._visit_node(self.tree)


class CompilerPassCheckConstValueAssign(CompilerPassCheckConstValue):
    skip_unused_nodes = True

    def handle_assign(self, node: astroid.Assign):
        for child in node.get_children():
            self._visit_node(child)
        if node.value._ndata.is_constant:
            value = node.value._ndata.constant_value
            target = node.targets[0]
            if isinstance(target, astroid.AssignName):
                sym = self.data.get_sym_data(target)
                if not sym.is_overwritten:
                    for read_node in sym.nodes_reading:
                        read_node._ndata.set_constant(value)

    def run(self):
        self._info("run")
        for module in self.data.modules.values():
            self._visit_node_recursive(module)
        self._visit_node_recursive(self.tree)


class CompilerPassCheckUsed(CompilerPass):
    def __init__(self, tree: astroid.Module):
        super().__init__(tree)
        self._have_unset_nodes = True
        self._throw_on_unset = False

        self._functions = {}

    def handle_node(self, node: astroid.NodeNG):
        data = node._ndata

        if isinstance(node, astroid.FunctionDef):
            fname = get_function_name(node)
            if fname in self._functions and self._functions[fname] != node:
                raise CompilerError(
                    f"Function '{fname}' already defined",
                    node,
                )
            self._functions[fname] = node
            data.is_used = data.is_used or False
            self._have_unset_nodes = True

        if isinstance(node, (astroid.If, astroid.While)):
            test_data = node.test._ndata
            if data.is_used is None:
                data.is_used = True
            test_data.is_used = data.is_used
            if test_data.is_constant and not test_data.constant_value:
                use_if = bool(test_data.constant_value)
                for child in node.body:
                    child._ndata.is_used = use_if and data.is_used
                for child in node.orelse:
                    child._ndata.is_used = not use_if and data.is_used
                return

        if data.is_used is None:
            if self._throw_on_unset:
                raise CompilerError(
                    f"Node has no used flag set: {node}",
                    node,
                )
            self._have_unset_nodes = True
            return

        if isinstance(node, astroid.Call):
            fname = get_function_name(node.func)
            if isinstance(node.func, (astroid.Attribute, astroid.Name)):
                if fname in self._functions:
                    func = self._functions[fname]
                    func._ndata.is_used = func._ndata.is_used or data.is_used
                elif fname not in symbols.__dict__:
                    raise CompilerError(
                        f"Calling undefined function {fname}",
                        node,
                    )
            else:
                raise CompilerError(
                    f"Unsupported function call type: {type(node.func)}",
                    node,
                )

        for child in node.get_children():
            child._ndata.is_used = data.is_used

    def handle_module(self, node: astroid.Module):
        node._ndata.is_used = True

        for child in node.get_children():
            if not isinstance(child, (astroid.FunctionDef, astroid.If)):
                child._ndata.is_used = True

    def run(self):
        for _ in range(10):
            self._have_unset_nodes = False
            for module in self.data.modules.values():
                self._visit_node_recursive(module)
            self._visit_node_recursive(self.tree)
            if not self._have_unset_nodes:
                break

        self._throw_on_unset = True
        self._have_unset_nodes = False
        for module in self.data.modules.values():
            self._visit_node_recursive(module)
        self._visit_node_recursive(self.tree)


class CompilerPassResetReadWritten(CompilerPass):
    skip_unused_nodes = True

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
        for module in self.data.modules.values():
            self._visit_node_recursive(module)
        self._visit_node_recursive(self.tree)


class CompilerPassSetReadWritten(CompilerPassResetReadWritten):
    def handle_assign_name(self, node: astroid.AssignName):
        self.data.set_name_written(node)

    def handle_name(self, node: astroid.Name):
        self.data.set_name_read(node)

    def handle_function_def(self, node: astroid.FunctionDef):
        self.data.set_name_written(node)

    def handle_attribute(self, node: astroid.Attribute):
        # scope = get_scope_name(node) #.expr.as_string()
        scope = (
            node.expr.name
            if isinstance(node.expr, astroid.Name)
            else get_scope_name(node.expr)
        )
        if scope in self.data.modules:
            module_locals = self.data.modules[scope].locals
            if node.attrname not in module_locals:
                raise CompilerError(
                    f"Module '{scope}' has no attribute '{node.attrname}'",
                    node,
                )
            obj = module_locals[node.attrname][0]
            obj._ndata.is_used = True
            sym = self.data.get_sym_data(obj)
            sym.nodes_reading.append(node)


class CompilerPassCheckReadWritten(CompilerPassResetReadWritten):
    def handle_assign_name(self, node: astroid.AssignName):
        if node._ndata.is_used and not is_builtin_name(node.name):
            sym_data = self.data.get_sym_data(node)
            if sym_data.is_read == 0:
                # print(f"mark unused name '{node.name}' in scope '{sym_data.scope}'")
                node._ndata.is_used = False

    def handle_name(self, node: astroid.Name):
        pass
        # if node._ndata.is_used and not is_builtin_name(node.name):
        #     parent = node.parent
        #     if isinstance(parent, astroid.Call):
        #         self.data.set_function_called(node.name)
        #     else:
        #         self.data.set_name_read(node.scope(), node.name)


class CompilerPassCheckReturnValues(CompilerPass):
    def handle_return(self, node: astroid.Return):
        if not node._ndata.is_used:
            return

        if node.value is None:
            return

        function_node = get_function_parent(node)
        function_node._ndata.func_has_return_value = True

    def handle_node(self, node: astroid.NodeNG):
        pass


class CompilerPassCreateFunctionData(CompilerPass):

    def handle_function_def(self, node: astroid.FunctionDef):
        sym_data = self.data.get_sym_data(node)
        name = get_function_name(node)
        self.data.functions[name] = FunctionData(node, sym_data)

    def handle_node(self, node: astroid.NodeNG):
        pass
