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

point = [0, 0]
r1d1 = 0
r5d1 = 0
r7d1 = 0
r1d2 = 0

for i in range(len(trees)):
    point[0] = i + 1
    point[1] += 1

    try:
        if trees[i + 1][point[1] % 31] == "#":
            r1d1 += 1
    except IndexError:
        break

point = [0, 0]

for i in range(len(trees)):
    point[0] = i + 1
    point[1] += 5

    try:
        if trees[i + 1][point[1] % 31] == "#":
            r5d1 += 1
    except IndexError:
        break

point = [0, 0]

for i in range(len(trees)):
    point[0] = i + 1
    point[1] += 7

    try:
        if trees[i + 1][point[1] % 31] == "#":
            r7d1 += 1
    except IndexError:
        break

point = [0, 0]
counter = 0

for i in range(len(trees)):
    counter += 2
    point[0] = counter
    point[1] += 1

    try:
        if trees[counter][point[1] % 31] == "#":
            r1d2 += 1
    except IndexError:
        break

print(f"Part 2: {count * r1d1 * r5d1 * r7d1 * r1d2}")