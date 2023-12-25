"""
https://adventofcode.com/2023/day/1
"""
def main():
    with open("inputs\day01.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0
    firstchar = ""
    lastchar = ""
    nums = ["1","2","3","4","5","6","7","8","9"]
    for line in lines:
        for c in line:
            if c in nums:
                firstchar = c
                break
        for c in reversed(line):
            if c in nums:
                lastchar = c
                break
        n = firstchar + lastchar
        total += int(n)

    return total

def p2(lines):
    total = 0
    digits = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }

    for line in lines:
        newline = [0] * len(line)
        for k in digits.keys():
            ii = findall(k, line)
            for i in ii:
                if i != -1:
                    newline[i] = digits[k]

        newline = [x for x in newline if x != 0]
        total += newline[0] * 10 + newline[-1]
    
    return total

def findall(p, s):
    ii = []
    i = s.find(p)
    while i != -1:
        ii.append(i)
        i = s.find(p, i+1)

    if ii == []:
        ii.append(-1)

    return ii

main()