import fileinput
import itertools
from collections import defaultdict


def neighbors(point):
    n = len(point)
    for delta in itertools.product((-1, 0, 1), repeat=n):
        if not any(delta):
            continue
        yield tuple(x + dx for x, dx in zip(point, delta))


def traverse(space):
    return {p for p in itertools.chain(*map(neighbors, space.keys()))}


def run_until(space, n):
    def update(space):
        new_space = defaultdict(bool)
        for p in traverse(space):
            active_neighbors = sum(space[n] for n in neighbors(p))
            if space[p]:
                new_space[p] = active_neighbors in (2, 3)
            else:
                new_space[p] = active_neighbors == 3
        return new_space

    for _ in range(n):
        space = update(space)

    return space


if __name__ == "__main__":
    lines = "".join(fileinput.input()).splitlines()

    space = defaultdict(bool)
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            space[(x, y, 0)] = value == "#"

    print("Part 1:", sum(run_until(space, 6).values()))

    space_4d = defaultdict(bool)
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            space_4d[(x, y, 0, 0)] = value == "#"

    print("Part 2:", sum(run_until(space_4d, 6).values()))
