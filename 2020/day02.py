"""
https://adventofcode.com/2020/day/2
"""
def main():
    with open("inputs\day02p.txt") as f:
        plines = [line.strip() for line in f.readlines()]

    with open("inputs\day02.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part 1:")
    print(p1(plines))
    print(p1(lines))
    print("Part 2:")
    print(p2(plines))
    print(p2(lines))

def p1(lines):
    total = 0

    for line in lines:
        counts, pw = line.split(": ")
        r, ch = counts.split(" ")
        mi, ma = r.split("-")
        if int(mi) <= pw.count(ch) <= int(ma):
            total += 1

    return total

def p2(lines):
    total = 0

    for line in lines:
        counts, pw = line.split(": ")
        r, ch = counts.split(" ")
        mi, ma = r.split("-")
        if (pw[int(mi) - 1] == ch) ^ (pw[int(ma) - 1] == ch):
            total += 1

    return total

main()