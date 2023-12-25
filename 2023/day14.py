"""
https://adventofcode.com/2023/day/14
"""
import numpy as np

def main():
    with open("inputs\day14.txt") as f:
        lines = [[*line.strip()] for line in f.readlines()]

    lines = np.array(lines)

    print(p1(lines))
    print(p2(lines))

def p1(grid):
    grid = tiltnorth(grid)

    return sum(sum(np.transpose(grid == "O")) * np.arange(len(grid[0]), 0, -1))

def p2(grid):
    def contained(grid, grids):
        return np.any([np.all(np.array(subarray) == grid) for subarray in grids])
    
    grids = []
    for i in range(1000000000):
        grid = cycle(grid)
        if contained(grid, grids):
            break
        grids.append(grid.copy())

    c = 0
    while True:
        if np.all(grids[c] == grid):
            break
        c += 1

    inx = (1000000000-(c+1))%(i-c) + c
    bgrid = grids[inx]
    return sum(sum(np.transpose(bgrid == "O")) * np.arange(len(bgrid[0]), 0, -1))

def tiltnorth(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != "O" and grid[x][y] != "#":
            return True

    changed = True

    while changed:
        changed = False
        inx = np.argwhere(grid == "O")

        for rock in inx:
            i, j = rock
            i -= 1
            while isvalid(i, j):
                i -= 1
            i += 1
            if i != rock[0]:
                changed = True
                grid[rock[0]][rock[1]] = "."
                grid[i][j] = "O"

    return grid

def tiltwest(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != "O" and grid[x][y] != "#":
            return True

    changed = True

    while changed:
        changed = False
        inx = np.argwhere(grid == "O")

        for rock in inx:
            i, j = rock
            j -= 1
            while isvalid(i, j):
                j -= 1
            j += 1
            if j != rock[1]:
                changed = True
                grid[rock[0]][rock[1]] = "."
                grid[i][j] = "O"

    return grid

def tiltsouth(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != "O" and grid[x][y] != "#":
            return True

    changed = True

    while changed:
        changed = False
        inx = np.argwhere(grid == "O")

        for rock in inx:
            i, j = rock
            i += 1
            while isvalid(i, j):
                i += 1
            i -= 1
            if i != rock[0]:
                changed = True
                grid[rock[0]][rock[1]] = "."
                grid[i][j] = "O"

    return grid

def tilteast(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != "O" and grid[x][y] != "#":
            return True

    changed = True

    while changed:
        changed = False
        inx = np.argwhere(grid == "O")

        for rock in inx:
            i, j = rock
            j += 1
            while isvalid(i, j):
                j += 1
            j -= 1
            if j != rock[1]:
                changed = True
                grid[rock[0]][rock[1]] = "."
                grid[i][j] = "O"

    return grid

def cycle(grid):
    grid = tiltnorth(grid)
    grid = tiltwest(grid)
    grid = tiltsouth(grid)
    grid = tilteast(grid)
    return grid

main()