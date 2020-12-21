import fileinput
import re


def find_possible_allergens(foods):
    contains = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen in contains:
                contains[allergen] &= set(ingredients)
            else:
                contains[allergen] = set(ingredients)

    return contains


def match_allergens(candidates):
    match = {}
    while candidates:
        exact = [(list(ing)[0], al) for al, ing in candidates.items() if len(ing) == 1]
        match.update(exact)
        for ing, al in exact:
            del candidates[al]
            for k in candidates:
                if ing in candidates[k]:
                    candidates[k].remove(ing)
    return match


if __name__ == "__main__":

    def parse(line):
        words = re.findall(r"(\w+)", line)
        i = words.index("contains")
        return words[:i], words[i + 1 :]

    foods = list(map(parse, fileinput.input()))

    allergen_candidates = find_possible_allergens(foods)
    has_allergens = set().union(*allergen_candidates.values())
    print(
        "Part 1:",
        sum(len(set(ingredients) - has_allergens) for ingredients, _ in foods),
    )

    print(
        "Part 2:",
        ",".join(
            i[0]
            for i in sorted(
                match_allergens(allergen_candidates).items(), key=lambda i: i[1]
            )
        ),
    )
