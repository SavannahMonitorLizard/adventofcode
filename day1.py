nums = [int(i) for i in open('inputs\\day1.txt', 'r').readlines()]

part1 = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == 2020:
            part1 = nums[i] * nums[j]
            break

print(f"Part 1: {part1}")

part2 = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                part2 = nums[i] * nums[j] * nums[k]
                break

print(f"Part 2: {part2}")