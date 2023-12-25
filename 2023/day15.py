"""
https://adventofcode.com/2023/day/15
"""
def main():
    with open("inputs\day15.txt") as f:
        lines = f.readlines()[0].split(",")

    print(p1(lines))
    print(p2(lines))

def p1(line):
    total = 0
    for word in line:
        total += HASH(word)

    return total

def p2(line):
    lenses = {}
    for i, order in enumerate(line):
        if "=" in order:
            label, lens = order.split("=")
            box = HASH(label)
            if box not in lenses.keys() or (not any([label == lens[:-1] for lens in lenses[box]])):
                lenses.setdefault(box, []).append(label + lens)
            else:
                for i, nlens in enumerate(lenses[box]):
                    if label == nlens[:-1]:
                        inx = i
                lenses[box][inx] = label + lens
        elif "-" in order:
            label, _ = order.split("-")
            box = HASH(label)
            if box in lenses.keys():
                if any([label == lens[:-1] for lens in lenses[box]]):
                    for i, lens in enumerate(lenses[box]):
                        if label == lens[:-1]:
                            inx = i
                    del lenses[box][inx]

    # print(lenses)
    
    total = 0
    for box in [lens for lens in lenses.keys() if len(lenses[lens]) != 0]:
        for i, lens in enumerate(lenses[box]):
            # print(box, i, lens, (box + 1) * (i + 1) * int(lens[-1]))
            total += (box + 1) * (i + 1) * int(lens[-1])

    return total

def HASH(word):
    cv = 0
    for c in word:
        cv += ord(c)
        cv *= 17
        cv %= 256
    
    return cv

main()