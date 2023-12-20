"""
https://adventofcode.com/2023/day/19
"""
from copy import deepcopy

def main():
    with open("inputs\day19.txt") as f:
        workflow, parts = f.read().split("\n\n")

    workflow = workflow.split("\n")
    parts = [part[1:-1].split(",") for part in parts.split("\n")]
    global orders
    orders = genorders(workflow)
    parts = genparts(parts)

    # p1(parts, orders)
    p2()

def p1(parts, orders):
    total = 0
    for part in parts:
        wf = "in"
        while wf not in "AR":
            cons = orders[wf]
            for con in cons:
                if len(con) == 1:
                    wf = con[0]
                    break
                else:
                    if "<" in con[0]:
                        atb, num = con[0].split("<")
                        num = int(num)
                        if part[atb] < num:
                            wf = con[1]
                            break
                    elif ">" in con[0]:
                        atb, num = con[0].split(">")
                        num = int(num)
                        if part[atb] > num:
                            wf = con[1]
                            break

        if wf == "A":
            total += part["x"] + part["m"] + part["a"] + part["s"] 

    print(total)

def p2():
    ranges = {"x": range(1, 4001), "m": range(1, 4001), "a": range(1, 4001), "s": range(1, 4001)}
    print(pruneranges(ranges, "in"))

def genorders(workflow):
    orders = {}
    for order in workflow:
        wf, con = order.split("{")
        con = con[:-1]
        cons = con.split(",")
        cons = [con.split(":") for con in cons]
        orders[wf] = cons

    return orders

def genparts(parts):
    dictparts = []
    for part in parts:
        p = {}
        for atb in part:
            p[atb[0]] = int(atb[2:])

        dictparts.append(p)

    return dictparts

def pruneranges(ranges, wf):
    if wf == "A":
        return len(ranges["x"]) * len(ranges["m"]) * len(ranges["a"]) * len(ranges["s"])
    elif wf == "R":
        return 0
    
    total = 0
    cons = orders[wf]
    for con in cons:
        if len(con) == 1:
            total += pruneranges(ranges, con[0])
        else:
            if "<" in con[0]:
                lhs, rhs = con[0].split("<")
                
                branch_true = range(ranges[lhs].start, int(rhs))
                branch_false = range(int(rhs), ranges[lhs].stop)
                range_true = deepcopy(ranges)
                range_true[lhs] = branch_true
                ranges[lhs] = branch_false
                
                total += pruneranges(range_true, con[1])
            elif ">" in con[0]:
                lhs, rhs = con[0].split(">")
                
                branch_true = range(int(rhs)+1, ranges[lhs].stop)
                branch_false = range(ranges[lhs].start, int(rhs)+1)
                range_true = deepcopy(ranges)
                range_true[lhs] = branch_true
                ranges[lhs] = branch_false
                
                total += pruneranges(range_true, con[1])

    return total

main()