import fileinput


def count_any(group):
    return len(set().union(*map(set, group)))


def count_every(group):
    return len(set(group[0]).intersection(*map(set, group[1:])))



if __name__ == "__main__":
    groups = [group.split() for group in "".join(fileinput.input()).split("\n\n")]

    print(f"Part 1: {sum(1 for _ in filter(count_any, groups))}")
    print(f"Part 2: {sum(1 for _ in filter(count_every, groups))}")
