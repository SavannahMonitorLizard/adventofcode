"""
https://adventofcode.com/2023/day/5
"""
import math

def main():
    with open("inputs\day05.txt") as f:
        lines = f.read()

    p1(lines)
    p2(lines)

def p1(lines):
    orders = lines.split("\n\n")
    locs = list(map(int, orders[0][7:].split(" ")))
    del orders[0]
    for i in range(len(orders)):
        orders[i] = [list(map(int, num.split(" "))) for num in orders[i].split(":")[1].split("\n")[1:]]

    for loc in range(len(locs)):
        locs[loc] = output(locs[loc], orders)

    print(min(locs))

def p2(lines):
    orders = lines.split("\n\n")
    locs = list(map(int, orders[0][7:].split(" ")))
    del orders[0]
    for i in range(len(orders)):
        orders[i] = [list(map(int, num.split(" "))) for num in orders[i].split(":")[1].split("\n")[1:]]
    boundaries = []
    newlocs = []
    i = 0
    while i < len(locs):
        tlocs = [locs[i], locs[i] + locs[i+1] - 1]
        newlocs.append(tlocs)
        i += 2

    for pair in newlocs:
        boundaries.append(find_boundaries(pair[0],pair[1],orders))

    points = []
    for li in boundaries:
        for pair in li:
            points += pair

    # print(points)
    
    outs = []
    for pt in points:
        outs.append(output(pt, orders))
    
    print(min(outs))

def find_boundaries(start, end, orders):
    boundaries = []
    point = start

    while point < end:
        diff = 10000
        boundary = []
        boundary.append(point)
        tpoint = point + diff
        while tpoint - boundary[-1] > 0.1:
            if point - output(point, orders) == tpoint - output(tpoint, orders):
                boundary.append(tpoint)
                tpoint += diff
            else:
                diff /= 2
                tpoint -= diff
        boundaries.append(boundary)
        point = math.ceil(boundary[-1]) + 1

    newbounds = []
    for bound in boundaries:
        newbounds.append([bound[0]])

    return newbounds

def output(loc, orders):
    for order in orders:
        for mp in order:
            if loc >= mp[1] and loc <= mp[1]+mp[2]-1:
                loc = loc - mp[1] + mp[0]
                break

    return loc

main()