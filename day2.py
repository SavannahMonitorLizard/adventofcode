passwords = open('inputs\\day2.txt', 'r').read().split("\n")
passwords.remove('')

temp = []
temp2 = []
temp3 = []
count = 0
total = 0

for i in range(len(passwords)):
    temp = passwords[i].split(": ")
    temp2 = temp[0].split(" ")
    temp3 = temp2[0].split("-")
    temp3[0] = int(temp3[0])
    temp3[1] = int(temp3[1])
    count = 0

    password = temp[1]
    letter = temp2[1]
    index1 = temp3[0]
    index2 = temp3[1]

    for j in password:
        if j == letter:
            count += 1

    if count >= index1 and count <= index2:
        total += 1

print(f"part 1: {total}")

temp = []
temp2 = []
temp3 = []
count = 0
total = 0

for i in range(len(passwords)):
    temp = passwords[i].split(": ")
    temp2 = temp[0].split(" ")
    temp3 = temp2[0].split("-")
    temp3[0] = int(temp3[0])
    temp3[1] = int(temp3[1])
    count = 0

    password = temp[1]
    letter = temp2[1]
    index1 = temp3[0]
    index2 = temp3[1]

    if password[index1 - 1] == letter or password[index2 - 1] == letter:
        if not (password[index1 - 1] == letter and password[index2 - 1] == letter):
            total += 1

print(f"part 2: {total}")