import fileinput
import re

REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def parse(lines):
    record = {}
    for line in lines:
        if not line.strip():
            yield record
            record = {}
            continue

        record.update([tuple(field.split(":")) for field in line.split()])

    # off-by-one!
    yield record


def required(passport):
    return all(attr in passport for attr in REQUIRED)


def validate(passport):
    try:
        assert 1920 <= int(passport["byr"]) <= 2002
        assert 2010 <= int(passport["iyr"]) <= 2020
        assert 2020 <= int(passport["eyr"]) <= 2030

        if passport["hgt"][-2:] == "cm":
            assert 150 <= int(passport["hgt"][:3]) <= 193
        elif passport["hgt"][-2:] == "in":
            assert 59 <= int(passport["hgt"][:2]) <= 76
        else:
            return False

        assert re.match(r"^#[a-z0-9]{6}$", passport["hcl"])

        assert passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        assert re.match(r"^[0-9]{9}$", passport["pid"])

        return True
    except (AssertionError, ValueError):
        return False


if __name__ == "__main__":
    lines = list(fileinput.input())

    passports = list(filter(required, parse(lines)))
    print(f"Part 1: {sum(map(required, parse(lines)))}")

    valid = list(filter(validate, passports))
    print(f"Part 2: {len(valid)}")
