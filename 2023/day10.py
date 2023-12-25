"""
https://adventofcode.com/2023/day/10
"""
def main():
    with open("inputs\day10.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

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
 
    return int(distance/2)

def p2(grid):
    def polygon_area(vertices):
        n = len(vertices)
        area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
        return area
    
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and ((x, y) not in visited or (grid[x][y] == "S" and distance != 1)):
            return True
    
    start_x, start_y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_x, start_y = i, j

    x, y = start_x - 1, start_y
    distance = 1
    visited = set()
    visited.add((start_x, start_y))
    vertices = []
    vertices.append((start_x, start_y))

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
            vertices.append((x,y))
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "J":
            vertices.append((x,y))
            if isvalid(x, y - 1):
                x, y = x, y - 1
            elif isvalid(x - 1, y):
                x, y = x - 1, y
        elif grid[x][y] == "7":
            vertices.append((x,y))
            if isvalid(x, y - 1):
                x, y = x, y - 1
            elif isvalid(x + 1, y):
                x, y = x + 1, y
        elif grid[x][y] == "F":
            vertices.append((x,y))
            if isvalid(x, y + 1):
                x, y = x, y + 1
            elif isvalid(x + 1, y):
                x, y = x + 1, y

        distance += 1

    return int((polygon_area(vertices) - (distance / 2) + 1))

main()