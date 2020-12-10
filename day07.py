bags = open('inputs\\day7.txt', 'r').read().split("\n")

goldContents = {}
bagContents = {}
bagsInside = {}

def calculateContents(array, bagType):
    if bagType in bagsInside:
        return bagsInside[bagType]
    count = 1
    if bagType not in array:
        array[bagType] = []
    for k, v in array[bagType]:
        count += k * calculateContents(array, v)
    bagsInside[bagType] = count
    return count

for bag in bags:
    bag = bag.replace('.', '')
    bagMain, thingsContained = bag.split(' bags contain ')
    contents = thingsContained.split(',')
    for content in contents:
        content = content.strip()
        if content == 'no other bags':
            continue
        c, d = content.split(' ', 1)
        c = int(c)
        d = d.replace('bags', '').replace('bag', '').strip()
        if bagMain not in goldContents:
            goldContents[bagMain] = []
        goldContents[bagMain].append((c, d))
        if d not in bagContents:
            bagContents[d] = []
        bagContents[d].append((c, bagMain))

calculateContents(bagContents, "shiny gold")
print("Part 1: " + str(len(bagsInside) - 1))

bagsInside = {}
print("Part 2: " + str(calculateContents(goldContents, "shiny gold") - 1))