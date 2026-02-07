import re
from contextlib import contextmanager

from astroid import nodes

from . import _version, intrinsics, structures_generated, symbols, types
from .compile_pass import CodeData, CompilerError, CompilerPass, FunctionData
from .types import IC10, IC10Instruction, IC10Operand, IC10Register
from .types_generated import LogicBatchMethod
from .utils import (
    get_comparison_suffix,
    get_negated_comparison_suffix,
    get_unop_instruction,
    get_scope_name,
    get_binop_instruction,
    get_function_parent,
    is_builtin_function,
    is_builtin_name,
    is_builtin_structure,
    is_loadable_type,
    is_math_function,
    logger,
    get_function_name,
    eval_constexpr,
)

from .register_assignment import assign_registers

# use stack addresses 511 for function return values
# and 510, 509, ... for function arguments
_RETURN_VALUE_ADDRESS = 511

_HAS_RELATIVE_INSTRUCTION = set(
    [
        "j",
        "bap",
        "bapz",
        "bdns",
        "bdse",
        "beq",
        "beqz",
        "bge",
        "bgez",
        "bgt",
        "bgtz",
        "ble",
        "blez",
        "blt",
        "bltz",
        "bna",
        "bnan",
        "bnaz",
        "bne",
        "bnez",
    ]
)


