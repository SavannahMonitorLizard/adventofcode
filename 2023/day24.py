"""
https://adventofcode.com/2023/day/24
"""
import numpy as np
import z3

def main():
    lines = np.genfromtxt("inputs\day24.txt", delimiter=", ", dtype=np.int64)

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    total = 0
    for i, line in enumerate(lines):
        otherlines = np.delete(lines, i, axis=0)
        for oline in otherlines:
            intersect = intersection([line[0], line[1]], [line[0]+line[3], line[1]+line[4]], [oline[0], oline[1]], [oline[0]+oline[3], oline[1]+oline[4]])
            if intersect[0] >= 200000000000000 and intersect[0] <= 400000000000000:
                if intersect[1] >= 200000000000000 and intersect[1] <= 400000000000000:
                    if ((intersect[0] >= line[0] and line[3] > 0) or (intersect[0] <= line[0] and line[3] < 0)) and ((intersect[0] >= oline[0] and oline[3] > 0) or (intersect[0] <= oline[0] and oline[3] < 0)):
                        if ((intersect[1] >= line[1] and line[4] > 0) or (intersect[1] <= line[1] and line[4] < 0)) and ((intersect[1] >= oline[1] and oline[4] > 0) or (intersect[1] <= oline[1] and oline[4] < 0)):
                            total += 1

    return total // 2

def p2(lines):
    x, y, z = z3.BitVec('x', 64), z3.BitVec('y', 64), z3.BitVec('z', 64)
    vx, vy, vz = z3.BitVec('vx', 64), z3.BitVec('vy', 64), z3.BitVec('vz', 64)

    s = z3.Solver()
    for i in range(4):
        (px, py, pz, vax, vay, vaz) = lines[i]

        t = z3.BitVec(i, 64)
        s.add(t >= 0)
        s.add(x + vx * t == px + vax * t)
        s.add(y + vy * t == py + vay * t)
        s.add(z + vz * t == pz + vaz * t)

    s.check()
    m = s.model()
    x, y, z = m.eval(x), m.eval(y), m.eval(z)
    x, y, z = x.as_long(), y.as_long(), z.as_long()

    return x + y + z

def intersection(line1_point1, line1_point2, line2_point1, line2_point2):
    x1, y1 = line1_point1
    x2, y2 = line1_point2
    x3, y3 = line2_point1
    x4, y4 = line2_point2

    m1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
    m2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('inf')

    if m1 == m2:
        return (float('inf'), float('inf'))

    if m1 == float('inf'):
        x_intersection = x1
        y_intersection = m2 * (x1 - x3) + y3
    elif m2 == float('inf'):
        x_intersection = x3
        y_intersection = m1 * (x3 - x1) + y1
    else:
        x_intersection = (m1 * x1 - m2 * x3 + y3 - y1) / (m1 - m2)
        y_intersection = m1 * (x_intersection - x1) + y1

    return (x_intersection, y_intersection)

main()