"""
https://adventofcode.com/2023/day/3
"""
import math
from copy import deepcopy

def main():
    with open("inputs\day03.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        lines2 = deepcopy(lines)

    print(p1(lines))
    print(p2(lines2))

def p1(lines):
    total = 0

    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[0])-1):
            if lines[i][j] not in '0123456789.':
                adj = getadjacent(lines, i, j)

                for k in range(len(adj[0])):
                    if lines[i-1][j+k-1] >= '0' and lines[i-1][j+k-1] <= '9':
                        lines, n = getnum(lines, i-1, j+k-1)
                        total += n

                if lines[i][j-1] >= '0' and lines[i][j-1] <= '9':
                    lines, n = getnum(lines, i, j-1)
                    total += n
                if lines[i][j+1] >= '0' and lines[i][j+1] <= '9':
                    lines, n = getnum(lines, i, j+1)
                    total += n

                for k in range(len(adj[2])):
                    if lines[i+1][j+k-1] >= '0' and lines[i+1][j+k-1] <= '9':
                        lines, n = getnum(lines, i+1, j+k-1)
                        total += n

    return total

def p2(lines):
    total = 0

    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[0])-1):
            if lines[i][j] == "*":
                nums = [0] * 8
                for c, x, y in [(0,i-1, j-1), (1,i-1,j), (2,i-1,j+1),(3,i,j-1),(4,i,j+1),(5,i+1, j-1), (6,i+1,j), (7,i+1,j+1)]:
                    if lines[x][y] >= '0' and lines[x][y] <= '9':
                        lines, n = getnum(lines, x, y)
                        nums[c] = n

                if len([x for x in nums if x == 0]) == 6:
                    gears = [x for x in nums if x != 0]
                    total += math.prod(gears)

    return total

def getadjacent(lines, i, j):
    return [[lines[i-1][j-1], lines[i-1][j], lines[i-1][j+1]],
          [lines[i][j-1], lines[i][j+1]],
          [lines[i+1][j-1], lines[i+1][j], lines[i+1][j+1]]]

def getnum(lines, i, j):
    jo = j
    n = lines[i][j]
    line_list = list(lines[i])
    line_list[j] = '.'
    lines[i] = ''.join(line_list)
    while j != 0 and lines[i][j-1] >= '0' and lines[i][j-1] <= '9':
        n = lines[i][j-1] + n
        line_list = list(lines[i])
        line_list[j-1] = '.'
        lines[i] = ''.join(line_list)
        j -= 1

    j = jo

    while j < len(lines[0]) - 1 and lines[i][j+1] >= '0' and lines[i][j+1] <= '9':
        n = n + lines[i][j+1]
        line_list = list(lines[i])
        line_list[j+1] = '.'
        lines[i] = ''.join(line_list)
        j += 1

    return lines, int(n)

main()