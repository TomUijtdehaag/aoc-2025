from functools import reduce
from pathlib import Path


def parse(path: str):
    lines = Path(path).read_text().splitlines()

    numbers = []
    for line in lines[:-1]:
        numbers.append([int(number) for number in line.split()])

    numbers = list(zip(*numbers))
    operators = lines[-1].split()

    return zip(numbers, operators)


def parse2(path: str):
    lines = Path(path).read_text().splitlines()
    width = len(lines[0])

    nlines = lines[:-1]

    numbers = []

    nums = []
    for col in range(width):
        num = "".join([l[col] for l in nlines]).strip()

        if not num:
            numbers.append(nums)
            nums = []

        else:
            nums.append(int(num))
    else:
        numbers.append(nums)

    operators = lines[-1].split()

    return zip(numbers, operators)


def p(problems):
    total = 0

    for numbers, operator in problems:
        total += reduce(lambda x, y: eval(f"{x} {operator} {y}"), numbers)

    return total


problems = parse("d06/input.txt")
print(p(problems))
problems = parse2("d06/input.txt")
print(p(problems))
