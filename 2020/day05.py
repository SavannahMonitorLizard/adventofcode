"""
https://adventofcode.com/2020/day/5
"""
def main():
    with open("inputs\day05p.txt") as f:
        plines = [line.strip() for line in f.readlines()]

    with open("inputs\day05.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print("Part 1:")
    print(p1(plines))
    print(p1(lines))
    print("Part 2:")
    print(p2(lines))

def p1(lines):
    mID = 0

    for line in lines:
        ri, ci = line[:7], line[7:]

        row = range(128)
        col = range(8)
        for i in ri:
            if i == "F":
                row = range(row.start, (row.start + row.stop) // 2)
            elif i == "B":
                row = range((row.start + row.stop) // 2, row.stop)

        for j in ci:
            if j == "L":
                col = range(col.start, (col.start + col.stop) // 2)
            elif j == "R":
                col = range((col.start + col.stop) // 2, col.stop)

        mID = max(mID, list(row)[0] * 8 + list(col)[0])

    return mID

def p2(lines):
    IDs = []

    for line in lines:
        ri, ci = line[:7], line[7:]

        row = range(128)
        col = range(8)
        for i in ri:
            if i == "F":
                row = range(row.start, (row.start + row.stop) // 2)
            elif i == "B":
                row = range((row.start + row.stop) // 2, row.stop)

        for j in ci:
            if j == "L":
                col = range(col.start, (col.start + col.stop) // 2)
            elif j == "R":
                col = range((col.start + col.stop) // 2, col.stop)

        IDs.append(list(row)[0] * 8 + list(col)[0])

    IDs = sorted(IDs)
    for i in range(len(IDs)-1):
        if (IDs[i+1]) - IDs[i] != 1:
            return IDs[i] + 1

main()