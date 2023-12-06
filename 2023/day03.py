"""
https://adventofcode.com/2023/day/3
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
--- Part Two ---

The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
def main():
    with open("inputs\day3.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    # p1(lines)
    p2(lines)

def getadjacent(lines, i, j):
    return [[lines[i-1][j-1], lines[i-1][j], lines[i-1][j+1]],
          [lines[i][j-1], lines[i][j+1]],
          [lines[i+1][j-1], lines[i+1][j], lines[i+1][j+1]]]

def getnum(lines, i, j):
    jo = j
    n = lines[i][j]
    line_list = list(lines[i])
    line_list[j] = '.'
    lines[i] = ''.join(line_list)
    while j != 0 and lines[i][j-1] >= '0' and lines[i][j-1] <= '9':
        n = lines[i][j-1] + n
        line_list = list(lines[i])
        line_list[j-1] = '.'
        lines[i] = ''.join(line_list)
        j -= 1

    j = jo

    while j < len(lines[0]) - 1 and lines[i][j+1] >= '0' and lines[i][j+1] <= '9':
        n = n + lines[i][j+1]
        line_list = list(lines[i])
        line_list[j+1] = '.'
        lines[i] = ''.join(line_list)
        j += 1

    return lines, int(n)

def p1(lines):
    total = 0

    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[0])-1):
            if lines[i][j] not in '0123456789.':
                adj = getadjacent(lines, i, j)

                for k in range(len(adj[0])):
                    if lines[i-1][j+k-1] >= '0' and lines[i-1][j+k-1] <= '9':
                        lines, n = getnum(lines, i-1, j+k-1)
                        total += n

                if lines[i][j-1] >= '0' and lines[i][j-1] <= '9':
                    lines, n = getnum(lines, i, j-1)
                    total += n
                if lines[i][j+1] >= '0' and lines[i][j+1] <= '9':
                    lines, n = getnum(lines, i, j+1)
                    total += n

                for k in range(len(adj[2])):
                    if lines[i+1][j+k-1] >= '0' and lines[i+1][j+k-1] <= '9':
                        lines, n = getnum(lines, i+1, j+k-1)
                        total += n

    print(total)

def p2(lines):
    total = 0

    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[0])-1):
            if lines[i][j] in "*":
                n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = 0
                adj = getadjacent(lines, i, j)

                # for k in range(len(adj[0])):
                #     if lines[i-1][j+k-1] >= '0' and lines[i-1][j+k-1] <= '9':
                #         lines, n1 = getnum(lines, i-1, j+k-1)

                if lines[i-1][j-1] >= '0' and lines[i-1][j-1] <= '9':
                    lines, n1 = getnum(lines, i-1, j-1)
                if lines[i-1][j] >= '0' and lines[i-1][j] <= '9':
                    lines, n2 = getnum(lines, i-1, j)
                if lines[i-1][j+1] >= '0' and lines[i-1][j+1] <= '9':
                    lines, n3 = getnum(lines, i-1, j+1)
                
                if lines[i][j-1] >= '0' and lines[i][j-1] <= '9':
                    lines, n4 = getnum(lines, i, j-1)
                if lines[i][j+1] >= '0' and lines[i][j+1] <= '9':
                    lines, n5 = getnum(lines, i, j+1)

                # for k in range(len(adj[2])):
                #     if lines[i+1][j+k-1] >= '0' and lines[i+1][j+k-1] <= '9':
                #         lines, n4 = getnum(lines, i+1, j+k-1)

                if lines[i+1][j-1] >= '0' and lines[i+1][j-1] <= '9':
                    lines, n6 = getnum(lines, i+1, j-1)
                if lines[i+1][j] >= '0' and lines[i+1][j] <= '9':
                    lines, n7 = getnum(lines, i+1, j)
                if lines[i+1][j+1] >= '0' and lines[i+1][j+1] <= '9':
                    lines, n8 = getnum(lines, i+1, j+1)

                if len([x for x in [n1,n2,n3,n4,n5,n6,n7,n8] if x == 0]) == 6:
                    if n1 == 0:
                        n1 = 1
                    if n2 == 0:
                        n2 = 1
                    if n3 == 0:
                        n3 = 1
                    if n4 == 0:
                        n4 = 1
                    if n5 == 0:
                        n5 = 1
                    if n6 == 0:
                        n6 = 1
                    if n7 == 0:
                        n7 = 1
                    if n8 == 0:
                        n8 = 1

                    n = n1 * n2 * n3 * n4 * n5 * n6 * n7 * n8
                    total += n

    print(total)

main()