"""
https://adventofcode.com/2023/day/20
"""
def main():
    with open("inputs\day20p.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    md, td = parselines(lines)
    print(md)
    print(td)
    
    print(p1(lines))
    print(p2(lines))

def p1(lines):
    pass

def p2(lines):
    pass

def parselines(lines):
    moddict = {}
    typedict = {}
    for line in lines:
        module, dest = line.split(" -> ")
        if module[0] in "%&":
            typedict[module[1:]] = module[0]
        else:
            typedict[module] = "bc"
        if ", " in dest:
            dest = dest.split(", ")
        moddict[module[1:]] = dest

    return moddict, typedict

main()