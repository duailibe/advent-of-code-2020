import fileinput
import re


def make_regex(rules, r, depth=1000):
    # depth is to prevent infinite recursion
    if depth == 0:
        return ""
    if len(rules[r]) == 1 and len(rules[r][0]) == 1 and rules[r][0][0].startswith('"'):
        return rules[r][0][0][1]
    return (
        "("
        + "|".join(
            "".join(make_regex(rules, s, depth - 1) for s in group)
            for group in rules[r]
        )
        + ")"
    )


if __name__ == "__main__":

    def parse_rule(line):
        r_id, r = line.split(": ")
        return r_id, [sub.split() for sub in r.split(" | ")]

    rules_lines, messages_lines = "".join(fileinput.input()).split("\n\n")
    rules = dict(map(parse_rule, rules_lines.splitlines()))
    messages = messages_lines.splitlines()

    pattern = re.compile(make_regex(rules, "0"))
    print("Part 1:", sum(map(lambda msg: bool(pattern.fullmatch(msg)), messages)))

    # Part 2
    rules.update([parse_rule("8: 42 | 42 8"), parse_rule("11: 42 31 | 42 11 31")])

    pattern = re.compile(make_regex(rules, "0", max(map(len, messages))))
    print("Part 2:", sum(map(lambda msg: bool(pattern.fullmatch(msg)), messages)))
