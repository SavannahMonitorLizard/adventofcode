"""
https://adventofcode.com/2023/day/18
"""
def main():
    with open("inputs\day18.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    pos = (0, 0)
    vertices = []
    boundary = 0
    for line in lines:
        direction, distance, _ = line.split(" ")
        distance = int(distance)
        boundary += distance

        if direction == 'R':
            pos = (pos[0], pos[1] + distance)
        elif direction == 'L':
            pos = (pos[0], pos[1] - distance)
        elif direction == 'U':
            pos = (pos[0] - distance, pos[1])
        elif direction == 'D':
            pos = (pos[0] + distance, pos[1])

        vertices.append(pos)

    return int(polygon_area(vertices) - (boundary / 2) + 1 + boundary)

def p2(lines):
    pos = (0, 0)
    vertices = []
    boundary = 0
    for line in lines:
        _, _, code = line.split(" ")
        direction = code[-2]
        code = code[2:-2]
        distance = int(code, 16)
        boundary += distance

        if direction == '0':
            pos = (pos[0], pos[1] + distance)
        elif direction == '2':
            pos = (pos[0], pos[1] - distance)
        elif direction == '3':
            pos = (pos[0] - distance, pos[1])
        elif direction == '1':
            pos = (pos[0] + distance, pos[1])

        vertices.append(pos)

    return int(polygon_area(vertices) - (boundary / 2) + 1 + boundary)

def polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area

main()