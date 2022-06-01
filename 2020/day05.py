passes = open('inputs\\day5.txt', 'r').read().split("\n")

largestID = 0

for bpass in passes:
    seatId = 0
    seats = [i for i in range(128)]
    columns = [i for i in range(8)]
    for letter in bpass:
        if letter == "B":
            seats = seats[len(seats)//2:]
        elif letter == "F":
            seats = seats[:len(seats)//2]
        elif letter == "R":
            columns = columns[len(columns)//2:]
        elif letter == "L":
            columns = columns[:len(columns)//2]

    row = seats[0]
    column = columns[0]

    seatId = (row * 8) + column
    if seatId > largestID:
        largestID = seatId

print(f"Part 1: {largestID}")

bpasses = []
yourSeat = 0

for bpass in passes:
    seatId = 0
    seats = [i for i in range(128)]
    columns = [i for i in range(8)]
    for letter in bpass:
        if letter == "B":
            seats = seats[len(seats)//2:]
        elif letter == "F":
            seats = seats[:len(seats)//2]
        elif letter == "R":
            columns = columns[len(columns)//2:]
        elif letter == "L":
            columns = columns[:len(columns)//2]

    row = seats[0]
    column = columns[0]

    seatId = (row * 8) + column
    bpasses += [seatId]

for seat in bpasses:
    if seat + 1 not in bpasses:
        yourSeat = seat + 1

print(f"Part 2: {yourSeat}")