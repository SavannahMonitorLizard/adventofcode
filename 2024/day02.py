def main():
    with open("inputs\day02.txt") as f:
        lines = [line.strip().split(" ") for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0
    rows = []
    for line in lines:
        rows.append(line)

    for row in rows:
        rev = False
        safe = True
        if int(row[0]) > int(row[-1]):
            rev = True

        if row == ['2', '3', '4', '7', '9', '10']:
            print(rev)
        if not rev:
            for i in range(len(row) - 1):
                if int(row[i+1]) - int(row[i]) > 3 or int(row[i + 1]) - int(row[i]) < 1:
                    safe = False
        else:
            for i in range(len(row) - 1):
                if int(row[i + 1]) - int(row[i]) < -3 or int(row[i + 1]) - int(row[i]) > -1:
                    safe = False

        if row[0] == row[-1]:
            safe = False

        if safe:
            total += 1

    return total

def p2(lines):
    total = 0
    rows = []
    for line in lines:
        rows.append(line)

    for row in rows:
        rev = False
        safes = []
        for i in range(len(row)):
            safe = True
            new_row =  row[:i] + row[i+1:]
            if int(new_row[0]) > int(new_row[-1]):
                rev = True

            if not rev:
                for j in range(len(new_row) - 1):
                    if int(new_row[j+1]) - int(new_row[j]) > 3 or int(new_row[j + 1]) - int(new_row[j]) < 1:
                        safe = False
            else:
                for j in range(len(new_row) - 1):
                    if int(new_row[j + 1]) - int(new_row[j]) < -3 or int(new_row[j + 1]) - int(new_row[j]) > -1:
                        safe = False

            safes.append(safe)

        if any(safes):
            safe = True

        if safe:
            total += 1

    return total

main()