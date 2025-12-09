from pathlib import Path


def parse(path):
    return Path(path).read_text().splitlines()


def max_joltage(bank: str, n: int):
    joltages = [int(d) for d in bank]

    left_bound = 0
    right_bound = len(joltages) + 1
    picks = []

    for d in range(n):
        to_consider = joltages[left_bound : right_bound - (n - d)]
        pick = max(to_consider)
        picks.append(str(pick))

        idx = to_consider.index(pick)
        left_bound = left_bound + idx + 1

    return int("".join(picks))


def p(banks: list[str], n: int) -> int:
    out = []
    for bank in banks:
        out.append(max_joltage(bank, n))

    return sum(out)


if __name__ == "__main__":
    banks = parse("d03/input.txt")
    print(p(banks, 2))
    print(p(banks, 12))
