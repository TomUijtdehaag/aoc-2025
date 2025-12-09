from pathlib import Path


def parse(path):
    return Path(path).read_text().splitlines()


DIRS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def neighbours(x: int, y: int, height: int, width: int) -> list[tuple[int, int]]:
    n = []

    for dx, dy in DIRS:
        xx = x + dx
        yy = y + dy
        if (xx in range(width)) and (yy in range(height)):
            n.append((xx, yy))

    return n


def removable(grid: list[str]) -> list[tuple[int, int]]:
    height = len(grid)
    width = len(grid[0])

    removes = []

    for y, line in enumerate(grid):
        for x, pos in enumerate(line):
            if pos == "@":
                ns = neighbours(x, y, height, width)

                nns = 0
                for xx, yy in ns:
                    nn = grid[yy][xx]
                    if nn == "@":
                        nns += 1

                if nns < 4:
                    removes.append((x, y))

    return removes


def update(grid: list[str], remove: list[tuple[int, int]]) -> list[str]:
    new_grid = []

    for y, line in enumerate(grid):
        new_line = ""
        for x, pos in enumerate(line):
            if (x, y) in remove:
                new_line += "x"
            else:
                new_line += pos

        new_grid.append(new_line)

    return new_grid


def p1(grid: list[str]) -> int:
    return len(removable(grid))


def p2(grid: list[str]) -> int:
    total = 0

    while True:
        remove = removable(grid)
        if len(remove) == 0:
            break
        total += len(remove)
        grid = update(grid, remove)

    return total


grid = parse("d04/input.txt")
print(p1(grid))
print(p2(grid))
