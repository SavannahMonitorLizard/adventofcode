trees = open('inputs\\day3.txt', 'r').read().split("\n")

y, x = [0, 0]
count = 0
y_max = len(trees)

for i in range(len(trees)):
    y = i + 1
    x += 3

    while y < y_max:
        if trees[y][x % 31] == "#":
            count += 1
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
    y, x = [0, 0]
    count = 0
    for i in range(len(trees)):
        dx, dy = s
        y += dy
        x += dx

        while y < y_max:
            if trees[y][x % 31] == "#":
                count += 1
            break

    total *= count

print(f"Part 2: {total}")