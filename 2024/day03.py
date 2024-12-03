import re

def main():
    with open("inputs\day03.txt") as f:
        lines = [line.strip().split("mul") for line in f.readlines()]

    # print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0

    for line in lines:
        for com in line:
            matches = find_mul(com)

            if matches != []:
                total += int(matches[0]) * int(matches[1])

    return total

def p2(lines):
    total = 0
    en = True

    for line in lines:
        for com in line:
            if en:
                matches = find_mul(com)

                if matches != []:
                    total += int(matches[0]) * int(matches[1])
                
                stop = find_dont(com)

                if stop != []:
                    en = False
            else:
                res = find_do(com)

                if res != []:
                    en = True


    return total

def find_mul(text):
    pattern = r'^\((\d{1,3}),(\d{1,3})\)'
    matches = re.match(pattern, text)

    if matches:
        return matches.groups()
    else:
        return []
    
def find_do(text):
    pattern = r"do\(\)"
    matches = re.findall(pattern, text)

    return matches

def find_dont(text):
    pattern = r"don't\(\)"
    matches = re.findall(pattern, text)

    return matches

main()