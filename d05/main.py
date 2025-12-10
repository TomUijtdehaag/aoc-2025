from pathlib import Path


def parse(path: str) -> tuple[list[range], list[int]]:
    fresh, available = Path(path).read_text().split("\n\n")

    fresh_ranges = []
    for r in fresh.splitlines():
        s, e = r.split("-")
        fresh_ranges.append((int(s), int(e)))

    available = [int(a) for a in available.splitlines()]

    return fresh_ranges, available


def p1(fresh_ranges: list[range], available: list[int]) -> int:
    t = 0
    for a in available:
        if any(a in range(*r) for r in fresh_ranges):
            t += 1

    return t


def p2(fresh_ranges: list[range]) -> int:
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])

    sm, em = sorted_ranges[0]
    total = 0

    for s, e in sorted_ranges[1:]:
        if s > (em + 1):
            total += em - sm + 1
            sm, em = s, e
        else:
            em = max(em, e)

    total += em - sm + 1
    return total


fresh_ranges, available = parse("d05/input.txt")
print(p1(fresh_ranges, available))
print(p2(fresh_ranges))
