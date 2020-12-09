import fileinput


def invalid_preamble(numbers):
    preamble = set(numbers[:25])
    for n, number in enumerate(numbers[25:]):
        if n > 0:
            preamble.remove(numbers[n - 1])
            preamble.add(numbers[n + 24])
        if not any((number - k) in preamble for k in preamble):
            return number
    raise


def find_sum_set(numbers, number):
    for i in range(len(numbers) - 1):
        sum_ = numbers[i]
        for j in range(i + 1, len(numbers)):
            sum_ += numbers[j]
            if sum_ == number:
                return numbers[i : j + 1]
    raise


if __name__ == "__main__":
    numbers = [int(i) for i in fileinput.input()]

    invalid = invalid_preamble(numbers)
    print(f"Part 1: {invalid}")

    sum_set = find_sum_set(numbers, invalid)
    print(f"Part 2: {min(sum_set) + max(sum_set)}")
