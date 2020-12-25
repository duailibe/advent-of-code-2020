def transform(subject, n):
    return pow(subject, n) % 20201227


def reverse_loop(pkey, subject):
    n = 0
    value = 1
    while value != pkey:
        value = (value * subject) % 20201227
        n += 1
    return n


if __name__ == "__main__":
    # Test
    # pkeys = (5764801, 17807724)
    pkeys = (15335876, 15086442)

    print("Result:", transform(pkeys[1], reverse_loop(pkeys[0], 7)))
