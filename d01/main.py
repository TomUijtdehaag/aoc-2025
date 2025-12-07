from pathlib import Path


def parse(path):
    return Path(path).read_text().splitlines()


def p(moves: list[str], p2: bool = False):
    ans = 0

    pos = 50
    for move in moves:
        d, a = -1 if move[0] == "L" else 1, int(move[1:])
        positions = [p % 100 for p in range(pos, pos + d * (a + 1), d)][1:]

        pos = positions[-1]

        if not p2:
            ans += positions[-1] == 0

        if p2:
            ans += sum([p == 0 for p in positions])

    return ans


if __name__ == "__main__":
    moves = parse("d01/input.txt")
    a1 = p(moves)
    print("p1:", a1)
    a2 = p(moves, p2=True)
    print("p2", a2)
