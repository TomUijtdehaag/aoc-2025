from __future__ import annotations

from pathlib import Path

lines = Path("d07/input.txt").read_text().splitlines()

s = lines[0].index("S")

up = {s}
splitters = 0
beams = {s: 1}

for y, l in enumerate(lines[1:]):
    for x, c in enumerate(l):
        if c == "^":
            if x in up:
                splitters += 1
                up.add(x - 1)
                up.add(x + 1)
                up.remove(x)

            b = beams.pop(x, 0)
            if b:
                beams[x - 1] = beams.get(x - 1, 0) + b
                beams[x + 1] = beams.get(x + 1, 0) + b

print(splitters)
print(sum(beams.values()))
