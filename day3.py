trees = open('inputs\\day3.txt', 'r').read().split("\n")

point = [0, 0]
count = 0

for i in range(len(trees)):
    point[0] = i + 1
    point[1] += 3

    try:
        if trees[i + 1][point[1] % 31] == "#":
            count += 1
    except IndexError:
        break

print(f"Part 1: {count}")

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

total = 1

for s in slopes:
    point = [0, 0]
    count = 0
    for i in range(len(trees)):
        dx, dy = s
        point[0] += dy
        point[1] += dx

        try:
            if trees[point[0]][point[1] % 31] == "#":
                count += 1
        except IndexError:
            break

    total *= count

print(f"Part 2: {total}")