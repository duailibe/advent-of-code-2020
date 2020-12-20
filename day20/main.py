import fileinput
import itertools
import math

MONSTER = """\
                  #
#    ##    ##    ###
 #  #  #  #  #  # """


def border(tile, side):
    """Return one of the borders of a tile

    side: maybe one of 'top', 'bottom', 'left', 'right'"""

    if side == "top":
        return tile[0]
    if side == "bottom":
        return tile[-1]
    if side == "left":
        return "".join(line[0] for line in tile)
    if side == "right":
        return "".join(line[-1] for line in tile)

    raise ValueError(f"{side} is invalid")


def all_borders(tile):
    for side in ["top", "bottom", "left", "right"]:
        b = border(tile, side)
        yield b
        yield b[::-1]


def neighbors(tiles, tid):
    borders = list(all_borders(tiles[tid]))
    for oid in tiles:
        if oid != tid and any(
            b1 == b2 for b1, b2 in itertools.product(borders, all_borders(tiles[oid]))
        ):
            yield oid


def corner_ids(tiles):
    # corner tiles must match exactly two other tiles
    for tid in tiles:
        if len(list(neighbors(tiles, tid))) == 2:
            yield tid


def rotate(tile):
    return ["".join(r) for r in zip(*tile[::-1])]


def flip(tile):
    return tile[::-1]


def orientations(tile):
    for _ in range(4):
        tile = rotate(tile)
        yield tile

    tile = flip(tile)
    for _ in range(4):
        tile = rotate(tile)
        yield tile


def get_grid(tiles):
    ntiles = int(math.sqrt(len(tiles)))
    gridmap = {}
    available = set(tiles)

    for x, y in itertools.product(range(ntiles), repeat=2):
        if x == 0 and y == 0:
            tid = next(corner_ids(tiles))
            tile = tiles[tid]
            nbs = set(
                itertools.chain(
                    *[all_borders(tiles[nid]) for nid in neighbors(tiles, tid)]
                )
            )

            while border(tile, "bottom") not in nbs or border(tile, "right") not in nbs:
                tile = rotate(tile)

            gridmap[0, 0] = tile
            available.remove(tid)
        else:
            ref = (
                border(gridmap[x - 1, y], "right")
                if x > 0
                else border(gridmap[0, y - 1], "bottom")
            )
            test = "left" if x > 0 else "top"
            for tid, tile in (
                (tid, tile) for tid in available for tile in orientations(tiles[tid])
            ):
                if border(tile, test) == ref:
                    gridmap[x, y] = tile
                    available.remove(tid)
                    break
            else:
                raise RuntimeError(f"no tile found for {(x, y)}")

    return [
        "".join(gridmap[x, y][i][1:-1] for x in range(ntiles))
        for y in range(ntiles)
        for i in range(1, len(gridmap[0, 0]) - 1)
    ]


def find_monster(grid):

    pattern = [
        (r, c)
        for r, line in enumerate(MONSTER.splitlines())
        for c, char in enumerate(line)
        if char == "#"
    ]

    def find(grid):
        return sum(
            all(
                r + dr < len(grid)
                and c + dc < len(grid[0])
                and grid[r + dr][c + dc] == "#"
                for dr, dc in pattern
            )
            for r in range(len(grid))
            for c in range(len(grid[0]))
        )

    n = 0
    for grid in orientations(grid):
        n += find(grid)
    return n


if __name__ == "__main__":

    def get_tiles(lines):
        lines = lines.splitlines()
        tile_id = lines[0][5:-1]
        return tile_id, lines[1:]

    tiles = dict(map(get_tiles, "".join(fileinput.input()).split("\n\n")))

    print("Part 1:", math.prod(map(int, corner_ids(tiles))))

    grid = get_grid(tiles)
    monsters = find_monster(grid)
    print("Part 2:", "".join(grid).count("#") - MONSTER.count("#") * monsters)
