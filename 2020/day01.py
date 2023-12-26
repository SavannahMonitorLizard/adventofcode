"""
https://adventofcode.com/2020/day/1
"""
def main():
    with open("inputs\day01p.txt") as f:
        plines = [line.strip() for line in f.readlines()]

    with open("inputs\day01.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part 1:")
    print(p1(plines))
    print(p1(lines))
    print("Part 2:")
    print(p2(plines))
    print(p2(lines))

def p1(lines):
    for i, l in enumerate(lines):
        for l2 in lines[i+1:]:
            if int(l) + int(l2) == 2020:
                return int(l) * int(l2)

def p2(lines):
    for i, l in enumerate(lines):
        for l2 in lines[i+1:]:
            for l3 in lines[i+2:]:
                if int(l) + int(l2) + int(l3) == 2020:
                    return int(l) * int(l2) * int(l3)


main()