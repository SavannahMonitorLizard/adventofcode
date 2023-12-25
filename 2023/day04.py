"""
https://adventofcode.com/2023/day/4
"""
def main():
    with open("inputs\day04.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0

    for line in lines:
        line = line.split(": ")
        line = line[1]
        left_part, right_part = line.split("|")

        left_set = set(map(int, left_part.split()))
        right_set = set(map(int, right_part.split()))
        count = sum(1 for num in right_set if num in left_set)
        if count != 0:
            total += (2**(count-1))

    return total

def p2(lines):
    cards = [1] * len(lines)

    for i in range(len(lines)):
        line = lines[i].split(": ")
        line = line[1]
        left_part, right_part = line.split("|")

        left_set = set(map(int, left_part.split()))
        right_set = set(map(int, right_part.split()))
        count = sum(1 for num in right_set if num in left_set)
        
        for j in range(1,count+1):
            cards[i+j] += cards[i]

    return sum(cards)

main()