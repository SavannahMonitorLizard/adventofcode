"""
https://adventofcode.com/2023/day/10
"""
def main():
    with open("inputs\p.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    p1(lines)
    p2(lines)

def p1(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and ((x, y) not in visited or (grid[x][y] == "S" and distance != 1)):
            return True
    
    start_x, start_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_x, start_y = i, j

    x, y = start_x, start_y + 1
    distance = 1
    visited = set()
    visited.add((start_x, start_y))

    while grid[x][y] != "S":
        visited.add((x, y))

        if grid[x][y] == "|":
            if isvalid(x + 1, y):
                x, y = x + 1, y
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "-":
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x, y - 1):
                x, y = x, y - 1
        elif grid[x][y] == "L":
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "J":
            if isvalid(x, y - 1):
                x, y = x, y - 1
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "7":
            if isvalid(x, y - 1):
                x, y = x, y - 1
            elif isvalid(x + 1, y):
                x, y = x + 1, y
        elif grid[x][y] == "F":
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x + 1, y):
                x, y = x + 1, y

        distance += 1

    grid2 = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid2[i] = [*grid2[i]]
            if (i, j) in visited:
                grid2[i][j] = "#"
            else:
                grid2[i][j] = "."
            "".join(grid2[i])

    with open("inputs\\day10a.txt", "w") as f:
        for line in grid2:
            f.write("".join(line) + "\n")
 
    print(distance/2)

def p2(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and ((x, y) not in visited or (grid[x][y] == "S" and distance != 1)):
            return True
    
    start_x, start_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_x, start_y = i, j

    x, y = start_x, start_y + 1
    distance = 1
    seeds = []
    visited = set()
    visited.add((start_x, start_y))
    left = (-1, 0)

    while grid[x][y] != "S":
        visited.add((x, y))

        if grid[x][y] == "|":
            if isvalid(x + 1, y):
                x, y = x + 1, y
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "-":
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x, y - 1):
                x, y = x, y - 1
        elif grid[x][y] == "L":
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "J":
            if isvalid(x, y - 1):
                x, y = x, y - 1
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "7":
            if isvalid(x, y - 1):
                x, y = x, y - 1
            elif isvalid(x + 1, y):
                x, y = x + 1, y
        elif grid[x][y] == "F":
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x + 1, y):
                x, y = x + 1, y

        distance += 1

        if grid[x][y] == "7":
            left = (0, 1)
        elif grid[x][y] == "L":
            left = (-1, 0)
        elif grid[x][y] == "J":
            left = (0, -1)
        elif grid[x][y] == "F":
            left = (-1, 0)


main()