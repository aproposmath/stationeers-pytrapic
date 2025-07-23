from contextlib import contextmanager

import astroid

from . import intrinsics, structures_generated, symbols, types
from .compile_pass import CodeLine, CompilerError, CompilerPass, Symbol
from .utils import is_constant, logger


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
        "+": "add",
        "-": "sub",
        "*": "mul",
        "/": "div",
        "%": "mod",
    }.get(op, None)


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
    def __init__(self, tree: astroid.Module):
        logger.info("Initializing CompilerPassGenerateCode")
        super().__init__(tree)
        self._name_counter = 0
        self._symbol_counter = 0

        self._names = {}

        self.ignore_nodes(astroid.ImportFrom, astroid.Import, astroid.Pass)

    def set_name(
        self, node: astroid.NodeNG, symbol: Symbol, identifyer: str | None = None
    ):
        logger.info("set name %s %s %s", node, symbol, identifyer)
        if identifyer is not None:
            scope_name = node.scope().name
            key = (scope_name, identifyer)
            if key in self._names:
                raise CompilerError(
                    f"Name {identifyer} already exists in scope {scope_name}", node
                )
            self._names[key] = symbol
        else:
            self._names[node] = symbol

    def get_name(self, node: astroid.NodeNG, identifyer: str | None = None) -> str:
        logger.debug("get name %s %s", node, identifyer)
        scope_name = node.scope().name
        symbol_id = self._symbol_counter
        self._symbol_counter += 1
        if identifyer is None:
            if node not in self._names:
                identifyer = f"tmp_{self._name_counter}"
                self._names[node] = Symbol(
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
                self._names[key] = Symbol(symbol_id, scope_name, identifyer)
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
        if node._ndata.is_compiled:
            return node._ndata.result
        self._visit_node(node)
        node._ndata.is_compiled = True
        return node._ndata.result

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

        if attrname in ["Minimum", "Maximum", "Sum", "Average"]:
            symbol = self.get_name(node)
            data.add(attr(symbol), attrname)
            data.result = symbol
        elif isinstance(attr, symbols.DeviceLogicType):
            symbol = self.get_name(node)
            data.add(attr._load(symbol), attrname)
            data.result = symbol
        else:
            data.result = attr


    def handle_call(self, node: astroid.Call):
        data = node._ndata

        fname = node.func.name
        if not hasattr(intrinsics, fname):
            data.add(f"jal {fname}", f"call {fname}")
            return

        func = getattr(intrinsics, fname)
        args = [self.compile_node(arg) for arg in node.args]
        result = func(*args)
        if fname == "HASH" or hasattr(types, fname):
            data.result = str(result)
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
            node._ndata.result = self.get_name(node, name)

    def handle_const(self, node: astroid.Const):
        data = node._ndata
        if isinstance(node.value, bool):
            data.result = int(node.value)
        elif isinstance(node.value, (int, float)):
            data.result = str(node.value)
        elif isinstance(node.value, str):
            data.result = f'"{node.value}"'
        else:
            raise CompilerError(f"Unsupported constant type: {type(node.value)}", node)

    def handle_function_def(self, node: astroid.FunctionDef):
        data = node._ndata
        data.add(f"{node.name}:", "function definition")
        data.add_end("j ra", "return from function", 1)

        if len(node.args.args):
            raise CompilerError("Function arguments are not supported yet", node)

        if node.returns:
            raise CompilerError("Function return values not supported yet", node)

        for stmt in node.body:
            self._visit_node(stmt)

    def handle_assign_name(self, node: astroid.AssignName):
        data = node._ndata
        reg = self.get_name(node, node.name)
        data.result = reg

    def handle_assign(self, node: astroid.Assign):
        target = node.targets[0]
        data = node._ndata

        if data.is_compiled:
            return

        data.is_compiled = True

        # TODO: use define instead of move for constants

        if len(node.targets) != 1:
            raise NotImplementedError("Multiple assignment targets are not supported")

        elif isinstance(target, astroid.AssignName):
            value = self.compile_node(node.value)
            if isinstance(value, (symbols.GenericStructures, symbols.GenericStructure)):
                data.result = value
                self.set_name(target, value, target.name)
            elif isinstance(value, Symbol):
                data.result = value
                # assign new name to symbol instead of extra move instruction
                value.name = target.name
                self.set_name(target, value, target.name)
            else:
                value = self.compile_node(node.value)
                reg = self.get_name(target, target.name)
                data.add(f"move {reg} {value}", "assign name")
                data.result = reg
        elif isinstance(target, astroid.AssignAttr):
            rhs = self.compile_node(list(node.get_children())[1])
            lhs = self.compile_node(target)
            expr = lhs._set(rhs)
            data.add(f"{expr}", "assign attribute")
        else:
            raise CompilerError(f"Unsupported assignment target: {type(target)}")

    def handle_assign_attr(self, node: astroid.AssignAttr):
        expr = self.compile_node(node.expr)
        val = getattr(expr, node.attrname)
        node._ndata.result = val

    def handle_subscript(self, node: astroid.Subscript):
        value = self.compile_node(node.value)
        slice_ = self.compile_node(node.slice)
        node._ndata.result = value[slice_]

    def handle_compare(self, node: astroid.Compare):
        reg = self.get_name(node)
        left = self.compile_node(node.left)
        right = self.compile_node(node.ops[0][1])

        instruction = "s" + get_comparison_suffix(node.ops[0][0])
        data = node._ndata
        data.add(f"{instruction} {reg} {left} {right}", "compare")
        data.result = reg

    def handle_ifexp(self, node: astroid.IfExp):
        test = self.compile_node(node.test)
        left = self.compile_node(node.body)
        right = self.compile_node(node.orelse)

        data = node._ndata
        data.result = self.get_name(node)
        data.add(f"select {data.result} {test} {left} {right}", "if expression")

    def handle_if(self, node: astroid.If):
        else_label = self.get_label("else")

        test = self.compile_node(node.test)

        emit_if = len(node.body) > 0
        emit_else = len(node.orelse) > 0

        data = node._ndata
        test_data = node.test._ndata

        if test_data.is_constant_value:
            if test_data.result:
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
        elif isinstance(node.test, astroid.Attribute):
            data.add(f"bne {test} {else_label}", "if with attribute")
        else:
            raise NotImplementedError(f"Unsupported if test: {type(node.test)}")

        for stmt in node.body:
            if emit_if:
                self._visit_node(stmt)
            else:
                stmt._ndata.is_used = False

        if emit_if:
            data.add_else(f"{else_label}:", "", -1)

        for stmt in node.orelse:
            if emit_else:
                self._visit_node(stmt)
            else:
                stmt._ndata.is_used = False

    def handle_binop(self, node: astroid.BinOp):
        left_name = self.compile_node(node.left)
        right_name = self.compile_node(node.right)

        op = node.op

        data = node._ndata
        data.result = self.get_name(node)
        instruction = get_binop_instruction(op)
        if instruction is None:
            raise CompilerError(f"Unsupported binary operation: {op}", node)

        data.add(
            f"{instruction} {data.result} {left_name} {right_name}", "binary operation"
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
    def __init__(self, tree: astroid.Module):
        super().__init__(tree)
        self.code = []
        self._indent_level = 0
        self._symbols = set()

        self._functions = []
        self._called_functions = set()

        self._target = None
        self._function_codes = {}

    def add_line(self, line: CodeLine):
        line.indent += self._indent_level
        if self._target is not None:
            if self._target not in self._function_codes:
                self._function_codes[self._target] = []
            code = self._function_codes[self._target]
        else:
            code = self.code
        code.append(line)
        self.scan_symbols(line)

    def scan_symbols(self, line: CodeLine):
        tokens = line.code.split()
        for token in tokens:
            if token.startswith("__symbol_"):
                self._symbols.add(token)

    def replace_symbols(self, line: CodeLine):
        symbols = sorted(self._symbols)
        symbol_map = {symbol: f"r{i}" for i, symbol in enumerate(symbols)}

        for line in self.code:
            for symbol in symbols:
                if symbol in line.code:
                    line.code = line.code.replace(symbol, symbol_map[symbol])

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
            self._target = node.name
            self._functions.append(node)

        if isinstance(node, astroid.Call):
            self._called_functions.add(node.func.name)

        if isinstance(data.code, str):
            data.code = [data.code]

        if isinstance(node, astroid.While):
            if data.code[''][0].code.endswith(":"):
                # emit while loop start label explicitly now, before any comparison is generated
                self.add_line(data.code[''][0])
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
        self._visit_node(self.tree)

        function_names = set()
        for func in self._functions:
            if func.name in function_names:
                raise CompilerError(f"Function {func.name} is defined multiple times.")
            function_names.add(func.name)

        for func in self._functions:
            if func.name in self._called_functions:
                for line in self._function_codes[func.name]:
                    self.add_line(line)

    def get_code(
        self,
        append_comments=False,
        append_original_line=True,
        original_code: str = None,
    ) -> dict:
        s = ""
        if original_code is not None:
            original_code = original_code.splitlines()

        shift = 2
        code_width = 0

        for line in self.code:
            self.replace_symbols(line)
            line.code = " " * (line.indent * shift) + line.code
            code_width = max(code_width, len(line.code))

        just_width = min(60, code_width + 4)

        prev_comment = None
        for line in self.code:
            self.replace_symbols(line)
            c = line.code
            if line.code.endswith(":"):
                # labels are not allowed to have indentation
                c = c.strip()

            if append_comments and line.comment:
                if prev_comment != line.comment:
                    c = c.ljust(just_width) + " # " + line.comment
                    prev_comment = line.comment
            elif append_original_line and line.node and original_code:
                ori_line = original_code[line.node.lineno - 1]
                if prev_comment != ori_line:
                    c = c.ljust(just_width)
                    c += f" # {ori_line}"
                    prev_comment = ori_line

            s += c + "\n"

        s = s[:-1]  # remove last newline

        logger.info("Number of used registers: %i", len(self._symbols))

        if len(self._symbols) > 16:
            raise CompilerError("Running out of registers.")

        s = remove_unused_labels(s)

        num_lines = len(s.splitlines())
        num_registers = len(self._symbols)

        return {"code": s, "num_lines": num_lines, "num_registers": num_registers}
