"""
https://adventofcode.com/2023/day/11
"""
import numpy as np

def main():
    with open("inputs\day11.txt") as f:
        lines = [[*line.strip()] for line in f.readlines()]

    lines = np.array(lines)

    print(p1(lines))
    print(p2(lines))

def p1(grid):
    grid = expanduniverse(grid)
    indices = np.argwhere(grid == '#')

    total = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sum(np.abs(indices[i] - indices[j]))

    return total

def p2(grid):
    empty_rows = np.all(grid == '.', axis=1)
    empty_columns = np.all(grid == '.', axis=0)
    indices = np.argwhere(grid == '#')
    total = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            x, y = indices[i][0], indices[i][1]
            x_end, y_end = indices[j][0], indices[j][1]
            while x != x_end:
                if x < x_end:
                    x += 1
                else:
                    x -= 1
                total += 1
                if empty_rows[x]:
                    total += 1000000 - 1

            while y != y_end:
                if y < y_end:
                    y += 1
                else:
                    y -= 1
                total += 1
                if empty_columns[y]:
                    total += 1000000 - 1

    return total

def expanduniverse(grid):
    empty_rows = np.all(grid == '.', axis=1)
    empty_columns = np.all(grid == '.', axis=0)

    grid = np.insert(grid, np.where(empty_rows)[0] + 1, grid[empty_rows], axis=0)
    grid = np.insert(grid, np.where(empty_columns)[0] + 1, grid[:, empty_columns], axis=1)

    return grid

main()