"""
https://adventofcode.com/2023/day/15
"""
def main():
    with open("inputs\day15.txt") as f:
        lines = f.readlines()

    p1(lines)
    p2(lines)

def p1(line):
    line = line[0].split(",")
    total = 0
    for word in line:
        cv = 0
        for c in word:
            cv += ord(c)
            cv *= 17
            cv %= 256
        total += cv

    print(total)

def p2(grid):
    pass

main()