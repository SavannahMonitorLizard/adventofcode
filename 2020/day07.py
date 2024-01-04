"""
https://adventofcode.com/2020/day/7
"""
def main():
    bags = open('inputs\\day07.txt', 'r').read().split("\n")

    global goldContents
    global bagContents

    goldContents = {}
    bagContents = {}

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

    print("Part 1:")
    print(p1())
    print("Part 2:")
    print(p2())

def p1():
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

    calculateContents(bagContents, "shiny gold")
    return len(bagsInside) - 1

def p2():
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

    return calculateContents(goldContents, "shiny gold") - 1

main()