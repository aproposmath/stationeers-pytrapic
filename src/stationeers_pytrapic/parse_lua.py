import astroid
from luaparser import ast as lua_ast
from luaparser import astnodes as L


def args_from_node(node: L.Node) -> dict:
    data = {
        "parent": None,
        "lineno": None,
        "col_offset": None,
        "end_lineno": None,
        "end_col_offset": None,
    }
    if node.first_token is not None:
        data["lineno"] = node.first_token.line
        data["col_offset"] = node.first_token.column

    if node.last_token is not None:
        data["end_lineno"] = node.last_token.line
        data["end_col_offset"] = node.last_token.column

    return data


class LuaToAstroid:
    def to_astroid(self, src: str) -> astroid.Module:
        lua_tree = lua_ast.parse(src)
        body = [self.visit_stmt(stmt) for stmt in lua_tree.body.body]
        # Module node
        node = astroid.Module(
            name="lua_module",
        )

        for b in body:
            b.parent = node

        node.postinit(body)
        return node

    def visit_stmt(self, node: L.Node, is_assign_target=False) -> astroid.NodeNG:

        kwargs = args_from_node(node)

        if isinstance(node, L.Index):
            val = self.visit_stmt(node.value)
            if is_assign_target:
                attr = astroid.AssignAttr(node.idx.id, **args_from_node(node))
            else:
                attr = astroid.Attribute(node.idx.id, **args_from_node(node))
            val.parent = attr
            attr.postinit(val)
            return attr

        if isinstance(node, L.TrueExpr):
            return astroid.Const(
                True,
                **kwargs,
            )
        if isinstance(node, L.FalseExpr):
            return astroid.Const(
                False,
                **kwargs,
            )
        if isinstance(node, L.Assign):
            targets = [self.visit_stmt(t, True) for t in node.targets]
            values = [self.visit_stmt(v) for v in node.values]
            node = astroid.Assign(**kwargs)
            for t in targets:
                t.parent = node
            for v in values:
                v.parent = node
            node.postinit(
                targets,
                values[0] if values else astroid.Const(None),
                None,
            )
            return node

        if isinstance(node, L.Call):
            if node.func.id == "require":
                names = [a.s for a in node.args if isinstance(a, L.String)]
                if len(names) != 1:
                    raise NotImplementedError("Multiple imports not supported")
                node = astroid.ImportFrom(
                    names[0],
                    names=[("*", None)],
                    **kwargs,
                )
                return node
            func = self.visit_stmt(node.func)
            args = [self.visit_stmt(a) for a in node.args or []]
            node = astroid.Call(**kwargs)
            node.postinit(func, args, [])
            func.parent = node
            for a in args:
                a.parent = node
            return node

        if isinstance(node, L.While):

            test_node = self.visit_stmt(node.test)
            body = [self.visit_stmt(s) for s in node.body.body]

            node = astroid.While(**kwargs)
            for b in body:
                b.parent = node
            node.postinit(test_node, body, [])
            test_node.parent = node
            return node

        if isinstance(node, L.Function):
            args_node = astroid.Arguments(None, None, None)
            args = [astroid.AssignName(a.id, **args_from_node(a)) for a in node.args]
            for a in args:
                a.parent = args_node
            args_node.postinit(
                args,
                None,
                [],
                None,
                [],
                [],
                [],
                [],
            )
            body = [self.visit_stmt(s) for s in node.body.body]
            node = astroid.FunctionDef(
                name=node.name.id if isinstance(node.name, L.Name) else "anon",
                **kwargs,
            )
            args_node.parent = node
            node.postinit(args_node, body)
            for b in body:
                b.parent = node
            return node

        if isinstance(node, L.Name):
            if is_assign_target:
                return astroid.AssignName(
                    name=node.id,
                    **kwargs,
                )
            return astroid.Name(
                name=node.id,
                **kwargs,
            )
        if isinstance(node, L.Number):
            return astroid.Const(
                node.n,
                **kwargs,
            )
        if isinstance(node, L.String):
            return astroid.Const(
                node.s,
                **kwargs,
            )

        if isinstance(node, L.RelOp):
            op = {
                L.LessThanOp: "<",
                L.LessOrEqThanOp: "<=",
                L.GreaterThanOp: ">",
                L.GreaterOrEqThanOp: ">=",
                L.EqToOp: "==",
                L.NotEqToOp: "!=",
            }.get(type(node), None)

            if op is None:
                raise NotImplementedError(
                    f"Unsupported binary operator: {type(node.op)}"
                )

            left = self.visit_stmt(node.left)
            right = self.visit_stmt(node.right)

            node = astroid.Compare(
                **kwargs,
            )
            node.postinit(left, [(op, right)])
            left.parent = node
            right.parent = node
            return node
        if isinstance(node, L.AriOp):
            op = {
                L.AddOp: "+",
                L.SubOp: "-",
                L.MultOp: "*",
                L.FloatDivOp: "/",
                L.ModOp: "%",
            }.get(type(node), None)
            if op is None:
                raise NotImplementedError(
                    f"Unsupported binary operator: {type(node.op)}"
                )

            left = self.visit_stmt(node.left)
            right = self.visit_stmt(node.right)

            node = astroid.BinOp(
                op,
                **kwargs,
            )
            node.postinit(left, right)
            left.parent = node
            right.parent = node
            return node
        # Fallback
        return astroid.Const(
            None,
            **kwargs,
        )


def parse_lua(src: str) -> astroid.Module:
    conv = LuaToAstroid()
    return conv.to_astroid(src)
