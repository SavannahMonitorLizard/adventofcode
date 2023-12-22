"""
https://adventofcode.com/2023/day/21
"""
import numpy as np
from copy import deepcopy

def main():
    with open("inputs\day21.txt") as f:
        lines = [[*line.strip()] for line in f.readlines()]

    global grid
    grid = np.array(lines)

    print(p1(64))
    p2(26501365 % len(grid))

def p1(n):
    directions = np.array([
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)]
    )

    start = np.argwhere(grid == "S")
    start_x, start_y = start[0][0], start[0][1]

    locs = np.array([(start_x, start_y)])
    for _ in range(n):
        newlocs = []
        for loc in locs:
            for direc in directions:
                if isvalid(loc + direc):
                    if list(loc + direc) not in newlocs:
                        newlocs.append(list(loc + direc))

        newlocs = np.array(newlocs)
        locs = newlocs

    return len(locs)

def p2(n):
    directions = ([
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)]
    )

    start = np.argwhere(grid == "S")
    start = (start[0][0], start[0][1])
    m = len(grid)
    counts = []

    next_queue = [start]
    for i in range(1, (n + m * 2) + 1):
        print(i)
        curr_queue = deepcopy(next_queue)
        visited = set(deepcopy(next_queue))
        next_queue = []

        while curr_queue:
            curr = curr_queue.pop(0)

            for dir in directions:
                new_y, new_x = curr[0] + dir[0], curr[1] + dir[1]

                if grid[new_y % m][new_x % m] != "#" and (new_y, new_x) not in visited:
                    visited.add((new_y, new_x))
                    next_queue.append((new_y, new_x))

        if i in [n, n + m, n + m * 2]:
            counts.append(len(next_queue))

    counts = [3726, 33086, 91672]
    coeffs = np.polyfit([65, 196, 327], counts, 2)
    print(coeffs)
    poly = np.poly1d(coeffs)
    print(poly(26501365))

def isvalid(pt):
    x, y = pt
    x %= len(grid)
    y %= len(grid)
    if not (x in range(0, len(grid[0])) and y in range(0, len(grid))):
        return False
    if grid[x][y] == "#":
        return False
    else:
        return True

main()