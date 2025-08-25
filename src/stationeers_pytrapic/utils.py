import logging

import astroid

logger = logging.getLogger("stationeers_pytrapic")


def is_builtin_name(name: str) -> bool:
    from . import symbols

    return name in symbols.__dict__


def is_structure(val):
    from . import symbols, types

    return isinstance(
        val,
        (
            symbols.GenericStructures,
            symbols.GenericStructure,
            types._BaseStructure,
            types._BaseStructures,
        ),
    )


def is_constant(node):
    if isinstance(node, (int, float, str)):
        return True, node

    if isinstance(node, astroid.Const):
        return True, node.value

    if isinstance(node, astroid.Call):
        if node.func.name == "HASH":
            from . import symbols

            return True, symbols.HASH(node.args[0].value)
        else:
            return False, None

    try:
        inferred = node.inferred()
    except Exception:
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