def is_branch(op: str) -> bool:
    return op.startswith("b") or op in ["j", "jal"]


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

        self.ignore_nodes(nodes.ImportFrom, nodes.Import, nodes.Pass)
        self.functions = {}

    def set_name_(
        self, node: nodes.NodeNG, symbol: IC10Register, identifyer: str | None = None
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
        if isinstance(node.parent, nodes.Assign):
            target = node.parent.targets[0]
            if isinstance(target, nodes.AssignName):
                sym = self.data.get_sym_data(target)
                if not sym.code_expr:
                    sym.code_expr = self.get_register_name()
                return sym
        reg = self.get_register_name()
        sym = self.data.get_tmp_sym_data(node, reg)
        sym.code_expr = reg
        sym.nodes_writing.append(node)
        sym._is_intermediate = True
        return sym

    def get_register_name(self) -> str:
        name = f"__register.{self._name_counter}_"
        self._name_counter += 1
        return name

    def get_name(self, node: nodes.NodeNG, identifyer: str | None = None) -> str:
        return self.data.get_sym_data(node)

        logger.debug("get name %s %s", node, identifyer)
        scope_name = node.scope().name
        symbol_id = self._symbol_counter
        self._symbol_counter += 1
        if identifyer is None:
            if node not in self._names:
                identifyer = f"tmp_{self._name_counter}"
                self._names[node] = IC10Register(
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
                self._names[key] = IC10Register(symbol_id, scope_name, identifyer)
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

    def compile_node(self, node: nodes.NodeNG):
        if not node._ndata.is_compiled:
            self._visit_node(node)
            node._ndata.is_compiled = True
        return node._ndata.result

    def handle_not_implemented(self, node: nodes.NodeNG):
        comment = f"not implemented: {type(node).__name__} at line {node.lineno}"
        node._ndata.add(IC10("", comment=comment))

    def handle_module(self, node: nodes.Module):
        for stmt in node.body:
            self._visit_node(stmt)

    def handle_arguments(self, node: nodes.Arguments):
        pass

    def handle_global(self, node: nodes.Global):
        pass  # nothing todo, astroid is correctly handling the scope() of variables declared global

    def handle_attribute(self, node: nodes.Attribute):
        expr = self.compile_node(node.expr)
        attrname = node.attrname
        data = node._ndata

        if not hasattr(expr, attrname):
            raise CompilerError(
                f"Invalid attribute {node.attrname} in expression {node.as_string()}",
                node,
            )
        attr = getattr(expr, attrname)
        if isinstance(expr, type) and issubclass(expr, types._BaseStructure):
            name = expr.__name__
            raise CompilerError(
                f"""Cannot use "{name}"" directly, either use "{name}s" to read from all devices of this type or create a specific device with "{name}(d0)".""",
                node,
            )

        is_batch_method = attrname in LogicBatchMethod.__members__

        if is_batch_method and hasattr(attr, "__call__"):
            symbol = self.get_intermediate_symbol(node)
            data.add(attr(symbol))
            data.result = symbol
        elif is_batch_method and hasattr(attr, "_load") and not attr._logic_type:
            data.result = attr
        elif is_loadable_type(attr):
            symbol = self.get_intermediate_symbol(node)
            try:
                data.add(attr._load(symbol))
            except ValueError as e:
                raise CompilerError(f"Error loading attribute {attrname}: {e}", node)
            data.result = symbol
        else:
            data.result = attr

    def handle_call(self, node: nodes.Call):
        data = node._ndata

        fname = get_function_name(node.func)

        if node.kwargs:
            raise CompilerError("**kwargs are not supported", node)

        if is_math_function(fname) and data.is_constant:
            data.result = IC10Operand(data.constant_value)
            return

        if is_builtin_name(fname):
            func = getattr(symbols, fname)
            kwargs = {kw.arg: self.compile_node(kw.value) for kw in node.keywords}
            args = [self.compile_node(arg) for arg in node.args]

            try:
                result = func(*args, **kwargs)
            except TypeError as e:
                raise CompilerError(f"Error calling function {fname}: {e}", node)
            if isinstance(result, IC10Instruction):
                if result.op == "define":
                    name = result.inputs[0].value
                    result.inputs = result.inputs[1:]
                    result.output = IC10Register(name, code_expr=name)
                elif result.output != None:
                    # instruction returns a value, so we need to assign it to a symbol
                    result.output = self.get_intermediate_symbol(node)
                data.add(result)
                data.result = result.output
            elif is_builtin_structure(result):
                data.result = result
            elif is_builtin_function(fname):
                data.result = IC10Register(name="", code_expr=result)
            else:
                data.result = result
            return

        if fname not in self.functions:
            raise CompilerError(f"Function {fname} is not defined.", node)

        func_node = self.functions[fname]
        func_data = self.data.functions[fname]

        if func_data.is_constexpr:
            data.result = IC10Operand(data.constant_value)
            return

        do_inline = self.data.options.inline_functions and func_data.can_inline

        for i, arg in enumerate(node.args):
            d = self.compile_node(arg)
            if is_builtin_structure(d):
                raise CompilerError(
                    f"Structures as function arguments are not yet supported: {d}",
                    arg,
                )
            if not do_inline:
                addr = _RETURN_VALUE_ADDRESS - 1 - i
                data.add(IC10("put", ["db", addr, d]))

        data.add(IC10("jal", [fname.replace("_", ".")]))
        self.compile_function(self.functions[fname])

        do_inline = self.data.options.inline_functions and func_data.can_inline

        if func_node._ndata.func_has_return_value:
            if do_inline:
                data.result = func_data.sym_data
            else:
                if (
                    isinstance(node.parent, nodes.Assign)
                    and isinstance(node.parent.targets[0], nodes.AssignName)
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
                data.add_end(IC10("get", ["db", _RETURN_VALUE_ADDRESS], symbol))
                data.result = symbol

    def handle_expr(self, node: nodes.Expr):
        self._visit_node(node.value)

    def handle_return(self, node: nodes.Return):
        func_node = get_function_parent(node)
        fname = get_function_name(func_node)
        func_data = self.data.functions[fname]

        do_inline = self.data.options.inline_functions and func_data.can_inline

        data = node._ndata
        if node.value is not None:
            d = self.compile_node(node.value)
            if do_inline:
                # todo: check if there are multiple return statements
                # if not, we can avoid this move instruction
                sym_data = self.data.get_sym_data(func_node)
                data.add(IC10("move", [d], sym_data))
            else:
                data.add(IC10("put", ["db", _RETURN_VALUE_ADDRESS, d]))

        if node != func_node.body[-1]:
            # only jump to end of function, if return is not the last statement
            label = fname.replace("_", ".") + "end"
            data.add(IC10("j", [label], indent=-1))

    def handle_continue(self, node: nodes.Continue):
        loop_node = node
        while not isinstance(loop_node, (nodes.While, nodes.For)):
            loop_node = loop_node.parent
        start_label = loop_node._ndata.start_label
        node._ndata.add(IC10("j", [start_label]))

    def handle_break(self, node: nodes.Break):
        while not isinstance(node.parent, (nodes.While, nodes.For)):
            node = node.parent
        end_label = node.parent._ndata.end_label
        node._ndata.add(IC10("j", [end_label]))

    def handle_name(self, node: nodes.Name):
        # todo: detect if name is in locals/globals
        # throw proper error if not
        name = node.name
        scope_name = get_scope_name(node)

        if name in self.data.modules:
            node._ndata.result = self.data.modules[name]
            return
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
        elif name in self.data.structures.get(scope_name, {}):
            node._ndata.result = self.data.structures[scope_name][name]
        else:
            sym_data = self.data.get_sym_data(node)
            node._ndata.result = sym_data

    def handle_const(self, node: nodes.Const):
        data = node._ndata
        if isinstance(node.value, bool):
            data.result = IC10Operand(int(node.value))
        elif isinstance(node.value, (int, float)):
            data.result = IC10Operand(node.value)
        elif isinstance(node.value, str):
            data.result = node.value
        elif isinstance(node.value, type(None)):
            data.result = ""
        else:
            raise CompilerError(f"Unsupported constant type: {type(node.value)}", node)

    def handle_function_def(self, node: nodes.FunctionDef):
        fname = get_function_name(node)
        self.functions[fname] = node

    def compile_function(self, node: nodes.FunctionDef):
        data = node._ndata
        if data.code[""]:
            # function already compiled
            return
        fname = get_function_name(node)
        sym_data = self.data.get_sym_data(node)
        label = fname.replace("_", ".")
        data.add(IC10(f"{label}:"))
        data.add_end(IC10(f"{label}end:"))

        func_data = self.data.functions[fname]

        if self.data.options.inline_functions and func_data.can_inline:
            ret_value = self.get_register_name() if func_data.has_return_value else ""
            sym_data.code_expr = ret_value
            calling_node = sym_data.nodes_reading[0].parent

            if len(node.args.args) != len(calling_node.args):
                raise CompilerError(
                    f"Function {fname} expects {len(node.args.args)} arguments, but {len(calling_node.args)} were given.",
                    calling_node,
                )
            for i, arg in enumerate(node.args.args):
                arg_sym = self.data.get_sym_data(arg)
                calling_arg = calling_node.args[i]._ndata.result
                if arg_sym.is_overwritten:
                    # need to copy argument to a register, as it is overwritten in the function
                    arg_sym.code_expr = self.get_register_name()
                    data.add(IC10("move", [calling_arg], arg_sym))
                else:
                    if isinstance(calling_arg, IC10Register):
                        calling_arg = calling_arg.code_expr
                    elif isinstance(calling_arg, IC10Operand):
                        calling_arg = calling_arg.value
                    arg_sym.code_expr = calling_arg
                func_data.args.append(arg_sym)
        else:
            for i, arg in enumerate(node.args.args):
                reg = self.get_register_name()
                sym = self.data.get_sym_data(arg)
                sym.code_expr = reg
                data.add(
                    IC10(
                        "get",
                        ["db", _RETURN_VALUE_ADDRESS - 1 - i],
                        sym,
                        indent=1,
                    )
                )
                if arg.name in symbols.__dict__:
                    raise CompilerError(
                        f"Function argument name {arg.name} conflicts with a built-in name",
                        arg,
                    )
                sym.nodes_writing.append(arg)
                arg._ndata.result = sym
                func_data.args.append(sym)

        for stmt in node.body:
            self._visit_node(stmt)

        apply_tail_call_optimization = False

        if node.body and (
            not func_data.can_inline or not self.data.options.inline_functions
        ):
            last_node = node.body[-1]
            if isinstance(last_node, nodes.Expr):
                last_node = last_node.value

            if isinstance(last_node, nodes.Call):
                ndata = last_node._ndata
                sd = self.data.get_sym_data(last_node.func)
                if sd.is_read != 1 or not self.data.options.inline_functions:
                    apply_tail_call_optimization = True
                    last_op = ndata.code[""][-1]
                    if not last_op.op == "jal":
                        raise CompilerError(
                            "Tail call optimization can only be applied to direct function calls",
                            last_node,
                        )
                    last_op.op = "j"

        if not apply_tail_call_optimization and (
            sym_data.is_read != 1 or not self.data.options.inline_functions
        ):
            data.add_end(IC10("j", ["ra"], indent=1))

    def handle_assign_name(self, node: nodes.AssignName):
        data = node._ndata
        sym = self.data.get_sym_data(node.targets[0])
        node.targets[0]._ndata.result = sym
        data.result = sym
        # list(node.get_children())[0]._ndata.result = sym

    def handle_assign(self, node: nodes.Assign):
        target = node.targets[0]
        data = node._ndata

        if data.is_compiled:
            return

        data.is_compiled = True

        # TODO: use define instead of move for constants

        if len(node.targets) != 1:
            raise NotImplementedError("Multiple assignment targets are not supported")

        elif isinstance(target, nodes.AssignName):
            value = self.compile_node(node.value)
            value_name = value.__name__ if isinstance(value, type) else value
            if isinstance(value, IC10Instruction):
                sym_data = self.data.get_sym_data(target)
                if not sym_data.code_expr:
                    sym_data.code_expr = self.get_register_name()
                value.output = sym_data
                data.result = sym_data
            elif isinstance(value, (IC10Register, IC10Operand)):
                sym_data = self.data.get_sym_data(target)
                can_assign_directly = not sym_data.is_overwritten
                if can_assign_directly:
                    sym_data.code_expr = (
                        value.code_expr
                        if isinstance(value, IC10Register)
                        else value.value
                    )
                    data.result = sym_data
                    target._ndata.result = sym_data
                    return
                # raise CompilerError(
                #     f"Cannot assign symbol {value.name} to name {target.name}", target
                # )
                if not sym_data.code_expr:
                    sym_data.code_expr = self.get_register_name()
                if sym_data != value:
                    data.add(IC10("move", [value], sym_data))
                # data.result = value
                # # assign new name to symbol instead of extra move instruction
                # value.name = target.name
                # self.set_name(target, value, target.name)
            elif is_builtin_structure(value) or value_name in symbols.__dict__:
                data.result = value
                structures = self.data.structures
                scope_name = get_scope_name(target)
                if scope_name not in structures:
                    structures[scope_name] = {}
                scope_vars = structures[scope_name]
                if target.name in scope_vars:
                    raise CompilerError(
                        f"Cannot reassign assign {value_name} to {target.name} at line {node.lineno}",
                        node,
                    )
                scope_vars[target.name] = value
            else:
                sym_data = self.data.get_sym_data(target)
                can_assign_directly = not sym_data.is_overwritten
                if isinstance(node.value, nodes.Call):
                    can_assign_directly = can_assign_directly and is_builtin_function(
                        node.value.func.name
                    )
                if can_assign_directly:
                    sym_data.name = value  # self.get_constant_name()
                    # sym.name = value
                    # sym.is_constant = True
                    data.result = sym_data
                else:
                    reg = sym_data.code_expr or self.get_register_name()
                    if reg != value:
                        data.add(IC10("move", [value], sym_data))
                    sym_data.code_expr = reg
                    data.result = sym_data
            target._ndata.result = data.result
            target._ndata.is_compiled = True
        elif isinstance(target, nodes.AssignAttr):
            rhs = self.compile_node(list(node.get_children())[1])
            lhs = self.compile_node(target)
            expr = lhs._set(rhs)
            data.add(expr)
        elif isinstance(target, nodes.Subscript):
            rhs = self.compile_node(node.value)
            lhs = self.compile_node(target.value)
            slice_ = self.compile_node(target.slice)
            if not isinstance(lhs, types.Stack):
                raise CompilerError(f"Cannot subscript {type(lhs)}", target)
            value = lhs[slice_]
            data.add(value._set(rhs))
        else:
            raise CompilerError(f"Unsupported assignment target: {type(target)}")

    def handle_assign_attr(self, node: nodes.AssignAttr):
        expr = self.compile_node(node.expr)
        if not hasattr(expr, node.attrname):
            raise CompilerError(
                f"Invalid attribute {node.attrname} in expression {node.as_string()}",
                node,
            )
        val = getattr(expr, node.attrname)
        if isinstance(val, property):
            val = val.fget(expr)

        node._ndata.result = val

    def handle_subscript(self, node: nodes.Subscript):
        from .types import _StackValue

        value = self.compile_node(node.value)
        slice_ = self.compile_node(node.slice)
        res = value[slice_]
        data = node._ndata
        if isinstance(res, _StackValue):
            sym = self.get_intermediate_symbol(node)
            data.add(value[slice_]._load(sym))
            res = sym
        data.result = res

    def handle_compare(self, node: nodes.Compare):
        if (
            isinstance(node.parent, (nodes.If, nodes.While))
            and node == node.parent.test
        ):
            # no need to calculate comparison result, it's done by the branch instruction of the parent
            return
        sym = self.get_intermediate_symbol(node)
        left = self.compile_node(node.left)
        right = self.compile_node(node.ops[0][1])

        instruction = "s" + get_comparison_suffix(node.ops[0][0])
        data = node._ndata
        data.add(IC10(instruction, [left, right], sym))
        data.result = sym

    def handle_ifexp(self, node: nodes.IfExp):
        test = self.compile_node(node.test)
        left = self.compile_node(node.body)
        right = self.compile_node(node.orelse)

        sym = self.get_intermediate_symbol(node)
        data = node._ndata
        data.result = sym
        data.add_end(IC10("select", [test, left, right], sym))

    def handle_if(self, node: nodes.If):
        else_label, end_label = self.get_label("else", "end")
        
        test_node = node.test
        negate_test = False
        
        if isinstance(test_node, nodes.UnaryOp) and test_node.op == "not":
            test_node = test_node.operand
            negate_test = True
        
        test = self.compile_node(test_node)

        emit_if = len(node.body) > 0
        emit_else = len(node.orelse) > 0

        data = node._ndata
        test_data = test_node._ndata
        
        if test_data.is_constant:
            if test_data.constant_value:
                emit_else = negate_test
            else:
                emit_if = negate_test
        elif isinstance(test_node, nodes.Compare):
            left = self.compile_node(test_node.left)
            right = self.compile_node(test_node.ops[0][1])
            cmp_op = test_node.ops[0][0]

            instruction = "b" + (get_comparison_suffix(cmp_op) if negate_test else get_negated_comparison_suffix(cmp_op))
            data.add(IC10(instruction, [left, right, else_label]))
        elif isinstance(test_node, nodes.Const):
            if test_node.value:
                emit_else = negate_test
            else:
                emit_if = negate_test
        elif isinstance(test_node, (nodes.BoolOp, nodes.Name, nodes.Attribute)):
            data.add(IC10("bnez" if negate_test else "beqz", [test, else_label]))
        else:
            raise NotImplementedError(f"Unsupported if test: {type(test_node)}")

        for stmt in node.body:
            if emit_if:
                self._visit_node(stmt)
            else:
                stmt._ndata.is_used = False

        if emit_if:
            if emit_else:
                data.add_else(IC10("j", [end_label]))
            data.add_else(IC10(f"{else_label}:", indent=-1))

        for stmt in node.orelse:
            if emit_else:
                self._visit_node(stmt)
            else:
                stmt._ndata.is_used = False

        data.add_end(IC10(f"{end_label}:", indent=-1))

    def handle_unop(self, node: nodes.UnaryOp):
        data = node._ndata

        if data.is_constant:
            data.result = IC10Operand(data.constant_value)
            return

        opcode, _ = get_unop_instruction(node.op)
        if opcode is None:
            raise CompilerError(f"Unsupported unary operation: {node.op}", node)

        opname = self.compile_node(node.operand)
        sym = self.get_intermediate_symbol(node)
        data.result = sym
        if opcode == "sub":
            data.add_end(IC10(opcode, [0, opname], sym))
        else:
            data.add_end(IC10(opcode, [opname], sym))

    def handle_immediate_op(self, node: nodes.AugAssign):
        if node.op[-1] != "=":
            raise CompilerError(f"Unsupported immediate operation: {node.op}", node)
        op = node.op[:-1]
        instruction = get_binop_instruction(op)[0]
        sym = self.data.get_sym_data(node.target)
        left_name = sym
        right_name = self.compile_node(node.value)
        data = node._ndata
        data.result = sym
        data.add_end(IC10(instruction, [left_name, right_name], left_name))

    def handle_binop(self, node: nodes.BinOp):
        data = node._ndata

        if data.is_constant:
            data.result = IC10Operand(data.constant_value)
            return

        left, right = node.get_children()
        left_name = self.compile_node(left)
        right_name = self.compile_node(right)
        op = node.op
        instruction, func = get_binop_instruction(op)
        if instruction is None:
            raise CompilerError(f"Unsupported binary operation: {op}", node)

        if isinstance(left, nodes.Const) and isinstance(right, nodes.Const):
            data.result = IC10Operand(func(left.value, right.value))
        else:
            sym = self.get_intermediate_symbol(node)
            data.result = sym
            data.add_end(IC10(instruction, [left_name, right_name], sym))

    def handle_for(self, node: nodes.For):
        iter_ = node.iter

        if (
            not isinstance(iter_, nodes.Call)
            or not isinstance(iter_.func, nodes.Name)
            or iter_.func.name != "range"
        ):
            raise CompilerError(
                "Only for loops over ranges are supported currently", node
            )

        args = iter_.args
        start = 0
        end = None
        step = 1
        is_increasing = True
        n_args = len(args)

        if n_args == 1:
            end = self.compile_node(args[0])
        elif n_args == 2:
            start = self.compile_node(args[0])
            end = self.compile_node(args[1])
        elif n_args == 3:
            start = self.compile_node(args[0])
            end = self.compile_node(args[1])
            step = self.compile_node(args[2])
            if args[2]._ndata.is_constant:
                is_increasing = args[2]._ndata.constant_value >= 0

        for_label, end_label = self.get_label("for", "for.end")
        data = node._ndata
        data.start_label = for_label
        data.end_label = end_label

        iter_sym = self.get_intermediate_symbol(node)
        data.add(IC10("move", [start], iter_sym))
        data.add(IC10(f"{for_label}:"))

        data.add(IC10("bge" if is_increasing else "ble", [iter_sym, end, end_label]))
        target_sym = self.data.get_sym_data(node.target)

        if not target_sym.code_expr:
            target_sym.code_expr = iter_sym.code_expr

        for stmt in node.body:
            self.compile_node(stmt)
        data.add_end(IC10("add", [iter_sym, step], iter_sym, indent=1))
        data.add_end(IC10("j", [for_label], indent=1))
        data.add_end(IC10(f"{end_label}:"))

    def handle_while(self, node: nodes.While):
        test = node.test
        while_label, end_label = self.get_label("while", "while.end")
        data = node._ndata

        data.start_label = while_label
        data.end_label = end_label

        data.add(IC10(f"{while_label}:"))
        if isinstance(test, nodes.Compare):
            left = self.compile_node(test.left)
            cmp_op, right_node = test.ops[0]
            right = self.compile_node(right_node)

            instruction = "b" + get_negated_comparison_suffix(cmp_op)
            data.add(IC10(instruction, [left, right, end_label]))
        elif isinstance(test, nodes.Const):
            if not test.value:
                return
        else:
            raise CompilerError(f"Unsupported while test: {type(test)}", node)

        for stmt in node.body:
            self.compile_node(stmt)

        data.add_end(IC10("j", [while_label], indent=1))
        data.add_end(IC10(f"{end_label}:"))

    def run(self):
        for module in self.data.modules.values():
            self._visit_node(module)
        self._visit_node(self.tree)


class CompilerPassGatherCode(CompilerPass):
    def __init__(self, data: CodeData):
        super().__init__(data)
        self.code = []
        self._indent_level = 0

        self._target = None

        # for scope, data in self.data.symbols.items():
        #     print(f"IC10Register in scope '{scope}'")
        #     for name, d in data.items():
        #         print(f"\t{name} {d.is_read} {d.is_written}")

    def add_line(self, line: IC10Instruction):
        line.indent += self._indent_level
        self._target.code.append(line)

    @contextmanager
    def indent(self, num_indents=1):
        if isinstance(num_indents, bool):
            num_indents = 1 if num_indents else 0

        self._indent_level += num_indents
        yield
        self._indent_level -= num_indents

    def gather_code(self, node: nodes.NodeNG, special_nodes=None):
        data = node._ndata
        special_nodes = special_nodes or []
        if "" in data.code:
            for line in data.code[""]:
                self.add_line(line)

        do_indent = isinstance(
            node, (nodes.FunctionDef, nodes.While, nodes.For, nodes.If)
        )

        with self.indent(do_indent):
            for child in node.get_children():
                if child not in special_nodes:
                    self._visit_node(child)

            for line in data.code.get("else", []):
                self.add_line(line)

            if isinstance(node, nodes.If):
                for child in node.orelse:
                    self._visit_node(child)
            if isinstance(node, nodes.IfExp):
                self._visit_node(node.orelse)

        for line in data.code.get("end", []):
            self.add_line(line)

    def handle_node(self, node: nodes.NodeNG):
        if not hasattr(node, "_ndata"):
            return
        data = node._ndata
        if not data.is_used:
            return

        old_target = self._target

        if isinstance(node, nodes.FunctionDef):
            fname = get_function_name(node)
            self._target = self.data.functions[fname]

        if isinstance(node, nodes.Call):
            fname = get_function_name(node.func)
            if not is_builtin_name(fname):
                if fname not in self.data.functions:
                    raise CompilerError(f"Function {fname} is not defined.", node)

                func = self.data.functions[fname]
                if self.data.options.inline_functions and func.can_inline:
                    node._ndata.code[""] = [
                        l for l in node._ndata.code[""] if l.op != "jal"
                    ]
                    node._ndata.code[""] += func.code
                    func.code = []

        if isinstance(data.code, str):
            data.code = [data.code]

        if isinstance(node, nodes.While):
            if data.code[""][0].op.endswith(":"):
                # emit while loop start label explicitly now, before any comparison is generated
                self.add_line(data.code[""][0])
                data.code[""] = data.code[""][1:]

        special_nodes = set()
        if hasattr(node, "test"):
            special_nodes.add(node.test)
            self._visit_node(node.test)

        if isinstance(node, nodes.Assign):
            special_nodes.add(node.value)
            self._visit_node(node.value)
            target = node.targets[0]
            special_nodes.add(target)
            self._visit_node(target)

        if isinstance(node, nodes.Subscript):
            special_nodes.add(node.value)
            self._visit_node(node.value)
            special_nodes.add(node.slice)
            self._visit_node(node.slice)

        if isinstance(node, nodes.BinOp):
            for child in node.get_children():
                special_nodes.add(child)
                self._visit_node(child)

        if isinstance(node, nodes.If):
            for child in node.orelse:
                special_nodes.add(child)

        if isinstance(node, nodes.Compare):
            special_nodes.add(node.left)
            self._visit_node(node.left)
            for _, right in node.ops:
                special_nodes.add(right)
                self._visit_node(right)
            # if (
            #     isinstance(node.parent, (nodes.If, nodes.While))
            #     and node == node.parent.test
            # ):
            #     # no need to calculate comparison result, it's done by the branch instruction of the parent
            #     data.code[""] = []
            #
        if isinstance(node, nodes.Call):
            for arg in node.args:
                special_nodes.add(arg)
                self._visit_node(arg)

        if isinstance(node, nodes.Return) and node.value is not None:
            special_nodes.add(node.value)
            self._visit_node(node.value)

        self.gather_code(node, special_nodes)

        self._target = old_target

    def run(self):
        functions = self.data.functions
        self._target = functions[""] = FunctionData(None, None)

        for module in self.data.modules.values():
            self._visit_node(module)
        self._visit_node(self.tree)

        for fname in sorted(self.data.functions.keys()):
            func = self.data.functions[fname]
            if func.is_constexpr:
                continue
            if fname != "" and func.is_called:
                func.add_ra_instructions()
            if fname == "" or func.is_called:
                for line in func.code:
                    self.code.append(line)

        self.used_registers = assign_registers(self.data, self.code)
        self.get_code()

    def remove_labels(
        self, code, relative_numbers: bool = True, keep_labels: set | None = None
    ) -> str:
        label_map = {}
        i_line = 0
        new_code = []
        keep_labels = keep_labels or set()

        if relative_numbers:
            # we must keep labels that are the target of jal instructions,
            # because there is no jral
            for line in code.splitlines():
                cline = line.split("#")[0].strip()
                op = cline.split()[0] if cline else ""
                if is_branch(op) and not op in _HAS_RELATIVE_INSTRUCTION:
                    parts = cline.split()
                    if len(parts) >= 2:
                        label = parts[1]
                        keep_labels.add(label)

        for line in code.splitlines():
            cline = line.split("#")[0].strip()
            label = cline[:-1] if cline.endswith(":") else None
            if label and label not in keep_labels:
                label = cline[:-1]
                label_map[label] = len(new_code)
            else:
                i_line += 1
                new_code.append(line)

        for line_num, line in enumerate(new_code):
            for label, target_line in label_map.items():
                pattern = r"\b{}\b".format(re.escape(label))
                if re.search(pattern, line):
                    if relative_numbers:
                        offset = target_line - line_num
                        replacement = str(offset)
                        instruction = line.split("#")[0].strip().split()[0]
                        if instruction == "jal":
                            replacement = str(target_line)
                        new_instruction = instruction[:1] + "r" + instruction[1:]
                        line = line.replace(instruction, new_instruction, 1)
                    else:
                        replacement = str(target_line)

                    line = re.sub(pattern, replacement, line)
            new_code[line_num] = line

        new_code = "\n".join(new_code)

        # for label, line_num in label_map.items():
        #     pattern = r"\b{}\b".format(re.escape(label))
        #     new_code = re.sub(pattern, str(line_num), new_code)

        return new_code

    def strip_code(self, code: str) -> str:
        return "\n".join([line.strip() for line in code.splitlines()])

    def get_code(
        self,
    ):
        s = ""

        shift = 2
        code_width = 0

        lines = []

        for line in self.code:
            lines.append(line.to_string(shift))
            code_width = max(code_width, len(lines[-1]))

        just_width = min(60, code_width + 4)

        options = self.data.options
        original_code = self.data.original_code

        prev_comment = None
        for i, line in enumerate(self.code):
            c = lines[i]
            if c.endswith(":"):
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
