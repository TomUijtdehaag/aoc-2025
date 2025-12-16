import math
from functools import reduce
from math import dist
from pathlib import Path
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int
    z: int


def parse(path: str) -> list[Point]:
    lines = Path(path).read_text().splitlines()

    points = []

    for line in lines:
        x, y, z = line.split(",")
        points.append(Point(int(x), int(y), int(z)))

    return points


def euclidean_dist(p1: Point, p2: Point) -> float:
    return math.sqrt(sum((d1 - d2) ** 2 for d1, d2 in zip(p1, p2)))


def find_circuit(i: int, circuits: dict[int, set[int]]) -> int:
    for j, circuit in circuits.items():
        if i in circuit:
            return j

    raise ValueError(f"{i} not found")


def solve(points: list[Point], merges=0):
    distances = {}
    for a in range(len(points)):
        for b in range(a + 1, len(points)):
            distances[(a, b)] = dist(points[a], points[b])

    distances = dict(sorted(distances.items(), key=lambda x: x[1]))
    circuits = {i: {i} for i in range(len(points))}

    n_merged = 0
    for (ia, ib), d in list(distances.items()):
        if merges and n_merged == merges:
            circuits = dict(
                sorted(circuits.items(), key=lambda x: len(x[1]), reverse=True)
            )
            return reduce(lambda a, b: a * b, [len(v) for v in circuits.values()][:3])

        a = find_circuit(ia, circuits)
        b = find_circuit(ib, circuits)

        n_merged += 1

        if a == b:
            continue

        circuits[a] |= circuits.pop(b)

        if len(circuits) == 1:
            return points[ia].x * points[ib].x


points = parse("d08/input.txt")
print(solve(points, 1000))
print(solve(points))
