passwords = open('inputs\\day2.txt', 'r').read().split("\n")
passwords.remove('')

total = 0

for i in range(len(passwords)):
    nums, password = passwords[i].split(": ")
    nums, letter = nums.split(" ")
    minV, maxV = [int(i) for i in nums.split('-')]
    count = 0

    for j in password:
        if j == letter:
            count += 1

    if minV <= count <= maxV:
        total += 1

print(f"Part 1: {total}")

total = 0

for i in range(len(passwords)):
    nums, password = passwords[i].split(": ")
    nums, letter = nums.split(" ")
    index1, index2 = [int(i) for i in nums.split('-')]

    if password[index1 - 1] == letter or password[index2 - 1] == letter:
        if not (password[index1 - 1] == letter and password[index2 - 1] == letter):
            total += 1

print(f"Part 2: {total}")