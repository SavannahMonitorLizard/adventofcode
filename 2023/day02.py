"""
https://adventofcode.com/2023/day/2
"""
def main():
    with open("inputs\day2.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    p1(lines)
    p2(lines)

def p1(lines):
    max_values = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    for line in lines:
        good = True
        g1 = line.split(":")
        id = g1[0][5:]
        g2 = g1[1][1:]
        groups = g2.split(';')

        for group in groups:
            items = group.split(',')
            for item in items:
                parts = item.split()
                quantity, color = parts
                if int(quantity) > max_values[color]:
                    good = False

        if good:
            total += int(id)
    
    print(total)

def p2(lines):
    total = 0
    for line in lines:
        color_counts = {'red': 0, 'green': 0, 'blue': 0}
        g1 = line.split(":")
        g2 = g1[1][1:]
        groups = g2.split(';')

        for group in groups:
            items = group.split(',')
            for item in items:
                parts = item.strip().split()
                quantity, color = parts
                color_counts[color] = max(color_counts[color], int(quantity))

        total += color_counts['blue'] * color_counts['red'] * color_counts['green']

    print(total)

main()