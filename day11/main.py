import fileinput
import itertools

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


class SeatMap:
    def __init__(self, seatmap):
        self.seatmap = seatmap

    def __contains__(self, coord):
        return (
            isinstance(coord, tuple)
            and 0 <= coord[1] < len(self.seatmap)
            and 0 <= coord[0] < len(self.seatmap[0])
        )

    def __getitem__(self, coord):
        x, y = coord
        if 0 <= y < len(self.seatmap) and 0 <= x < len(self.seatmap[0]):
            return self.seatmap[y][x]
        raise KeyError(coord)

    @property
    def occupied(self):
        return sum(seat == "#" for seat in itertools.chain(*self.seatmap))

    def update(self, updater):
        return SeatMap(
            [
                [updater(self, (x, y)) for x in range(len(self.seatmap[0]))]
                for y in range(len(self.seatmap))
            ]
        )


def update_by_adjacents(seatmap, xy):
    seat = seatmap[xy]
    if seat == ".":
        return seat

    x, y = xy
    occupied_adjacents = sum(
        seatmap[x + dx, y + dy] == "#"
        for dx, dy in DIRECTIONS
        if (x + dx, y + dy) in seatmap
    )
    if seat == "L" and occupied_adjacents == 0:
        return "#"
    if seat == "#" and occupied_adjacents >= 4:
        return "L"
    return seat


def update_by_visibility(seatmap, xy):
    def visible():
        x, y = xy
        for dx, dy in DIRECTIONS:
            step = 1
            while (xy_ := (x + step * dx, y + step * dy)) in seatmap:
                if seatmap[xy_] != ".":
                    yield xy_
                    break
                step += 1

    seat = seatmap[xy]
    if seat == ".":
        return seat

    occupied_visible = sum(seatmap[xy] == "#" for xy in visible())
    if seat == "L" and occupied_visible == 0:
        return "#"
    if seat == "#" and occupied_visible >= 5:
        return "L"
    return seat


def run(updater, seatmap):
    occupied = -1
    while occupied != (occupied := seatmap.occupied):
        seatmap = seatmap.update(updater)

    return occupied


if __name__ == "__main__":
    seatmap = SeatMap([list(l.strip()) for l in fileinput.input()])

    print(f"Part 1: {run(update_by_adjacents, seatmap)}")
    print(f"Part 2: {run(update_by_visibility, seatmap)}")
