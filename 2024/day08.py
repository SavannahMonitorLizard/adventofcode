def main():
    with open("inputs\day08.txt") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    ant = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != "." and lines[i][j] not in ant:
                ant.append(lines[i][j])

    antinodes = set()
    for a in ant:
        pos = []
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == a:
                    pos.append((i, j))

        antinodes.update(set(find_pos1(pos, len(lines), len(lines[0]))))

    return len(antinodes)

def p2(lines):
    ant = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != "." and lines[i][j] not in ant:
                ant.append(lines[i][j])

    antinodes = set()
    for a in ant:
        pos = []
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == a:
                    pos.append((i, j))

        antinodes.update(set(find_pos2(pos, len(lines), len(lines[0]))))

    return len(antinodes)

def find_pos1(positions, rows, cols):
    result = []

    for x in positions:
        for y in positions:
            if x == y:
                continue

            disp = (y[0] - x[0], y[1] - x[1])

            if 0 <= x[0] - disp[0] < rows and 0 <= x[1] - disp[1] < cols:
                result.append((x[0] - disp[0], x[1] - disp[1]))
            if 0 <= y[0] + disp[0] < rows and 0 <= y[1] + disp[1] < cols:
                result.append((y[0] + disp[0], y[1] + disp[1]))

    return result

def find_pos2(positions, rows, cols):
    result = []

    for x in positions:
        for y in positions:
            if x == y:
                continue

            disp = (y[0] - x[0], y[1] - x[1])

            for i in range(-100, 100):
                if 0 <= x[0] - i*disp[0] < rows and 0 <= x[1] - i*disp[1] < cols:
                    result.append((x[0] - i*disp[0], x[1] - i*disp[1]))
                else:
                    continue

    return result

main()