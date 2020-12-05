import fileinput


def parse(code):
    row_i = col_i = 0
    row_j = 128
    col_j = 8

    for c in code:
        if c == "F":
            row_j = int((row_i + row_j) / 2)
        elif c == "B":
            row_i = int((row_i + row_j) / 2)
        if c == "L":
            col_j = int((col_i + col_j) / 2)
        if c == "R":
            col_i = int((col_i + col_j) / 2)

    return (row_i, col_i)


def get_id(seat):
    row, column = seat
    return row * 8 + column


if __name__ == "__main__":
    seats = [parse(line.strip()) for line in fileinput.input()]

    ids = set(map(get_id, seats))

    print(f"Part 1: {max(ids)}")

    for row in range(128):
        for column in range(8):
            id_ = get_id((row, column))
            if id_ not in ids:
                print(f"Seat: (row={row}, column={column}, id={id_})")
