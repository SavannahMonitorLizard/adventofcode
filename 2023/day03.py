"""
https://adventofcode.com/2023/day/3
"""
def main():
    with open("inputs\day3.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    p1(lines)
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