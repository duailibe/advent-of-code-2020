import fileinput
import itertools
import re


def bitmask(value, bit, n):
    if bit == "0":
        return value & ~(1 << n)
    return value | (1 << n)


def exec_mask_value(instructions):
    def apply_mask(mask, value):
        for i in range(len(mask) - 1, -1, -1):
            n = len(mask) - i - 1
            if mask[i] in ("0", "1"):
                value = bitmask(value, mask[i], n)
        return value

    mem = {}
    mask = "X" * 36
    for instr, address, value in instructions:
        if instr == "mask":
            mask = value
        elif instr == "mem":
            mem[address] = apply_mask(mask, value)
    return mem


def exec_mask_addresses(instructions):
    def addresses(mask, address):
        xs = mask.count("X")
        for combination in itertools.product("01", repeat=xs):
            addr = address
            combination = iter(combination)
            for i in range(len(mask) - 1, -1, -1):
                n = len(mask) - i - 1
                if mask[i] == "1":
                    addr = bitmask(addr, "1", n)
                elif mask[i] == "X":
                    bit = next(combination)
                    addr = bitmask(addr, bit, n)
            yield addr

    mem = {}
    mask = "0" * 36
    for instr, address, value in instructions:
        if instr == "mask":
            mask = value
        elif instr == "mem":
            for address in addresses(mask, address):
                mem[address] = value
    return mem


if __name__ == "__main__":

    def parse_instr(line):
        instr = line.split(" = ")
        if instr[0] == "mask":
            return ("mask", None, instr[1])
        else:
            address, value = re.findall(r"^mem\[(\d+)] = (\d+)$", line)[0]
            return ("mem", int(address), int(value))

    instructions = [parse_instr(l.strip()) for l in fileinput.input()]

    mem = exec_mask_value(instructions)
    print(f"Part 1: {sum(mem.values())}")

    mem = exec_mask_addresses(instructions)
    print(f"Part 2: {sum(mem.values())}")
