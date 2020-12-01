nums = open("inputs\\day1.txt").read().split("\n")
nums.remove('')
for i in range(0, len(nums)): 
    nums[i] = int(nums[i])

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