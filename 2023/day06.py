"""
https://adventofcode.com/2023/day/6
"""
def main():
    with open("inputs\day06.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 1
    times = [int(x) for x in lines[0][5:].split(" ") if x != '']
    dists = [int(x) for x in lines[1][9:].split(" ") if x != '']
    
    for time in range(len(times)):
        t = 0
        for i in range(times[time]):
            if (times[time]-i)*i > dists[time]:
                t += 1

        total *= t

    return total

def p2(lines):
    total = 0
    time = int("".join([x for x in lines[0][5:] if x != ' ']))
    dist = int("".join([x for x in lines[1][9:] if x != ' ']))
    for i in range(time):
        if (time-i)*i > dist:
            total += 1

    return total

main()