"""
https://adventofcode.com/2023/day/22
"""
import numpy as np
import itertools

def main():
    # with open("inputs\day22p.txt") as f:
    #     lines = [line.strip() for line in f.readlines()]

    # with open("inputs\day22c.txt", "w") as f:
    #     for line in lines:
    #         f.write(line.replace("~", ",") + "\n")

    # bricks = np.genfromtxt("inputs\day22c.txt", delimiter=",")
    # bricks = bricks[np.argsort(bricks[:,2])]
    bricks = np.genfromtxt("inputs\day22cm.txt", delimiter=",")

    bricks = fall(bricks)

    print(p1(bricks))
    print(p2(bricks))

def p1(bricks):
    total = 0

    for i, _ in enumerate(bricks):
        print(i)
        newbricks = np.vstack((bricks[:i], bricks[i+1:]))
        if not canfall(newbricks):
            total += 1

    return total

def p2(bricks):
    # fallbricks = []
    # fallbricki = []

    # for i, brick in enumerate(bricks):
    #     # print(i)
    #     newbricks = np.vstack((bricks[:i], bricks[i+1:]))
    #     if canfall(newbricks):
    #         # fallbricks.append(brick)
    #         fallbricki.append(i)

    # fallbricki = np.array(fallbricki)
    # np.savetxt("inputs\day22fbi.txt", fallbricki, delimiter=",")
    fallbricki = np.genfromtxt("inputs\day22fbi.txt", delimiter=",")
    # print(fallbricki)
    # print(len(fallbricki))

    total = 0
    for i in fallbricki:
        i = int(i)
        newbricks = bricks
        newbricks = np.delete(newbricks, i, axis=0)
        inx = canfall2(newbricks)
        while inx != -1:
            total += 1
            newbricks = np.delete(newbricks, inx, axis=0)
            inx = canfall2(newbricks)

        print(i)

    return total

def fall(bricks):
    while True:
        cont = False
        for i, _ in enumerate(bricks):
            # print(i)
            newbricks = bricks
            newbricks = np.vstack((newbricks[:i], newbricks[i+1:]))
            # print(newbricks)
            # print(newbricks[:,5] == bricks[i,2] - 1)
            while not np.any(newbricks[:,5] == bricks[i,2] - 1) and bricks[i,2] > 1:
                cont = True
                bricks[i,2] -= 1
                bricks[i,5] -= 1

            f = True
            while np.any(newbricks[:,5] == bricks[i,2] - 1) and bricks[i,2] > 1 and f:
                conflicts = newbricks[newbricks[:,5] == bricks[i,2] - 1]
                for conflict in conflicts:
                    x_conf = set(range(int(conflict[0]), int(conflict[3]+1)))
                    x_brick = set(range(int(bricks[i,0]), int(bricks[i,3]+1)))
                    y_conf = set(range(int(conflict[1]), int(conflict[4]+1)))
                    y_brick = set(range(int(bricks[i,1]), int(bricks[i,4]+1)))
                    xy_conf = set(itertools.product(x_conf, y_conf))
                    xy_brick = set(itertools.product(x_brick, y_brick))
                    # print(xy_conf)
                    # print(xy_brick)
                    if len(set.intersection(set(xy_conf), set(xy_brick))) != 0:
                        f = False
                if f:
                    cont = True
                    bricks[i,2] -= 1
                    bricks[i,5] -= 1

        if not cont:
            break

    return bricks

def canfall(bricks):
    for i, _ in enumerate(bricks):
        # print(i)
        newbricks = bricks
        newbricks = np.vstack((newbricks[:i], newbricks[i+1:]))
        # print(newbricks)
        # print(newbricks[:,5] == bricks[i,2] - 1)
        while not np.any(newbricks[:,5] == bricks[i,2] - 1) and bricks[i,2] > 1:
            return True

        f = True
        while np.any(newbricks[:,5] == bricks[i,2] - 1) and bricks[i,2] > 1 and f:
            conflicts = newbricks[newbricks[:,5] == bricks[i,2] - 1]
            for conflict in conflicts:
                # print(conflict)
                x_conf = set(range(int(conflict[0]), int(conflict[3]+1)))
                x_brick = set(range(int(bricks[i,0]), int(bricks[i,3]+1)))
                y_conf = set(range(int(conflict[1]), int(conflict[4]+1)))
                y_brick = set(range(int(bricks[i,1]), int(bricks[i,4]+1)))
                xy_conf = set(itertools.product(x_conf, y_conf))
                xy_brick = set(itertools.product(x_brick, y_brick))
                # print(xy_conf)
                # print(xy_brick)
                if len(set.intersection(set(xy_conf), set(xy_brick))) != 0:
                    f = False
            if f:
                return True

    return False

def canfall2(bricks):
    for i, _ in enumerate(bricks):
        # print(i)
        newbricks = bricks
        newbricks = np.vstack((newbricks[:i], newbricks[i+1:]))
        # print(newbricks)
        # print(newbricks[:,5] == bricks[i,2] - 1)
        if not np.any(newbricks[:,5] == bricks[i,2] - 1) and bricks[i,2] > 1:
            return i

        f = True
        if np.any(newbricks[:,5] == bricks[i,2] - 1) and bricks[i,2] > 1:
            conflicts = newbricks[newbricks[:,5] == bricks[i,2] - 1]
            x_brick = set(range(int(bricks[i,0]), int(bricks[i,3]+1)))
            y_brick = set(range(int(bricks[i,1]), int(bricks[i,4]+1)))
            xy_brick = set(itertools.product(x_brick, y_brick))

            for conflict in conflicts:
                # print(conflict)
                x_conf = set(range(int(conflict[0]), int(conflict[3]+1)))
                y_conf = set(range(int(conflict[1]), int(conflict[4]+1)))
                xy_conf = set(itertools.product(x_conf, y_conf))
                # print(xy_conf)
                # print(xy_brick)
                if len(set.intersection(set(xy_conf), set(xy_brick))) != 0:
                    f = False
            if f:
                return i

    return -1

main()