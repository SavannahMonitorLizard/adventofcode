"""
https://adventofcode.com/2020/day/6
"""
def main():
    with open("inputs\day06p.txt") as f:
        plines = f.read().split("\n\n")

    with open("inputs\day06.txt") as f:
        lines = f.read().split("\n\n")

    print("Part 1:")
    print(p1(plines))
    print(p1(lines))
    print("Part 2:")
    print(p2(plines))
    print(p2(lines))

def p1(lines):
    total = 0

    for line in lines:
        qs = set()
        for p in line.split("\n"):
            [qs.add(i) for i in p]

        total += len(qs)

    return total

def p2(lines):
    total = 0

    for line in lines:
        qs = []
        for p in line.split("\n"):
            qs.append(set(p))

        cs = set(qs[0])
        for s in qs[1:]:
            cs = cs.intersection(s)

        total += len(cs)

    return total

main()