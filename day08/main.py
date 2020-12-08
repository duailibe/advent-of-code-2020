import fileinput


class InfiniteLoopError(Exception):
    def __init__(self, accumulator):
        self.accumulator = accumulator
        self.message = "Infinite loop detected!"


def exec(instructions):
    hst = set()
    curr = 0
    acc = 0

    while curr < len(instructions):
        if curr in hst:
            raise InfiniteLoopError(acc)
        hst.add(curr)
        cmd, arg = instructions[curr]

        if cmd == "jmp":
            curr += arg
        else:
            curr += 1
            if cmd == "acc":
                acc += arg

    return acc


def fix(instructions):
    for i, (cmd, arg) in enumerate(instructions):
        if cmd not in ("nop", "jmp"):
            continue
        try:
            copy = instructions[:]
            copy[i] = ("jmp" if cmd == "nop" else "nop", arg)
            return exec(copy)
        except InfiniteLoopError:
            pass


if __name__ == "__main__":

    def parse(line):
        cmd, arg = line.split()
        return (cmd, int(arg))

    instructions = [parse(l) for l in fileinput.input()]

    try:
        exec(instructions)
    except InfiniteLoopError as e:
        print(f"Part 1: {e.accumulator}")

    print(f"Part 2: {fix(instructions)}")
