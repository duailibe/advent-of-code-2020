import fileinput


def play_regular(player1, player2):
    while player1 and player2:
        n1, n2 = player1.pop(0), player2.pop(0)

        if n1 > n2:
            player1.extend([n1, n2])
        else:
            player2.extend([n2, n1])

    return player1, player2


def play_recursive(player1, player2):
    rounds = set()
    while player1 and player2:
        r = (tuple(player1), tuple(player2))
        if r in rounds:
            return player1, 0

        rounds.add(r)

        n1, n2 = player1.pop(0), player2.pop(0)

        if n1 <= len(player1) and n2 <= len(player2):
            result = play_recursive(player1[:n1], player2[:n2])
            player1_won = bool(result[0])
        else:
            player1_won = n1 > n2

        if player1_won:
            player1.extend([n1, n2])
        else:
            player2.extend([n2, n1])

    return player1, player2


def score(cards):
    return sum(card * i for i, card in enumerate(cards[::-1], 1))


if __name__ == "__main__":
    player1, player2 = [
        list(map(int, lines.splitlines()[1:]))
        for lines in "".join(fileinput.input()).split("\n\n")
    ]

    winner = next(filter(None, play_regular(player1[:], player2[:])))
    print("Part 1:", score(winner))

    winner = next(filter(None, play_recursive(player1[:], player2[:])))
    print("Part 2:", score(winner))
