def main():
    with open("inputs\day04.txt") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                total = find_M(total, lines, i, j)

    return total

def p2(lines):
    total = 0
    
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) - 1):
            if lines[i][j] == "A":
                if (lines[i - 1][j - 1] == "M" and lines[i + 1][j + 1] == "S") or (lines[i - 1][j - 1] == "S" and lines[i + 1][j + 1] == "M"):
                    if (lines[i - 1][j + 1] == "M" and lines[i + 1][j - 1] == "S") or (lines[i - 1][j + 1] == "S" and lines[i + 1][j - 1] == "M"):
                        total += 1

    return total

def find_M(total, lines, i, j):
    for pos in find_neighbors(lines, i, j):
        if lines[pos[0]][pos[1]] == "M":
            dir = (pos[0] - i, pos[1] - j)
            total = find_A(total, lines, pos[0], pos[1], dir)

    return total

def find_A(total, lines, i, j, dir):
    if 0 <= i + dir[0] < len(lines) and 0 <= j + dir[1] < len(lines[0]):
        if lines[i + dir[0]][j + dir[1]] == "A":
            total = find_S(total, lines, i + dir[0], j + dir[1], dir)

    return total

def find_S(total, lines, i, j, dir):
    if 0 <= i + dir[0] < len(lines) and 0 <= j + dir[1] < len(lines[0]):
        if lines[i + dir[0]][j + dir[1]] == "S":
            total += 1

    return total

def find_neighbors(lines, i, j):
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    row, col = i, j

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))

    return neighbors

main()