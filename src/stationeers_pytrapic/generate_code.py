import re
from contextlib import contextmanager

import astroid

from . import _version, intrinsics, structures_generated, symbols, types
from .compile_pass import (
    CodeData,
    CodeLine,
    CompilerError,
    CompilerPass,
    FunctionData,
    SymbolData,
)
from .utils import (
    get_function_parent,
    is_builtin_name,
    is_constant,
    logger,
    get_binop_instruction,
    is_builtin_function,
    is_builtin_structure,
)

# use stack addresses 511 for function return values
# and 510, 509, ... for function arguments
_RETURN_VALUE_ADDRESS = 511


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


def remove_unused_labels(code: str) -> str:
    lines = code.splitlines()

    labels = set()
    used_labels = set()

    for line in lines:
        tokens = line.split()
        if len(tokens) == 1 and tokens[0].endswith(":"):
            labels.add(tokens[0][:-1])

    for line in lines:
        tokens = line.split()
        for label in labels:
            if label in tokens:
                used_labels.add(label)

    unused_labels = labels - used_labels

    result = []
    for line in lines:
        if line.endswith(":") and line[:-1] in unused_labels:
            continue
        result.append(line)

    return "\n".join(result)


class CompilerPassGenerateCode(CompilerPass):
    skip_unused_nodes = True

    def __init__(self, data: CodeData):
        super().__init__(data)
        logger.info("Initializing CompilerPassGenerateCode")
        self._name_counter = 0
        self._symbol_counter = 0

        self._names = {}

        self.ignore_nodes(astroid.ImportFrom, astroid.Import, astroid.Pass)
        self.functions = {}

    def set_name_(
        self, node: astroid.NodeNG, symbol: SymbolData, identifyer: str | None = None
    ):
        logger.info("set name %s %s %s", node, symbol, identifyer)
        if identifyer is not None:
            scope_name = node.scope().name
            key = (scope_name, identifyer)
            if key in self._names:
                self._names[key].is_written += 1
                # raise CompilerError(
                #     f"Name {identifyer} already exists in scope {scope_name}", node
                # )
            else:
                self._names[key] = symbol
        else:
            self._names[node] = symbol

    def get_constant_name(self) -> str:
        name = f"c.{self._name_counter}"
        self._name_counter += 1
        return name

    def get_intermediate_symbol(self, node) -> str:
        reg = self.get_register_name()
        sym = self.data.get_tmp_sym_data(node, reg)
        sym.code_expr = reg
        sym.nodes_writing.append(node)
        return sym

    def get_register_name(self) -> str:
        name = f"__register.{self._name_counter}_"
        self._name_counter += 1
        return name

    def get_name(self, node: astroid.NodeNG, identifyer: str | None = None) -> str:
        return self.data.get_sym_data(node)

        logger.debug("get name %s %s", node, identifyer)
        scope_name = node.scope().name
        symbol_id = self._symbol_counter
        self._symbol_counter += 1
        if identifyer is None:
            if node not in self._names:
                identifyer = f"tmp_{self._name_counter}"
                self._names[node] = SymbolData(
                    symbol_id, scope_name, str(self._name_counter)
                )
                self._name_counter += 1
            logger.debug("return name", self._names[node])
            return self._names[node]
        else:
            if scope_name:
                if identifyer not in node.scope().locals:
                    scope_name = ""
            key = (scope_name, identifyer)
            if key not in self._names:
                # self._name_counter += 1
                self._names[key] = SymbolData(symbol_id, scope_name, identifyer)
                # self._names[key] = types.Register(f"_{scope_name}_{identifyer}")
            # print("\treturn name", self._names[key])
            return self._names[key]

    def get_label(
        self, prefix: str = "tmp", prefix2: str | None = None
    ) -> str | tuple[str, str]:
        self._name_counter += 1
        name = f"lb{prefix}{self._name_counter}"
        if prefix2 is not None:
            name2 = f"lb{prefix2}{self._name_counter}"
            return name, name2
        return name

    def compile_node(self, node: astroid.NodeNG):
        if not node._ndata.is_compiled:
            self._visit_node(node)
            node._ndata.is_compiled = True
        res = node._ndata.result
        if isinstance(res, SymbolData):
            return res.code_expr
        return res

    def handle_not_implemented(self, node: astroid.NodeNG):
        comment = f"not implemented: {type(node).__name__} at line {node.lineno}"
        node._ndata.add("", comment)

    def handle_module(self, node: astroid.Module):
        for stmt in node.body:
            self._visit_node(stmt)

    def handle_arguments(self, node: astroid.Arguments):
        pass

    def handle_global(self, node: astroid.Global):
        pass  # nothing todo, astroid is correctly handling the scope() of variables declared global

    def handle_attribute(self, node: astroid.Attribute):
        expr = self.compile_node(node.expr)
        attrname = node.attrname
        data = node._ndata

        if not hasattr(expr, node.attrname):
            expr = (
                str(expr) if isinstance(expr, (str, int, float, bool)) else type(expr)
            )
            raise CompilerError(f"Invalid attribute {node.attrname}", node)
        attr = getattr(expr, attrname)
        if isinstance(expr, type) and issubclass(expr, types._BaseStructure):
            name = expr.__name__
            raise CompilerError(
                f"""Cannot use "{name}"" directly, either use "{name}s" to read from all devices of this type or create a specific device with "{name}(d0)".""",
                node,
            )

        if attrname in ["Minimum", "Maximum", "Sum", "Average"]:
            symbol = self.get_intermediate_symbol(node)
            data.add(attr(symbol.code_expr), attrname)
            data.result = symbol
        elif isinstance(attr, symbols._DeviceLogicType):
            symbol = self.get_intermediate_symbol(node)
            data.add(attr._load(symbol.code_expr), attrname)
            data.result = symbol
        else:
            data.result = attr

    def handle_call(self, node: astroid.Call):
        data = node._ndata

        fname = node.func.name

        if node.kwargs:
            raise CompilerError("**kwargs are not supported", node)

        if is_builtin_name(fname):
            func = getattr(symbols, fname)
            kwargs = {kw.arg: self.compile_node(kw.value) for kw in node.keywords}
            args = [self.compile_node(arg) for arg in node.args]

            result = func(*args, **kwargs)
            if is_builtin_structure(result):
                data.result = result
            elif is_builtin_function(fname) or hasattr(types, fname):
                data.result = result
            else:
                data.add(result, "intrinsic called")
            return

        if fname not in self.functions:
            raise CompilerError(f"Function {fname} is not defined.", node)

        func_node = self.functions[fname]
        func_data = self.data.functions[fname]

        do_inline = self.data.options.inline_functions and func_data.can_inline

        for i, arg in enumerate(node.args):
            d = self.compile_node(arg)
            if is_builtin_structure(d):
                raise CompilerError(
                    f"Structures as function arguments are not yet supported: {d}",
                    arg,
                )
            if not do_inline:
                data.add(
                    f"put db {_RETURN_VALUE_ADDRESS-1-i} {d}", f"load argument {i}"
                )

        data.add(f"jal {fname.replace('_','.')}", f"call {fname}")
        self.compile_function(self.functions[fname])

        do_inline = self.data.options.inline_functions and func_data.can_inline

        if func_node._ndata.func_has_return_value:
            if do_inline:
                data.result = func_data.sym_data.code_expr
            else:
                if (
                    isinstance(node.parent, astroid.Assign)
                    and isinstance(node.parent.targets[0], astroid.AssignName)
                    and node.parent.value is node
                ):
                    symbol = self.data.get_sym_data(node.parent.targets[0])
                    data.result = symbol
                    node.parent._ndata.result = symbol
                    if not symbol.code_expr:
                        # target has no register assigned yet
                        symbol.code_expr = self.get_register_name()
                else:
                    symbol = self.get_intermediate_symbol(node)
                data.add_end(
                    f"get {symbol.code_expr} db {_RETURN_VALUE_ADDRESS}",
                    "get return value",
                )
                data.result = symbol

    def handle_expr(self, node: astroid.Expr):
        self._visit_node(node.value)

    def handle_return(self, node: astroid.Return):
        func_node = get_function_parent(node)
        func_data = self.data.functions[func_node.name]

        do_inline = self.data.options.inline_functions and func_data.can_inline

        data = node._ndata
        if node.value is not None:
            d = self.compile_node(node.value)
            if do_inline:
                # todo: check if there are multiple return statements
                # if not, we can avoid this move instruction
                sym_data = self.data.get_sym_data(func_node)
                data.add(f"move {sym_data.code_expr} {d}", "store return value")
            else:
                data.add(f"put db {_RETURN_VALUE_ADDRESS} {d}", "store return value")

        if node != func_node.body[-1]:
            # only jump to end of function, if return is not the last statement
            label = func_node.name.replace("_", ".") + "end"
            data.add(f"j {label}", "return from function", -1)

    def handle_continue(self, node: astroid.Continue):
        while not isinstance(node.parent, (astroid.While, astroid.For)):
            node = node.parent
        start_label = node.parent._ndata.start_label
        node._ndata.add(f"j {start_label}", "continue loop")

    def handle_break(self, node: astroid.Break):
        while not isinstance(node.parent, (astroid.While, astroid.For)):
            node = node.parent
        end_label = node.parent._ndata.end_label
        node._ndata.add(f"j {end_label}", "break loop")

    def handle_name(self, node: astroid.Name):
        # todo: detect if name is in locals/globals
        # throw proper error if not
        name = node.name
        if node._ndata.result:
            return node._ndata.result
        if name in symbols.__dict__:
            node._ndata.result = symbols.__dict__[name]
        elif name in structures_generated.__dict__:
            node._ndata.result = structures_generated.__dict__[name]
        elif name in intrinsics.__dict__:
            node._ndata.result = intrinsics.__dict__[name]
        elif name in types.__dict__:
            node._ndata.result = types.__dict__[name]
        else:
            sym_data = self.data.get_sym_data(node)
            node._ndata.result = sym_data.code_expr

    def handle_const(self, node: astroid.Const):
        data = node._ndata
        if isinstance(node.value, bool):
            data.result = int(node.value)
        elif isinstance(node.value, (int, float)):
            data.result = node.value
        elif isinstance(node.value, str):
            data.result = f'"{node.value}"'
        elif isinstance(node.value, type(None)):
            data.result = ""
        else:
            raise CompilerError(f"Unsupported constant type: {type(node.value)}", node)

    def handle_function_def(self, node: astroid.FunctionDef):
        self.functions[node.name] = node

    def compile_function(self, node: astroid.FunctionDef):
        data = node._ndata
        if data.code[""]:
            # function already compiled
            return
        sym_data = self.data.get_sym_data(node)
        label = node.name.replace("_", ".")
        data.add(f"{label}:", "function definition")
        data.add_end(f"{label}end:", "function end label")

        func_data = self.data.functions[node.name]

        if self.data.options.inline_functions and func_data.can_inline:
            ret_value = self.get_register_name() if func_data.has_return_value else ""
            sym_data.code_expr = ret_value
            calling_node = sym_data.nodes_reading[0].parent
            for i, arg in enumerate(node.args.args):
                arg_sym = self.data.get_sym_data(arg)
                calling_arg = calling_node.args[i]._ndata.result
                if isinstance(calling_arg, SymbolData):
                    calling_arg = calling_arg.code_expr
                if arg_sym.is_overwritten:
                    # need to copy argument to a register, as it is overwritten in the function
                    reg = self.get_register_name()
                    data.add(f"move {reg} {calling_arg}", "copy function argument")
                    arg_sym.code_expr = reg
                else:
                    arg_sym.code_expr = calling_arg
                func_data.args.append(arg_sym)
        else:
            for i, arg in enumerate(node.args.args):
                reg = self.get_register_name()
                sym = self.data.get_sym_data(arg)
                sym.code_expr = reg
                data.add(
                    f"get {sym.code_expr} db {_RETURN_VALUE_ADDRESS-1-i}",
                    f"load argument {arg.name}",
                    1,
                )
                if arg.name in symbols.__dict__:
                    raise CompilerError(
                        f"Function argument name {arg.name} conflicts with a built-in name",
                        arg,
                    )
                sym.nodes_writing.append(arg)
                arg._ndata.result = sym
                func_data.args.append(sym)

        if sym_data.is_read != 1 or not self.data.options.inline_functions:
            data.add_end("j ra", "return from function", 1)

        for stmt in node.body:
            self._visit_node(stmt)

    def handle_assign_name(self, node: astroid.AssignName):
        data = node._ndata
        sym = self.data.get_sym_data(node.targets[0])
        node.targets[0]._ndata.result = sym
        data.result = sym
        # list(node.get_children())[0]._ndata.result = sym

    def handle_assign(self, node: astroid.Assign):
        target = node.targets[0]
        # print("assign", target, node.value)
        data = node._ndata

        if data.is_compiled:
            return

        data.is_compiled = True

        # TODO: use define instead of move for constants

        if len(node.targets) != 1:
            raise NotImplementedError("Multiple assignment targets are not supported")

        elif isinstance(target, astroid.AssignName):
            value = self.compile_node(node.value)
            value_name = value.__name__ if isinstance(value, type) else value
            if isinstance(value, SymbolData):
                # raise CompilerError(
                #     f"Cannot assign symbol {value.name} to name {target.name}", target
                # )
                value.code_expr = target.name
                # data.result = value
                # # assign new name to symbol instead of extra move instruction
                # value.name = target.name
                # self.set_name(target, value, target.name)
            elif value_name in symbols.__dict__ or is_builtin_structure(value):
                data.result = value
                sym_data = self.data.get_sym_data(target)
                if sym_data.code_expr and sym_data.code_expr != value:
                    other_line = ""
                    for n in sym_data.nodes_writing:
                        if n is not node:
                            other_line = n.lineno
                            break
                    raise CompilerError(
                        f"Cannot reassign assign {value_name} to {target.name}, already assigned to {sym_data.code_expr} at line {other_line}",
                        target,
                    )
                sym_data.code_expr = value
                # self.set_name(target, value, target.name)
            else:
                sym_data = self.data.get_sym_data(target)
                can_assign_directly = not sym_data.is_overwritten
                if isinstance(node.value, astroid.Call):
                    can_assign_directly = can_assign_directly and is_builtin_function(
                        node.value.func.name
                    )
                if can_assign_directly:
                    sym_data.code_expr = value  # self.get_constant_name()
                    # sym.name = value
                    # sym.is_constant = True
                    data.result = value
                else:
                    reg = sym_data.code_expr or self.get_register_name()
                    if reg != value:
                        data.add(f"move {reg} {value}", "assign name")
                    sym_data.code_expr = reg
                    data.result = reg
            target._ndata.result = data.result
            target._ndata.is_compiled = True
        elif isinstance(target, astroid.AssignAttr):
            rhs = self.compile_node(list(node.get_children())[1])
            lhs = self.compile_node(target)
            if isinstance(lhs, symbols._DeviceLogicType) and lhs._device_id._id is None:
                name = lhs._cls.__name__
                raise CompilerError(
                    f"""Cannot use "{name}"" directly, either use "{name}s" to set all devices of this type or create a specific device with "{name}(d0)".""",
                    target,
                )

            if isinstance(rhs, symbols._DevicesLogicType):
                raise CompilerError(
                    "You need to take either Minimum/Maximum/Average/Sum", target
                )
            expr = lhs._set(rhs)
            data.add(f"{expr}", "assign attribute")
        else:
            raise CompilerError(f"Unsupported assignment target: {type(target)}")

    def handle_assign_attr(self, node: astroid.AssignAttr):
        expr = self.compile_node(node.expr)
        if not hasattr(expr, node.attrname):
            expr = (
                str(expr) if isinstance(expr, (str, int, float, bool)) else type(expr)
            )
            raise CompilerError(f"Invalid attribute {node.attrname}", node)
        val = getattr(expr, node.attrname)
        if isinstance(val, property):
            val = val.fget(expr)

        node._ndata.result = val

    def handle_subscript(self, node: astroid.Subscript):
        value = self.compile_node(node.value)
        slice_ = self.compile_node(node.slice)
        node._ndata.result = value[slice_]

    def handle_compare(self, node: astroid.Compare):
        sym = self.get_intermediate_symbol(node)
        left = self.compile_node(node.left)
        right = self.compile_node(node.ops[0][1])

        instruction = "s" + get_comparison_suffix(node.ops[0][0])
        data = node._ndata
        data.add(f"{instruction} {sym.code_expr} {left} {right}", "compare")
        data.result = sym

    def handle_ifexp(self, node: astroid.IfExp):
        test = self.compile_node(node.test)
        left = self.compile_node(node.body)
        right = self.compile_node(node.orelse)

        sym = self.get_intermediate_symbol(node)
        data = node._ndata
        data.result = sym
        data.add(f"select {sym.code_expr} {test} {left} {right}", "if expression")

    def handle_if(self, node: astroid.If):
        else_label, end_label = self.get_label("else", "end")

        test = self.compile_node(node.test)

        emit_if = len(node.body) > 0
        emit_else = len(node.orelse) > 0

        data = node._ndata
        test_data = node.test._ndata

        if test_data.is_constant_value:
            if test_data.constant_value:
                emit_else = False
            else:
                emit_if = False
        elif isinstance(node.test, astroid.Compare):
            left = self.compile_node(node.test.left)
            right = self.compile_node(node.test.ops[0][1])
            cmp_op = node.test.ops[0][0]

            instruction = "b" + get_negated_comparison_suffix(cmp_op)
            data.add(f"{instruction} {left} {right} {else_label}", "if with compare")
        elif isinstance(node.test, astroid.Const):
            if node.test.value:
                emit_else = False
            else:
                emit_if = False
        # elif isinstance(node.test, astroid.Attribute):
        #     data.add(f"bne {test} {else_label}", "if with attribute")
        elif isinstance(node.test, astroid.BoolOp):
            test = self.compile_node(node.test)
            data.add(f"beqz {test} {else_label}", "if with bool op")
        elif isinstance(node.test, astroid.Name):
            test_name = self.compile_node(node.test)
            if isinstance(test_name, SymbolData):
                test_name = test_name.code_expr
            data.add(f"beqz {test_name} {else_label}", "if with name")
        else:
            raise NotImplementedError(f"Unsupported if test: {type(node.test)}")

        for stmt in node.body:
            if emit_if:
                self._visit_node(stmt)
            else:
                stmt._ndata.is_used = False

        if emit_if:
            if emit_else:
                data.add_else(f"j {end_label}", "jump to end of if")
            data.add_else(f"{else_label}:", "", -1)

        for stmt in node.orelse:
            if emit_else:
                self._visit_node(stmt)
            else:
                stmt._ndata.is_used = False

        data.add_end(f"{end_label}:", "", -1)

    def handle_unop(self, node: astroid.UnaryOp):
        data = node._ndata

        if data.is_constant_value:
            data.result = data.constant_value
            return

        if node.op not in ["not", "-"]:
            raise CompilerError(f"Unsupported unary operation: {node.op}", node)

        opname = self.compile_node(node.operand)

        sym = self.get_intermediate_symbol(node)
        data.result = sym
        if node.op == "not":
            data.add(f"seqz {sym.code_expr} {opname}", "unary not")
        else:
            data.add(f"sub {sym.code_expr} 0 {opname}", "unary negation")

    def handle_immediate_op(self, node: astroid.AugAssign):
        if node.op[-1] != "=":
            raise CompilerError(f"Unsupported immediate operation: {node.op}", node)
        op = node.op[:-1]
        instruction = get_binop_instruction(op)[0]
        sym = self.data.get_sym_data(node.target)
        left_name = sym.code_expr
        right_name = self.compile_node(node.value)
        data = node._ndata
        data.result = sym
        data.add_end(
            f"{instruction} {left_name} {left_name} {right_name}",
            "binary operation",
        )

    def handle_binop(self, node: astroid.BinOp):
        data = node._ndata

        if data.is_constant_value:
            data.result = data.constant_value
            return

        left, right = node.get_children()
        left_name = self.compile_node(left)
        right_name = self.compile_node(right)
        op = node.op
        instruction, func = get_binop_instruction(op)
        if instruction is None:
            raise CompilerError(f"Unsupported binary operation: {op}", node)

        if isinstance(left, astroid.Const) and isinstance(right, astroid.Const):
            data.result = func(left.value, right.value)
        else:
            sym = self.get_intermediate_symbol(node)
            data.result = sym
            data.add_end(
                f"{instruction} {sym.code_expr} {left_name} {right_name}",
                "binary operation",
            )

    def handle_while(self, node: astroid.While):
        test = node.test
        while_label, end_label = self.get_label("while", "while.end")
        data = node._ndata

        data.start_label = while_label
        data.end_label = end_label

        data.add(f"{while_label}:", "while loop start")
        if isinstance(test, astroid.Compare):
            left = self.compile_node(test.left)
            cmp_op, right_node = test.ops[0]
            right = self.compile_node(right_node)

            instruction = "b" + get_negated_comparison_suffix(cmp_op)
            data.add(f"{instruction} {left} {right} {end_label}", "while with compare")
        elif isinstance(test, astroid.Const):
            if not test.value:
                return
        else:
            raise CompilerError(f"Unsupported while test: {type(test)}", node)

        for stmt in node.body:
            self.compile_node(stmt)

        data.add_end(f"j {while_label}", "jump to loop start", 1)
        data.add_end(f"{end_label}:", "while loop end")

    def run(self):
        self._visit_node(self.tree)


