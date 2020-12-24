import fileinput
import re
from collections import defaultdict

DIRECTIONS = {
    "e": (1, -1, 0),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w": (-1, 1, 0),
    "nw": (0, 1, -1),
    "ne": (1, 0, -1),
}


def walk(instructions):
    x = y = z = 0
    for d in instructions:
        dx, dy, dz = DIRECTIONS[d]
        x += dx
        y += dy
        z += dz
    return x, y, z


def neighbors(pos):
    x, y, z = pos
    return ((x + dx, y + dy, z + dz) for dx, dy, dz in DIRECTIONS.values())


def flip_instr(grid, tiles_instr):
    for instructions in tiles_instr:
        pos = walk(instructions)
        grid[pos] = not grid[pos]
    return grid


def flip_day(grid):
    relevant_tiles = set(filter(bool, grid.keys()))
    relevant_tiles.update(*map(neighbors, relevant_tiles))
    updates = {}
    for tile in relevant_tiles:
        bn = sum(grid[n] for n in neighbors(tile))
        if grid[tile] and (bn == 0 or bn > 2):
            updates[tile] = False
        if not grid[tile] and bn == 2:
            updates[tile] = True
    grid.update(updates)
    return grid


if __name__ == "__main__":
    pattern = re.compile(r"(e|se|sw|w|nw|ne)")
    tiles_instr = [pattern.findall(l) for l in fileinput.input()]

    grid = defaultdict(bool)
    flip_instr(grid, tiles_instr)
    print("Part 1:", sum(grid.values()))

    for d in range(100):
        grid = flip_day(grid)

    print(f"Part 2:", sum(grid.values()))
