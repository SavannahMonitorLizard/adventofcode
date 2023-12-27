"""
https://adventofcode.com/2020/day/4
"""
def main():
    with open("inputs\day04p.txt") as f:
        plines = f.read().split("\n\n")

    with open("inputs\day04.txt") as f:
        lines = f.read().split("\n\n")

    print("Part 1:")
    print(p1(plines))
    print(p1(lines))
    print("Part 2:")
    print(p2(plines))
    print(p2(lines))

def p1(lines):
    total = 0
    for pport in lines:
        if all([f in pport for f in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]):
            total += 1

    return total

def p2(lines):
    total = 0
    for pport in lines:
        cons = [False] * 7
        npports = pport.split("\n")
        for npport in npports:
            for fv in npport.split(" "):
                field, value = fv.split(":")
                if (field == "byr" and (1920 <= int(value) <= 2002)):
                    cons[0] = True
                elif (field == "iyr" and (2010 <= int(value) <= 2020)):
                    cons[1] = True
                elif (field == "eyr" and (2020 <= int(value) <= 2030)):
                    cons[2] = True
                elif (field == "hgt"):
                    if value[-2:] == "cm" and (150 <= int(value[:-2]) <= 193):
                        cons[3] = True
                    elif value[-2:] == "in" and (59 <= int(value[:-2]) <= 76):
                        cons[3] = True
                elif (field == "hcl" and len(value) == 7 and value[0] == "#"):
                    cons[4] = True
                    for letter in value[1:]:
                        if letter not in "abcdef0123456789":
                            cons[4] = False
                elif (field == "ecl" and (value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])):
                    cons[5] = True
                elif (field == "pid" and (len(value) == 9)):
                    cons[6] = True
                    for letter in value[1:]:
                        if letter not in "0123456789":
                            cons[6] = False

        if all(cons):
            total += 1

    return total

main()