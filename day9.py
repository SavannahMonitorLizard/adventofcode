numbers = [int(i) for i in open('inputs\\day9.txt', 'r').readlines()]

preamble = numbers[:25]

def calcValid(validNums, num):
    for j in validNums:
        for k in validNums:
            if int(j) + int(k) == int(num):
                return True

    return False

for i in range(len(numbers)):
    if i >= len(preamble):
        valid = calcValid(numbers[i-len(preamble): i], numbers[i])
        if not valid:
            invalid = numbers[i]
            break

print(f"Part 1: {invalid}")

def calcContinuous(num):
    current = 0
    num = int(num)
    for i in range(len(numbers)):
        current = 0
        for j in range(len(numbers)):
            if current < num:
                current += int(numbers[i + j])
                if current == num:
                    return numbers[i: i+j + 1]
            else:
                break
    
    return []

nums = calcContinuous(invalid)
print(f"Part 2: {min(nums) + max(nums)}")