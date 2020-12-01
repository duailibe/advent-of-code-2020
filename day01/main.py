import fileinput
import math


def find_pair(entries):
    for num in entries:
        if 2020 - num in entries:
            return (num, 2020 - num)
    raise


def find_three(entries):
    for i in range(len(entries) - 2):
        for j in range(i, len(entries) - 1):
            rest = 2020 - entries[i] - entries[j]
            if rest in entries:
                return (entries[i], entries[j], rest)
    raise


if __name__ == "__main__":
    entries = [int(line.strip()) for line in fileinput.input()]

    pair = find_pair(entries)
    print(f"Part 1: {math.prod(find_pair(entries))}")

    three = find_three(entries)
    print(f"Part 2: {math.prod(find_three(entries))}")
