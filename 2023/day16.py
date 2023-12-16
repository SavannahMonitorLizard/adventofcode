"""
https://adventofcode.com/2023/day/16
"""
def main():
    with open("inputs\day16.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    p1(lines)
    p2(lines)

def p1(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
            return True
        
    energized = set()
    beams = {(0,0): (0, 1)}
    c = 0
    while len(beams.items()) != 0:
        for beam in list(beams):
            direc = beams[beam]
            energized.add(beam)
            x, y = beam

            if grid[x][y] == "." or (grid[x][y] == "|" and (direc == (1, 0) or direc == (-1, 0))) or (grid[x][y] == "-" and (direc == (0, 1) or direc == (0, -1))):
                del beams[beam]

                x_new, y_new = x + direc[0], y + direc[1]
                if isvalid(x_new, y_new):
                    beam = (x_new, y_new)
                    beams[beam] = direc

                continue

            elif grid[x][y] == "\\" and direc == (0, 1):
                direc = (1, 0)
            elif grid[x][y] == "\\" and direc == (0, -1):
                direc = (-1, 0)
            elif grid[x][y] == "\\" and direc == (-1, 0):
                direc = (0, -1)
            elif grid[x][y] == "\\" and direc == (1, 0):
                direc = (0, 1)

            elif grid[x][y] == "/" and direc == (0, 1):
                direc = (-1, 0)
            elif grid[x][y] == "/" and direc == (0, -1):
                direc = (1, 0)
            elif grid[x][y] == "/" and direc == (-1, 0):
                direc = (0, 1)
            elif grid[x][y] == "/" and direc == (1, 0):
                direc = (0, -1)

            elif grid[x][y] == "|" and (direc == (0, 1) or direc == (0, -1)):
                del beams[beam]

                x_new, y_new = x + 1, y
                if isvalid(x_new, y_new):
                    beam = (x_new, y_new)
                    beams[beam] = (1, 0)

                x_new, y_new = x - 1, y
                if isvalid(x_new, y_new):
                    beam = (x_new, y_new)
                    beams[beam] = (-1, 0)

                continue

            elif grid[x][y] == "-" and (direc == (1, 0) or direc == (-1, 0)):
                del beams[beam]

                x_new, y_new = x, y + 1
                if isvalid(x_new, y_new):
                    beam = (x_new, y_new)
                    beams[beam] = (0, 1)

                x_new, y_new = x, y - 1
                if isvalid(x_new, y_new):
                    beam = (x_new, y_new)
                    beams[beam] = (0, -1)

                continue

            del beams[beam]

            x_new, y_new = x + direc[0], y + direc[1]
            if isvalid(x_new, y_new):
                beam = (x_new, y_new)
                beams[beam] = direc

            c += 1

        if c >= 200000:
            break

    print(len(energized))

def p2(grid):
    def isvalid(x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
            return True
        
    distances = []
    
    start_beams = get_starts(grid)

    for start_beam in start_beams.keys():
        energized = set()
        beams = {start_beam: start_beams[start_beam]}
        c = 0
        while len(beams.items()) != 0:
            for beam in list(beams):
                direc = beams[beam]
                energized.add(beam)
                x, y = beam

                if grid[x][y] == "." or (grid[x][y] == "|" and (direc == (1, 0) or direc == (-1, 0))) or (grid[x][y] == "-" and (direc == (0, 1) or direc == (0, -1))):
                    del beams[beam]

                    x_new, y_new = x + direc[0], y + direc[1]
                    if isvalid(x_new, y_new):
                        beam = (x_new, y_new)
                        beams[beam] = direc

                    continue

                elif grid[x][y] == "\\" and direc == (0, 1):
                    direc = (1, 0)
                elif grid[x][y] == "\\" and direc == (0, -1):
                    direc = (-1, 0)
                elif grid[x][y] == "\\" and direc == (-1, 0):
                    direc = (0, -1)
                elif grid[x][y] == "\\" and direc == (1, 0):
                    direc = (0, 1)

                elif grid[x][y] == "/" and direc == (0, 1):
                    direc = (-1, 0)
                elif grid[x][y] == "/" and direc == (0, -1):
                    direc = (1, 0)
                elif grid[x][y] == "/" and direc == (-1, 0):
                    direc = (0, 1)
                elif grid[x][y] == "/" and direc == (1, 0):
                    direc = (0, -1)

                elif grid[x][y] == "|" and (direc == (0, 1) or direc == (0, -1)):
                    del beams[beam]

                    x_new, y_new = x + 1, y
                    if isvalid(x_new, y_new):
                        beam = (x_new, y_new)
                        beams[beam] = (1, 0)

                    x_new, y_new = x - 1, y
                    if isvalid(x_new, y_new):
                        beam = (x_new, y_new)
                        beams[beam] = (-1, 0)

                    continue

                elif grid[x][y] == "-" and (direc == (1, 0) or direc == (-1, 0)):
                    del beams[beam]

                    x_new, y_new = x, y + 1
                    if isvalid(x_new, y_new):
                        beam = (x_new, y_new)
                        beams[beam] = (0, 1)

                    x_new, y_new = x, y - 1
                    if isvalid(x_new, y_new):
                        beam = (x_new, y_new)
                        beams[beam] = (0, -1)

                    continue

                del beams[beam]

                x_new, y_new = x + direc[0], y + direc[1]
                if isvalid(x_new, y_new):
                    beam = (x_new, y_new)
                    beams[beam] = direc

                c += 1

            if c >= 200000:
                break

        distances.append(len(energized))

    print(max(distances))

def get_starts(array):
    rows = len(array)
    cols = len(array[0])

    edge_directions = {}

    for col in range(cols):
        edge_directions[(0, col)] = (1, 0)
        edge_directions[(rows - 1, col)] = (-1, 0)

    for row in range(1, rows - 1):
        edge_directions[(row, 0)] = (0, 1)
        edge_directions[(row, cols - 1)] = (0, -1)

    return edge_directions

main()