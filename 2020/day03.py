"""
https://adventofcode.com/2020/day/3
"""
from math import prod

def main():
    with open("inputs\day03p.txt") as f:
        plines = [line.strip() for line in f.readlines()]

    with open("inputs\day03.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part 1:")
    print(p1(plines))
    print(p1(lines))
    print("Part 2:")
    print(p2(plines))
    print(p2(lines))

def p1(grid):
    r = c = total = 0
    while r < len(grid):
        if grid[r][c % len(grid[0])] == "#":
            total += 1
        r += 1
        c += 3

    return total

def p2(grid):
    totals = []
    for dr, dc in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        r = c = total = 0
        while r < len(grid):
            if grid[r][c % len(grid[0])] == "#":
                total += 1
            r += dr
            c += dc

        totals.append(total)

    return prod(totals)

main()