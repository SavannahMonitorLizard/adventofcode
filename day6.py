answers = open('inputs\\day6.txt', 'r').read().split("\n\n")

print("Part 1: " + str(sum([len(list(set.union(*map(set, answer.split("\n"))))) for answer in answers])) + "\nPart 2: " + str(sum([len(list(set.intersection(*map(set, answer.split("\n"))))) for answer in answers])))