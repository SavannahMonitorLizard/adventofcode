import copy

orders = open('inputs\\day8.txt', 'r').read().split("\n")

instructions = []

for order in orders:
    a, b = order.split(" ")
    c = [char for char in b]
    instruction = "".join(c[1:])
    instructions.append((a, c[0], int(instruction)))

acc = 0
runInstructions = []
ic = 0

while ic < len(instructions):
    a, b, c = instructions[ic]

    if ic in runInstructions:
        break

    runInstructions += [ic]

    if a == "acc":
        if b == "-":
            acc -= c
            ic += 1
        elif b == "+":
            acc += c
            ic += 1
    elif a == "nop":
        ic += 1
        continue
    elif a == "jmp":
        if b == "-":
            ic -= c
        elif b == "+":
            ic += c

print(f"Part 1: {acc}")

counter = 0

def runProgram(instructions):
    runInstructions = []
    ic = 0
    acc = 0
    while True:
        try:
            if ic in runInstructions:
                break

            runInstructions.append(ic)

            if instructions[ic].startswith('jmp'):
                ic += int(instructions[ic].split(' ')[1])

            elif instructions[ic].startswith('acc'):
                acc += int(instructions[ic].split(' ')[1])
                ic += 1
                
            else:
                ic += 1
        except:
            global counter
            counter += 1
            break
    
    return acc

for i in range(len(orders)):

    newInstructions = orders.copy()
    
    if newInstructions[i].startswith('jmp'):
        newInstructions[i] = newInstructions[i].replace('jmp', 'nop')
        runProgram(newInstructions)

    elif newInstructions[i].startswith('nop'):
        newInstructions[i] = newInstructions[i].replace('nop', 'jmp')
        runProgram(newInstructions)

    if counter == 1:
        break

print(f"Part 2: {runProgram(newInstructions)}")