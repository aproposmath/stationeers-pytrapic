from astroid import nodes

from .compile_pass import CodeData
from .types import IC10Register, IC10Instruction
from .utils import get_scope_name, CompilerError


def assign_colors(symbols: list[IC10Register]):
    # Sort by start time
    symbols_sorted = sorted(symbols, key=lambda s: s.lifetime.start)

    active = []  # list of (end, color) for currently active intervals
    free_colors = []  # pool of reusable colors
    next_color = 0
    # print("symbols_sorted")
    # for s in symbols_sorted:
    #     print(f"\t{s.name} {s.lifetime} {s._is_intermediate}")

    for sym in symbols_sorted:
        start, end = sym.lifetime.start, sym.lifetime.stop

        # Expire intervals that ended before this one starts
        still_active = []
        for e, c in active:
            if e <= start:
                free_colors.append(c)
            else:
                still_active.append((e, c))
        active = still_active

        # Assign a color (reuse if possible)
        if free_colors:
            sym._color = free_colors.pop()
        else:
            sym._color = next_color
            next_color += 1

        # Add to active set
        active.append((end, sym._color))

    return symbols


def assign_registers(data: CodeData, code: list[IC10Instruction]):
    # topological sort of function scopes
    called_from = {}

    for fname, func in data.functions.items():
        called_from[fname] = set()
        if fname == "":
            continue
        for node in func.sym_data.nodes_reading:
            scope = get_scope_name(node)
            scopes = [scope] if scope else []
            if isinstance(node.scope(), nodes.FunctionDef):
                scopes.append(node.scope().name)

            scope = ".".join(scopes)
            called_from[fname].add(scope)

    module_names = set(data.modules.keys())
    for name in called_from:
        if name == "":
            continue
        called_from[name].update(module_names)

    added_modules = set([""])
    for module in module_names:
        called_from[module] = added_modules.copy()
        added_modules.add(module)

    all_scopes = set(data.functions.keys())
    all_scopes.update(data.symbols.keys())

    # print("called_from")
    # for k, v in called_from.items():
    #     print(f"\t{k}: {v}")

    sorted_scopes = []
    while len(sorted_scopes) < len(all_scopes):
        for scope in all_scopes - set(sorted_scopes):
            if called_from.get(scope, set()).issubset(set(sorted_scopes)):
                sorted_scopes.append(scope)
                break
        else:
            raise RuntimeError("Internal error: cannot sort scopes")

    registers = list(range(16))

    registers_by_scope = {}
    blocked_registers_by_scope = {}

    # tokens = set(" ".join([line.code.split("#")[0] for line in self.code]).split())

    used_symbols = set()

    for line in code:
        if line.output:
            used_symbols.add(line.output)
        for inp in line.inputs:
            if inp.is_register:
                used_symbols.add(
                    inp.code_expr if isinstance(inp, IC10Register) else inp.value
                )

    mapping = {}

    for scope in sorted_scopes:
        if not scope in data.symbols:
            continue
        available_registers = set(registers)
        parent_registers = set()
        for calling_scope in called_from.get(scope, set()):
            parent_registers = parent_registers.union(
                blocked_registers_by_scope.get(calling_scope, set())
            )
        available_registers = list(sorted(set(registers) - parent_registers))
        used_registers = set()
        blocked_registers = set()

        symbols = []
        for symbol in data.symbols[scope].values():
            # if not symbol.code_expr in tokens:
            #     continue
            if symbol.is_register and symbol in used_symbols:
                symbols.append(symbol)

        assign_colors(symbols)
        for sym in symbols:
            if sym.code_expr in mapping:
                sym.code_expr = mapping[sym.code_expr]
                continue

            col = sym._color
            if col == -1:
                raise RuntimeError("Internal error: symbol not colored")
            if col >= len(available_registers):
                raise CompilerError(
                    f"Running out of registers, try to simplify your code."
                )
            reg_num = available_registers[col]
            mapping[sym.code_expr] = f"r{reg_num}"
            sym.code_expr = mapping[sym.code_expr]
            # print('use register', sym.code_expr, 'for', sym.name, 'in scope', scope)
            used_registers.add(reg_num)

            if (
                True or not sym._is_intermediate
            ):  # block all registers for now, this needs more refinement (check if the register is used before and after function calls)
                blocked_registers.add(reg_num)

        registers_by_scope[scope] = used_registers.union(parent_registers)
        blocked_registers_by_scope[scope] = blocked_registers.union(parent_registers)
        # print(f"scope '{scope}' uses registers {registers_by_scope[scope]}")

    for sym in used_symbols:
        if sym.code_expr in mapping:
            sym.code_expr = mapping[sym.code_expr]
        # print("used symbols", [s.name for s in used_symbols if s.is_register])

    # print("mapping", mapping)
    # if mapping:
    #     pattern = re.compile("|".join(re.escape(k) for k in mapping))
    #     replacer = lambda x: mapping[x.group(0)]
    #     for line in self.code:
    #         line.code = pattern.sub(replacer, line.code)

    # for token in tokens:
    #     if token.startswith("__register.") and token not in mapping:
    #         for line in self.code:
    #             if token in line.code:
    #                 raise CompilerError(
    #                     f"Internal error: register {token} not assigned, node: {line.node}"
    #                 )
    #         raise RuntimeError("Internal error: register not assigned: %s" % token)

    used_registers = set()
    for scope in data.symbols:
        used_registers = used_registers.union(registers_by_scope.get(scope, set()))

    return sorted(used_registers)
