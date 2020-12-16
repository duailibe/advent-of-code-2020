import fileinput
import itertools
import math


def in_range(value, ranges):
    return any(lo <= value <= hi for (lo, hi) in ranges)


def invalid_values(rules, ticket):
    return [
        value
        for value in ticket
        if not in_range(value, itertools.chain(*[r[1] for r in rules]))
    ]


def fields_order(rules, tickets):
    fields = [None] * len(rules)
    q = list(range(len(tickets[0])))
    while q:
        idx = q.pop()
        candidates = [
            field
            for field, ranges in rules
            if field not in fields
            and all(in_range(ticket[idx], ranges) for ticket in tickets)
        ]
        candidates = [
            field
            for field, ranges in rules
            if field not in fields
            and all(in_range(ticket[idx], ranges) for ticket in tickets)
        ]
        if len(candidates) == 1:
            fields[idx] = candidates[0]
        else:
            q.insert(0, idx)
    return fields


if __name__ == "__main__":

    def parse_rule(line):
        field, rule = line.split(": ")
        return field, [tuple(map(int, r.split("-"))) for r in rule.split(" or ")]

    rules_lines, my_ticket_lines, nearby_lines = "".join(fileinput.input()).split(
        "\n\n"
    )

    rules = [parse_rule(line.strip()) for line in rules_lines.splitlines()]
    my_ticket = tuple(map(int, my_ticket_lines.splitlines()[1].split(",")))
    nearby = [
        tuple(map(int, line.split(","))) for line in nearby_lines.splitlines()[1:]
    ]

    print(
        "Part 1:",
        sum(value for ticket in nearby for value in invalid_values(rules, ticket)),
    )

    valid = [ticket for ticket in nearby if not list(invalid_values(rules, ticket))]
    fields = fields_order(rules, valid + [my_ticket])
    print(
        "Part 2:",
        math.prod(
            my_ticket[i]
            for i, field in enumerate(fields)
            if field.startswith("departure")
        ),
    )
