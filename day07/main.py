import fileinput
import re
from collections import defaultdict


def find_all_outer(rules, start):
    lookup = defaultdict(list)
    for rule in rules:
        outer, contained = rule.split(" bags contain ")
        for color in re.findall(r"\d (.*?) bag", contained):
            lookup[color].append(outer)

    def get_outer(color):
        outer = set(lookup[color])
        for container in lookup[color]:
            outer |= get_outer(container)
        return outer

    return get_outer(start)


def sum_all_inner(lookup, start):
    lookup = {}
    for rule in rules:
        outer, contained = rule.split(" bags contain ")
        lookup[outer] = re.findall(r"(\d) (.*?) bag", contained)

    def sum_inner(color):
        return sum(int(n) + int(n) * sum_inner(inner) for (n, inner) in lookup[color])

    return sum_inner(start)


if __name__ == "__main__":
    rules = [l.strip() for l in fileinput.input()]

    print(f"Part 1: {len(find_all_outer(rules, 'shiny gold'))}")
    print(f"Part 2: {sum_all_inner(rules, 'shiny gold')}")
