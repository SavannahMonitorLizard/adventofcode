"""
https://adventofcode.com/2023/day/12
"""
import functools

def main():
    with open("inputs\day12.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0

    for line in lines:
        line = line.split(" ")
        orders = line[1]
        nums = [int(i) for i in orders.split(",")]
        line = line[0]
        total += solve(line, tuple(nums))

    return total

def p2(lines):
    total = 0

    for line in lines:
        line = line.split(" ")
        orders = line[1]
        nums = [int(i) for i in orders.split(",")]
        line = line[0]
        nums *= 5
        line += "?"
        line *= 5
        line = line[:-1]
        total += solve(line, tuple(nums))

    return total

@functools.cache
def solve(line, nums):

    if not nums:
        if "#" not in line:
            return 1
        else:
            return 0

    if not line:
        return 0

    next_character = line[0]
    next_group = nums[0]

    def pound():
        this_group = line[:next_group]
        this_group = this_group.replace("?", "#")

        if this_group != next_group * "#":
            return 0

        if len(line) == next_group:
            if len(nums) == 1:
                return 1
            else:
                return 0

        if line[next_group] in "?.":
            return solve(line[next_group+1:], nums[1:])

        return 0

    def dot():
        return solve(line[1:], nums)

    if next_character == '#':
        out = pound()

    elif next_character == '.':
        out = dot()

    elif next_character == '?':
        out = dot() + pound()

    return out

main()