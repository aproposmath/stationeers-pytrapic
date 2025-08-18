import re
from contextlib import contextmanager

import astroid

from . import intrinsics, structures_generated, symbols, types
from .compile_pass import (
    CodeData,
    CodeLine,
    CompilerError,
    CompilerPass,
    FunctionData,
    SymbolData,
)
from .utils import is_builtin_name, is_constant, logger
from . import _version


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


def get_binop_instruction(op: str):
    return {
        "+": ("add", lambda x, y: x + y),
        "-": ("sub", lambda x, y: x - y),
        "*": ("mul", lambda x, y: x * y),
        "/": ("div", lambda x, y: x / y),
        "%": ("mod", lambda x, y: x % y),
        "and": ("and", lambda x, y: x and y),
        "or": ("or", lambda x, y: x and y),
    }.get(op, (None, None))


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
    def __init__(self, data: CodeData):
        super().__init__(data)
        logger.info("Initializing CompilerPassGenerateCode")
        self._name_counter = 0
        self._symbol_counter = 0

        self._names = {}

        self.ignore_nodes(astroid.ImportFrom, astroid.Import, astroid.Pass)

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
        elif isinstance(attr, symbols.DeviceLogicType):
            symbol = self.get_intermediate_symbol(node)
            data.add(attr._load(symbol.code_expr), attrname)
            data.result = symbol
        else:
            data.result = attr

    def handle_call(self, node: astroid.Call):
        data = node._ndata

        fname = node.func.name
        if not hasattr(symbols, fname):
            data.add(f"jal {fname.replace('_','.')}", f"call {fname}")
            return

        func = getattr(symbols, fname)
        kwargs = {kw.arg: self.compile_node(kw.value) for kw in node.keywords}
        args = [self.compile_node(arg) for arg in node.args]
        result = func(*args, **kwargs)
        if isinstance(
            result,
            (
                symbols.GenericStructures,
                symbols.GenericStructure,
                types._BaseStructure,
                types._BaseStructures,
            ),
        ):
            data.result = result
        elif fname == "HASH" or hasattr(types, fname):
            data.result = result
        else:
            data.add(result, "intrinsic called")

    def handle_expr(self, node: astroid.Expr):
        self._visit_node(node.value)

    def handle_return(self, node: astroid.Return):
        if node.value is not None:
            raise CompilerError("Return value is not supported", node)
        node._ndata.add("j ra", "return from function")

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
        else:
            raise CompilerError(f"Unsupported constant type: {type(node.value)}", node)

    def handle_function_def(self, node: astroid.FunctionDef):
        data = node._ndata
        data.add(f"{node.name}:".replace("_", "."), "function definition")
        data.add_end("j ra", "return from function", 1)

        if len(node.args.args):
            raise CompilerError("Function arguments are not supported yet", node)

        if node.returns:
            raise CompilerError("Function return values not supported yet", node)

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
            elif value_name in symbols.__dict__ or isinstance(
                value,
                (
                    symbols.GenericStructures,
                    symbols.GenericStructure,
                    types._BaseStructure,
                    types._BaseStructures,
                ),
            ):
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
                if node.value._ndata.is_constant_value or not sym_data.is_overwritten:
                    sym_data.code_expr = value  # self.get_constant_name()
                    # sym.name = value
                    # sym.is_constant = True
                    data.result = value
                else:
                    reg = sym_data.code_expr or self.get_register_name()
                    data.add(f"move {reg} {value}", "assign name")
                    sym_data.code_expr = reg
                    data.result = reg
            target._ndata.result = data.result
            target._ndata.is_compiled = True
        elif isinstance(target, astroid.AssignAttr):
            rhs = self.compile_node(list(node.get_children())[1])
            lhs = self.compile_node(target)
            if isinstance(lhs, symbols.DeviceLogicType) and lhs._device_id._id is None:
                name = lhs._cls.__name__
                raise CompilerError(
                    f"""Cannot use "{name}"" directly, either use "{name}s" to set all devices of this type or create a specific device with "{name}(d0)".""",
                    target,
                )

            if isinstance(rhs, symbols.DevicesLogicType):
                raise CompilerError(
                    "You need to take either Minimum/Maximum/Average/Sum", target
                )
            expr = lhs._set(rhs)
            data.add(f"{expr}", "assign attribute")
        else:
            raise CompilerError(f"Unsupported assignment target: {type(target)}")

    def handle_assign_attr(self, node: astroid.AssignAttr):
        expr = self.compile_node(node.expr)
        if isinstance(expr, SymbolData):
            raise CompilerError(f"Cannot assign to symbol {expr.name} directly", node)
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

        self._called_functions = set()

        self._target = None
        self._function_codes = {}

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
            # emit function definitions after all other code
            # otherwise the function would be executed if it's defined before the call
            sym_data = self.data.get_sym_data(node)
            self._target = self.data.functions[node.name] = FunctionData(node, sym_data)

        if isinstance(node, astroid.Call):
            fname = node.func.name
            if not is_builtin_name(fname):
                if fname not in self.data.functions:
                    raise CompilerError(
                        f"Function {node.func.name} is not defined.", node
                    )

                func = self.data.functions[fname]
                if self.data.options.inline_functions and func.can_inline:
                    node._ndata.code[""] = func.code[:-1]
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

        self.gather_code(node, special_nodes)

        self._target = old_target

    def run(self):
        functions = self.data.functions
        self._target = functions[""] = FunctionData(None, None)

        self._visit_node(self.tree)

        for fname in self.data.functions.keys():
            func = self.data.functions[fname]
            if fname == "" or func.is_called:
                for line in func.code:
                    self.code.append(line)

        self.assign_registers()

        self.get_code()

    def assign_registers(self):
        registers = list(range(16))

        tokens = set(" ".join([line.code.split("#")[0] for line in self.code]).split())

        mapping = {}

        scope_names = sorted(self.data.symbols.keys())
        for scope in scope_names:
            scope_registers = registers.copy()
            for name, symbol in self.data.symbols[scope].items():
                if not symbol.code_expr in tokens:
                    continue

                if symbol.is_register and symbol.code_expr not in mapping:
                    reg_num = scope_registers.pop(0)
                    mapping[symbol.code_expr] = f"r{reg_num}"
                    # print("assign name", symbol.code_expr, "to", mapping[symbol.code_expr])

            if scope == "":
                registers = scope_registers

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
            s += f"\n\n# Generated by Stationeers-PyTrapIC v{_version.__version__}"

        num_lines = len(s.splitlines())
        num_registers = len(self.used_registers)
        num_bytes = len(s) + num_lines - 1

        self.data.result = {
            "code": s,
            "num_lines": num_lines,
            "num_registers": num_registers,
            "num_bytes": num_bytes,
            "used_registers": self.used_registers,
        }
