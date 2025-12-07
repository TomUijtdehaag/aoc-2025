import re
from pathlib import Path


def parse(path: str):
    ranges = []
    for r in Path(path).read_text().split(","):
        ranges.append([int(i) for i in r.split("-")])

    return ranges


def p(ranges: list[list[int]], p2=False):
    invalids = []

    for start, end in ranges:
        for identifier in range(start, end + 1):
            if not p2 and re.match(r"^(\d+)\1$", str(identifier)):
                invalids.append(identifier)

            if p2 and re.match(r"^(\d+)\1+$", str(identifier)):
                invalids.append(identifier)

    return sum(invalids)


if __name__ == "__main__":
    ranges = parse("d02/input.txt")
    print(p(ranges))
    print(p(ranges, True))
