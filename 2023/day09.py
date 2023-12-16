"""
https://adventofcode.com/2023/day/9
"""
import numpy as np
import itertools

def main():
    with open("inputs\day09.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    p1(lines)
    p2(lines)

def p1(lines):
    total = 0
    for line in lines:
        lastelems = []
        line = np.array(list(map(int, line.split(" "))))
        diff = np.diff(line)
        lastelems.append(line[-1])
        lastelems.append(diff[-1])
        while not np.all(diff == 0):
            diff = np.diff(diff)
            lastelems.append(diff[-1])

        total += sum(lastelems)

    print(total)

def p2(lines):
    total = 0
    for line in lines:
        elems = []
        line = np.array(list(map(int, line.split(" "))))
        diff = np.diff(line)
        elems.append(line[0])
        elems.append(diff[0])
        while not np.all(diff == 0):
            diff = np.diff(diff)
            elems.append(diff[0])

        total += sum(elems * np.fromiter(itertools.cycle([1,-1]), int, len(elems)))

    print(total)

main()