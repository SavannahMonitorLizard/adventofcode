passports = open('inputs\\day4.txt', 'r').read().split("\n\n")
for i in range(len(passports)):
    passports[i] = "".join(passports[i].split())

count = 0

# fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for passport in passports:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        count += 1

print(f"Part 1: {count}")

count = 0
lettersL = "abcdef"
lettersU = "ABCDEF"
chars = "0123456789"

for passport in passports:
    byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False, False
    for i in range(len(passport)):
        if passport[i:i+3] == "byr":
            if 1920 <= int(passport[i+4:i+8]) <= 2002:
                byr = True
        elif passport[i:i+3] == "iyr":
            if 2010 <= int(passport[i+4:i+8]) <= 2020:
                iyr = True
        elif passport[i:i+3] == "eyr":
            if (2020 <= int(passport[i+4:i+8]) and int(passport[i+4:i+8]) <= 2030):
                eyr = True
        elif passport[i:i+3] == "hgt":
            try:
                if 150 <= int(passport[i+4:i+7]) <= 193 and passport[i+7:i+9] == "cm":
                    hgt = True
            except ValueError:
                if 59 <= int(passport[i+4:i+6]) <= 76 and passport[i+6:i+8] == "in":
                    hgt = True
        elif passport[i:i+3] == "hcl":
            if not passport[i+4:i+5] == "#":
                break
            else:
                for dig in passport[i+5:i+11]:
                    if dig in lettersL or dig in lettersU or dig in chars:
                        hcl = True
        elif passport[i:i+3] == "ecl":
            if passport[i+4:i+7] == "amb" or passport[i+4:i+7] == "blu" or passport[i+4:i+7] == "brn" or passport[i+4:i+7] == "gry" or passport[i+4:i+7] == "grn" or passport[i+4:i+7] == "hzl" or passport[i+4:i+7] == "oth":
                ecl = True
        elif passport[i:i+3] == "pid":
            temp = passport[i+4:]
            try:
                if temp[9].isdigit() == True:
                    break
            except IndexError:
                pass
            try:
                if temp[8].isdigit() == False:
                    break
            except IndexError:
                pass
            try:
                for num in passport[i+4:i+13]:
                    if num not in chars:
                        break
                    pid = True
            except IndexError:
                break

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        count += 1

print(f"Part 2: {count}")