class CompilerPassGatherCode(CompilerPass):
    def __init__(self, data: CodeData):
        super().__init__(data)
        self.code = []
        self._indent_level = 0

        self._target = None

        # for scope, data in self.data.symbols.items():
        #     print(f"Symbols in scope '{scope}'")
        #     for name, d in data.items():
        #         print(f"\t{name} {d.is_read} {d.is_written}")

    def add_line(self, line: CodeLine):
        line.indent += self._indent_level
        self._target.code.append(line)

    @contextmanager
    def indent(self, num_indents=1):
        if isinstance(num_indents, bool):
            num_indents = 1 if num_indents else 0

        self._indent_level += num_indents
        yield
        self._indent_level -= num_indents

    def gather_code(self, node: astroid.NodeNG, special_nodes=None):
        data = node._ndata
        special_nodes = special_nodes or []

        if "" in data.code:
            for line in data.code[""]:
                self.add_line(line)

        do_indent = isinstance(
            node, (astroid.FunctionDef, astroid.While, astroid.For, astroid.If)
        )

        with self.indent(do_indent):
            for child in node.get_children():
                if child not in special_nodes:
                    self._visit_node(child)

            for line in data.code.get("else", []):
                self.add_line(line)

            if isinstance(node, astroid.If):
                for child in node.orelse:
                    self._visit_node(child)
            if isinstance(node, astroid.IfExp):
                self._visit_node(node.orelse)

        for line in data.code.get("end", []):
            self.add_line(line)

    def handle_node(self, node: astroid.NodeNG):
        if not hasattr(node, "_ndata"):
            return
        data = node._ndata
        if not data.is_used:
            return

        old_target = self._target

        if isinstance(node, astroid.FunctionDef):
            self._target = self.data.functions[node.name]

        if isinstance(node, astroid.Call):
            fname = node.func.name
            if not is_builtin_name(fname):
                if fname not in self.data.functions:
                    raise CompilerError(
                        f"Function {node.func.name} is not defined.", node
                    )

                func = self.data.functions[fname]
                if self.data.options.inline_functions and func.can_inline:
                    node._ndata.code[""] = [
                        l for l in node._ndata.code[""] if not l.code.startswith("jal ")
                    ]
                    node._ndata.code[""] += func.code
                    func.code = []

        if isinstance(data.code, str):
            data.code = [data.code]

        if isinstance(node, astroid.While):
            if data.code[""][0].code.endswith(":"):
                # emit while loop start label explicitly now, before any comparison is generated
                self.add_line(data.code[""][0])
                data.code[""] = data.code[""][1:]

        special_nodes = set()
        if hasattr(node, "test"):
            special_nodes.add(node.test)
            self._visit_node(node.test)

        if isinstance(node, astroid.Assign):
            special_nodes.add(node.value)
            self._visit_node(node.value)

        if isinstance(node, astroid.BinOp):
            for child in node.get_children():
                special_nodes.add(child)
                self._visit_node(child)

        if isinstance(node, astroid.If):
            for child in node.orelse:
                special_nodes.add(child)

        if isinstance(node, astroid.Compare):
            special_nodes.add(node.left)
            self._visit_node(node.left)
            for _, right in node.ops:
                special_nodes.add(right)
                self._visit_node(right)
            if (
                isinstance(node.parent, (astroid.If, astroid.While))
                and node == node.parent.test
            ):
                # no need to calculate comparison result, it's done by the branch instruction of the parent
                data.code[""] = []

        if isinstance(node, astroid.Call):
            for arg in node.args:
                special_nodes.add(arg)
                self._visit_node(arg)

        if isinstance(node, astroid.Return) and node.value is not None:
            special_nodes.add(node.value)
            self._visit_node(node.value)

        self.gather_code(node, special_nodes)

        self._target = old_target

    def run(self):
        functions = self.data.functions
        self._target = functions[""] = FunctionData(None, None)

        self._visit_node(self.tree)

        for fname in sorted(self.data.functions.keys()):
            func = self.data.functions[fname]
            if fname == "" or func.is_called:
                for line in func.code:
                    self.code.append(line)

        self.assign_registers()

        self.get_code()

    def assign_registers(self):
        # topological sort of function scopes
        called_from = {}

        for fname, func in self.data.functions.items():
            if fname == "":
                called_from[fname] = set()
                continue
            called_from[fname] = set(
                (node.scope().name for node in func.sym_data.nodes_reading)
            )

        all_scopes = set(self.data.functions.keys())

        sorted_scopes = []
        while len(sorted_scopes) < len(all_scopes):
            for scope in all_scopes - set(sorted_scopes):
                if called_from[scope].issubset(set(sorted_scopes)):
                    sorted_scopes.append(scope)
                    break
            else:
                raise RuntimeError("Internal error: cannot sort scopes")

        registers = list(range(16))

        registers_by_scope = {}

        tokens = set(" ".join([line.code.split("#")[0] for line in self.code]).split())

        mapping = {}

        for scope in sorted_scopes:
            if not scope in self.data.symbols:
                continue
            available_registers = set(registers)
            parent_registers = set()
            for calling_scope in called_from[scope]:
                parent_registers = parent_registers.union(
                    registers_by_scope.get(calling_scope, set())
                )
            available_registers = list(
                reversed(sorted(set(registers) - parent_registers))
            )
            used_registers = set()

            for name, symbol in self.data.symbols[scope].items():
                if not symbol.code_expr in tokens:
                    continue

                if symbol.is_register and symbol.code_expr not in mapping:
                    if not available_registers:
                        raise CompilerError(
                            f"Running out of registers, try to simplify your code."
                        )
                    reg_num = available_registers.pop()
                    used_registers.add(reg_num)
                    mapping[symbol.code_expr] = f"r{reg_num}"
                    # print("assign name", symbol.code_expr, "to", mapping[symbol.code_expr])

            registers_by_scope[scope] = used_registers.union(parent_registers)

        if mapping:
            pattern = re.compile("|".join(re.escape(k) for k in mapping))
            replacer = lambda x: mapping[x.group(0)]
            for line in self.code:
                line.code = pattern.sub(replacer, line.code)

        for token in tokens:
            if token.startswith("__register.") and token not in mapping:
                for line in self.code:
                    if token in line.code:
                        raise CompilerError(
                            f"Internal error: register {token} not assigned, node: {line.node}"
                        )
                raise RuntimeError("Internal error: register not assigned: %s" % token)

        self.used_registers = sorted(set(mapping.values()))

    def remove_labels(self, code):

        label_map = {}
        i_line = 0
        new_code = []
        for line in code.splitlines():
            cline = line.split("#")[0].strip()
            if cline.endswith(":"):
                label = cline[:-1]
                label_map[label] = len(new_code)
            else:
                i_line += 1
                new_code.append(line)

        new_code = "\n".join(new_code)

        for label, line_num in label_map.items():
            pattern = r"\b{}\b".format(re.escape(label))
            new_code = re.sub(pattern, str(line_num), new_code)

        return new_code

    def strip_code(self, code: str) -> str:
        return "\n".join([line.strip() for line in code.splitlines()])

    def get_code(
        self,
    ):
        s = ""

        shift = 2
        code_width = 0

        for line in self.code:
            line.code = " " * (line.indent * shift) + line.code
            code_width = max(code_width, len(line.code))

        just_width = min(60, code_width + 4)

        options = self.data.options
        original_code = self.data.original_code

        prev_comment = None
        for line in self.code:
            c = line.code
            if line.code.endswith(":"):
                # labels are not allowed to have indentation
                c = c.strip()

            if options.original_code_as_comment and line.node:
                ori_line = original_code[line.node.lineno - 1]
                if prev_comment != ori_line:
                    c = c.ljust(just_width)
                    c += f" # {ori_line}"
                    prev_comment = ori_line

            if options.generated_comments and line.comment:
                if prev_comment != line.comment:
                    c = c.ljust(just_width) + " # " + line.comment
                    prev_comment = line.comment

            s += c + "\n"

        s = s[:-1]  # remove last newline

        # logger.info("Number of used registers: %i", len(self._symbols))

        # if len(self._symbols) > 16:
        #     raise CompilerError("Running out of registers.")

        if options.remove_labels:
            s = self.remove_labels(s)
            s = self.strip_code(s)
        else:
            s = remove_unused_labels(s)

        if options.append_version:
            lines = s.splitlines()
            version_string = f" # Generated by PyTrapIC v{_version.__version__}"
            l = len(version_string)
            for i in range(len(lines)):
                if len(lines[i]) + l < 89:
                    lines[i] += version_string
                    break
            s = "\n".join(lines)

        num_lines = len(s.splitlines())
        num_registers = len(self.used_registers)
        num_bytes = len(s) + num_lines - 1

        self.data.result = {
            "code": s,
            "num_lines": num_lines,
            "num_registers": num_registers,
            "num_bytes": num_bytes,
        }
