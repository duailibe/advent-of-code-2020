import fileinput
import math

DIRECTIONS = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}


def move(pos, direction, units):
    dx, dy = direction
    return (int(pos[0] + dx * units), int(pos[1] + dy * units))


def rotate(xy, angle):
    rad = math.radians(angle)
    x, y = xy
    return (
        round(x * math.cos(rad) - y * math.sin(rad)),
        round(x * math.sin(rad) + y * math.cos(rad)),
    )


def navigate(instructions):
    pos = (0, 0)
    direction = (1, 0)
    for action, units in instructions:
        if action in DIRECTIONS:
            pos = move(pos, DIRECTIONS[action], units)
        elif action == "F":
            pos = move(pos, direction, units)
        elif action in ("L", "R"):
            direction = rotate(direction, units * (-1 if action == "R" else 1))
    return pos


def navigate_waypoint(instructions):
    pos = (0, 0)
    waypoint = (10, 1)
    for action, units in instructions:
        if action in DIRECTIONS:
            waypoint = move(waypoint, DIRECTIONS[action], units)
        elif action == "F":
            pos = move(pos, waypoint, units)
        elif action in ("L", "R"):
            waypoint = rotate(waypoint, units * (-1 if action == "R" else 1))
    return pos


if __name__ == "__main__":
    instructions = [(line[0], int(line[1:])) for line in fileinput.input()]

    pos = navigate(instructions)
    print(f"Part 1: {abs(pos[0]) + abs(pos[1])}")

    pos = navigate_waypoint(instructions)
    print(f"Part 2: {abs(pos[0]) + abs(pos[1])}")
