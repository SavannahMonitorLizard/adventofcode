"""
https://adventofcode.com/2023/day/8
"""
import math

def main():
    with open("inputs\day08.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    p1(lines)
    p2(lines)

def p1(lines):
    rl = lines[0]
    lines = lines[2:]
    node = "AAA"
    nodes = {}
    for line in lines:
        line = line.split(" = ")
        nodes[line[0]] = line[1][1:-1]
    
    steps = 0
    i = 0
    while node != "ZZZ":
        direc = rl[i]
        if direc == "L":
            node = nodes[node][0:3]
        elif direc == "R":
            node = nodes[node][5:]
        steps += 1
        i = i + 1
        if i >= len(rl):
            i = 0

    print(steps)

def p2(lines):
    rl = lines[0]
    lines = lines[2:]
    nodes = []
    paths = {}
    for line in lines:
        linesp = line.split(" = ")
        paths[linesp[0]] = linesp[1][1:-1]
        if linesp[0][-1] == "A":
            nodes.append(linesp[0])
    
    steps = []
    i = 0
    for node in nodes:
        step = 0
        while node[-1] != "Z":
            direc = rl[i]
            if direc == "L":
                node = paths[node][0:3]
            elif direc == "R":
                node = paths[node][5:]
            step += 1
            i = i + 1
            if i >= len(rl):
                i = 0
        steps.append(step)

    print(math.lcm(*steps))

main()