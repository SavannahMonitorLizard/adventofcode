def main():
    with open("inputs\day01.txt") as f:
        lines = [line.strip().split("   ") for line in f.readlines()]

    # print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0
    left = []
    right = []
    for line in lines:
        left.append(int(line[0]))
        right.append(int(line[1]))
    
    left.sort()
    right.sort()

    for i in range(len(left)):
        total += abs(left[i] - right[i])

    return total

def p2(lines):
    total = 0

    left = []
    right = []
    for line in lines:
        left.append(int(line[0]))
        right.append(int(line[1]))

    for i in range(len(left)):
        sim = 0
        for j in range(len(right)):
            if left[i] == right[j]:
                sim += 1
        
        total += left[i] * sim

    return total

main()