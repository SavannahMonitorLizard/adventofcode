"""
https://adventofcode.com/2023/day/12
"""
import itertools

def main():
    with open("inputs\day12.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    p1(lines)
    p2(lines)

def p1(lines) -> None:
    total = 0

    for line in lines:
        line = line.split(" ")
        orders = line[1]
        nums = [int(i) for i in orders.split(",")]
        line = [*line[0]]
        total += brute_force(line, nums)

    print(total)

def p2(lines) -> None:
    pass

def brute_force(line: str, nums: list[int]) -> int:
    gen = ("#." if letter == "?" else letter for letter in line)
    return sum(match(candidate, nums) for candidate in itertools.product(*gen))

def match(line: str, nums: list[int]) -> bool:
    return nums == [sum(1 for _ in grouper) for key, grouper in itertools.groupby(line) if key == "#"]

main()