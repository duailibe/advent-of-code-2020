import itertools
import fileinput


def count_all_diffs(jolts):
    counts = [0, 0, 0]
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i - 1]
        counts[diff - 1] += 1
    return counts


def count_possibilities(jolts):
    possibilities = [0] * len(jolts)

    def combinations(i):
        if possibilities[i]:
            return possibilities[i]

        if i == len(jolts) - 1:
            return 1

        possibilities[i] = sum(
            map(
                combinations,
                itertools.takewhile(
                    lambda j: jolts[j] - jolts[i] <= 3, range(i + 1, len(jolts))
                ),
            )
        )
        return possibilities[i]

    return combinations(0)


if __name__ == "__main__":
    jolts = sorted(int(i) for i in fileinput.input())
    jolts = [0] + jolts + [jolts[-1] + 3]

    diff1, _, diff3 = count_all_diffs(jolts)
    print(f"Part 1: {diff1 * diff3}")

    print(f"Part 2: {count_possibilities(jolts)}")
