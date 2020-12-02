import fileinput
import re


def old_valid(line):
    min_, max_, letter, password = re.split(r"[ \-:]+", line)
    return int(min_) <= password.count(letter) <= int(max_)


def new_valid(line):
    i, j, letter, password = re.split(r"[ \-:]+", line)
    return (password[int(i) - 1] == letter) ^ (password[int(j) - 1] == letter)


if __name__ == "__main__":
    lines = list(fileinput.input())

    print(f"Part 1: {sum(map(old_valid, lines))}")
    print(f"Part 2: {sum(map(new_valid, lines))}")
