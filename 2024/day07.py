from itertools import product

def main():
    with open("inputs\day07.txt") as f:
        lines = [line.strip().split(": ") for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0

    for line in lines:
        left = int(line[0])
        right = [int(i) for i in line[1].split(" ")]
        if check1(left, right):
            total += left

    return total

def p2(lines):
    total = 0

    for line in lines:
        left = int(line[0])
        right = [int(i) for i in line[1].split(" ")]
        if check2(left, right):
            total += left

    return total

def check1(result, nums):
    operators = ['+', '*']
    operator_combinations = product(operators, repeat=len(nums)-1)

    def ev(numbers, operators):
        total = numbers[0]

        for i in range(1, len(numbers)):
            if operators[i-1] == '+':
                total += numbers[i]

            elif operators[i-1] == '*':
                total *= numbers[i]

        return total
    
    for operators in operator_combinations:
        if ev(nums, operators) == result:
            return True
    
    return False

def check2(result, nums):
    operators = ['+', '*', "||"]
    operator_combinations = product(operators, repeat=len(nums)-1)

    def ev(numbers, operators):
        total = numbers[0]

        for i in range(1, len(numbers)):
            if operators[i-1] == '+':
                total += numbers[i]

            elif operators[i-1] == '*':
                total *= numbers[i]

            elif operators[i-1] == '||':
                total = int(str(total) + str(numbers[i]))

        return total
    
    for operators in operator_combinations:
        if ev(nums, operators) == result:
            return True
    
    return False

main()