import copy

adapters = [int(i) for i in open('inputs\\day10.txt', 'r').readlines()]
adapters = sorted(adapters)

oneJ = 1
threeJ = 1

for i in range(len(adapters)):
    try:
        d = adapters[i + 1] - adapters[i]
        if d == 1:
            oneJ += 1
        elif d == 3:
            threeJ += 1
    except IndexError:
        break

print(f"Part 1: {oneJ * threeJ}")

adapters.append(0)
adapters.sort()
arrangements = [0] * len(adapters)
arrangements[0] = 1

for i in range(1, len(adapters)):
    for j in range(i):
        if (adapters[i] - adapters[j] <= 3):
            arrangements[i] += arrangements[j]

print(f"Part 2: {arrangements[len(adapters) - 1]}")