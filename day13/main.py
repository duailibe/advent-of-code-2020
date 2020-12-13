import fileinput


def wait_times(ids, time):
    return [(id_, id_ - (time % id_)) for id_ in ids if id_ != "x"]


def common_time(ids):
    t = step = 1
    for diff, id_ in enumerate(ids):
        if id_ == "x":
            continue
        while ((t + diff) % id_) > 0:
            t += step
        step *= id_
    return t


if __name__ == "__main__":
    lines = list(fileinput.input())
    timestamp = int(lines[0])
    ids = [i if i == "x" else int(i) for i in lines[1].split(",")]

    id_, wait_time = min(wait_times(ids, timestamp), key=lambda k: k[1])
    print(f"Part 1: {id_ * wait_time}")

    print(f"Part 2: {common_time(ids)}")
