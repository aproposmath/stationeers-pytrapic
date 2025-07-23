import logging

import astroid

logger = logging.getLogger("stationeers_pytrapic")


def is_constant(node):
    if isinstance(node, (int, float, str)):
        return True, node

    if isinstance(node, astroid.Const):
        return True, node.value
    try:
        inferred = node.inferred()
    except Exception:
        return False, None

    res = len(inferred) == 1 and isinstance(inferred[0], astroid.Const)
    if res:
        return True, inferred[0].value
    else:
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
