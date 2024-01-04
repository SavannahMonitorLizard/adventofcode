"""
https://adventofcode.com/2020/day/6
"""
def main():
    with open("inputs\day08p.txt") as f:
        plines = [line.strip() for line in f.readlines()]

    with open("inputs\day08.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part 1:")
    print(p1(plines))
    print(p1(lines))
    # print("Part 2:")
    # print(p2(plines))
    # print(p2(lines))

def p1(lines):
    total = 0
    i = 0
    seen = set()
    while True:
        if i in seen:
            break
        seen.add(i)
        ins, val = lines[i].split(" ")
        val = int(val)
        if ins == "nop":
            i += 1
            continue
        elif ins == "jmp":
            i += val
        elif ins == "acc":
            i += 1
            total += val

    return total

def p2(lines):
    total = 0
    i = 0
    seen = set()
    while True:
        if i >= len(lines):
            break
        seen.add(i)
        ins, val = lines[i].split(" ")
        val = int(val)
        if ins == "nop":
            i += 1
            continue
        elif ins == "jmp":
            i += val
        elif ins == "acc":
            i += 1
            total += val

    return total

main()