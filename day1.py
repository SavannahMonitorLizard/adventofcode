nums = open("inputs\\day1.txt").read().split("\n")
nums.remove('')
for i in range(0, len(nums)): 
    nums[i] = int(nums[i])
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])
                break