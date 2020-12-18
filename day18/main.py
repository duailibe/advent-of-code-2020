import fileinput
import operator
import re


def parse(line):
    tokens = re.findall(r"\d+|[+*()]", line)
    expr = []
    q = []
    for token in tokens:
        if token.isdigit():
            expr.append(int(token))
        if token == "+":
            expr.append(operator.add)
        if token == "*":
            expr.append(operator.mul)
        if token == "(":
            inner = []
            expr.append(inner)
            q.append(expr)
            expr = inner
        if token == ")":
            expr = q.pop()
    return expr


def eval_no_precedence(expr):
    if isinstance(expr, int):
        return expr

    if len(expr) == 1:
        return eval_no_precedence(expr[0])

    lhs, op, rhs = expr[:3]
    lhs = eval_no_precedence(lhs)
    rhs = eval_no_precedence(rhs)

    return eval_no_precedence([op(lhs, rhs)] + expr[3:])


def eval_precedence(expr):
    if isinstance(expr, int):
        return expr

    if len(expr) == 1:
        return eval_no_precedence(expr[0])

    while operator.add in expr:
        i = expr.index(operator.add)
        expr[i - 1 : i + 2] = [
            eval_precedence(expr[i - 1]) + eval_precedence(expr[i + 1])
        ]

    res = eval_precedence(expr[0])
    for el in expr[1:]:
        if el == operator.mul:
            continue
        res *= eval_precedence(el)
    return res


if __name__ == "__main__":
    exprs = [parse(l) for l in fileinput.input()]

    print("Part 1:", sum(map(eval_no_precedence, exprs)))
    print("Part 2:", sum(map(eval_precedence, exprs)))
