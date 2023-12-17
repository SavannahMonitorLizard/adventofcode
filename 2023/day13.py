"""
https://adventofcode.com/2023/day/13
"""
import numpy as np

def main():
    with open("inputs\day13.txt") as f:
        lines = f.read().split("\n\n")

    p1(lines)
    p2(lines)

def p1(grids):
    total = 0

    for grid in grids:
        grid = np.array([[*g] for g in grid.split("\n")])
        line = vertref(grid)
        if line != 0:
            total += line
        else:
            total += 100 * vertref(np.transpose(grid))

    print(total)

def p2(grids):
    total = 0

    for grid in grids:
        grid = np.array([[*g] for g in grid.split("\n")])
        line = vertref2(grid)
        if line != 0:
            total += line
        else:
            total += 100 * vertref2(np.transpose(grid))

    print(total)

def vertref(grid):
    _, c = grid.shape
    for i in range(1, c):
        if i < c/2:
            lhalf = grid[:,:i]
            rhalf = grid[:,i:i*2][:,::-1]
            if np.all(lhalf == rhalf):
                return i
        elif i > c/2:
            lhalf = grid[:,i-(c-i):i]
            rhalf = grid[:,i:i*2][:,::-1]
            if np.all(lhalf == rhalf):
                return i
    return 0

def vertref2(grid):
    _, c = grid.shape
    for i in range(1, c):
        if i < c/2:
            lhalf = grid[:,:i]
            rhalf = grid[:,i:i*2][:,::-1]
            if np.count_nonzero((lhalf == rhalf) == False) == 1:
                return i
        elif i > c/2:
            lhalf = grid[:,i-(c-i):i]
            rhalf = grid[:,i:i*2][:,::-1]
            if np.count_nonzero((lhalf == rhalf) == False) == 1:
                return i
    return 0

main()