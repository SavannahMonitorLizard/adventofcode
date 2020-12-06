answers = open('inputs\\day6.txt', 'r').read().split("\n\n")

total = 0

for answer in answers:
    counted = []
    count = 0
    for letter in answer:
        if letter not in counted and letter != "\n":
            count += 1
            counted += [letter]

    total += count

print(f"Part 1: {total}")

total = 0

def intersect(lists):
    return list(set.intersection(*map(set, lists)))

for answer in answers:
    count = 0
    group = answer.split("\n")
    total += len(intersect(group))

print(f"Part 2: {total}")