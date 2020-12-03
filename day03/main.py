import fileinput


def traverse(lines, slope):
    w = len(lines[0])
    dx, dy = slope
    x, y = (0, 0)
    while y < len(lines):
        yield (x, y)
        x, y = ((x + dx) % w, y + dy)


def trees(lines, slope):
    return sum(
        lines[y][x] == "#"
        for x, y in traverse(lines, slope)
    )


if __name__ == "__main__":
    lines = "".join(fileinput.input()).split()

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    p = 1
    for slope in slopes:
        n = trees(lines, slope)
        if slope == (3, 1):
            print(f"Part 1: {n} trees")
        p = p * n

    print(f"Part 2: {p}")
