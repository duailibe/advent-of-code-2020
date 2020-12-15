def play_until(starting, final):
    mem = {spoken: i for i, spoken in enumerate(starting[:-1], 1)}
    spoken = starting[-1]
    for i in range(len(starting) + 1, final + 1):
        if spoken not in mem:
            mem[spoken] = i - 1
            spoken = 0
        else:
            last = mem[spoken]
            mem[spoken] = i - 1
            spoken = i - 1 - last
    return spoken


if __name__ == "__main__":
    print("Part 1:", play_until([16, 12, 1, 0, 15, 7, 11], 2020))
    print("Part 2:", play_until([16, 12, 1, 0, 15, 7, 11], 30000000))
