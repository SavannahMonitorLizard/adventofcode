"""
https://adventofcode.com/2023/day/23
"""
import numpy as np

def main():
    with open("inputs\day23.txt") as f:
        grid = np.array([[*line.strip()] for line in f.readlines()])

    print(p1(grid))
    print(p2(grid))

    # 6258

def p1(grid):
    def isvalid(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != "#"
    
    w = len(grid[0])
    h = len(grid)

    start = (0, 1)
    end = (h - 1, w - 2)

    intersections = [start, end]

    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if grid[r][c] == "#":
                continue
            n = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if isvalid(nr, nc):
                    n += 1
            if n >= 3:
                intersections.append((r, c))

    nodes = {point: {} for point in intersections}

    dirs = {".": [(-1, 0), (1, 0), (0, -1), (0, 1)], "^": [(-1, 0)], "v": [(1, 0)], "<": [(0, -1)], ">": [(0, 1)]}

    for sr, sc in intersections:
        points = [(0, sr, sc)]
        visited = {(sr, sc)}

        while points:
            n, r, c = points.pop()
            
            if n != 0 and (r, c) in intersections:
                nodes[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in dirs[grid[r][c]]:
                nr = r + dr
                nc = c + dc

                if isvalid(nr, nc) and (nr, nc) not in visited:
                    points.append((n + 1, nr, nc))
                    visited.add((nr, nc))

    def search(pt):
        if pt == end:
            return 0
        
        m = -float("inf")

        for npt in nodes[pt]:
            m = max(m, search(npt) + nodes[pt][npt])

        return m
    
    return search(start)

def p2(grid):
    def isvalid(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != "#"
    
    w = len(grid[0])
    h = len(grid)

    start = (0, 1)
    end = (h - 1, w - 2)

    intersections = [start, end]

    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if grid[r][c] == "#":
                continue
            n = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if isvalid(nr, nc):
                    n += 1
            if n >= 3:
                intersections.append((r, c))

    nodes = {point: {} for point in intersections}

    for sr, sc in intersections:
        points = [(0, sr, sc)]
        visited = {(sr, sc)}

        while points:
            n, r, c = points.pop()
            
            if n != 0 and (r, c) in intersections:
                nodes[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if isvalid(nr, nc) and (nr, nc) not in visited:
                    points.append((n + 1, nr, nc))
                    visited.add((nr, nc))

    visited = set()
    def search(pt):
        if pt == end:
            return 0
        
        m = -float("inf")

        visited.add(pt)
        for npt in nodes[pt]:
            if npt not in visited:
                m = max(m, search(npt) + nodes[pt][npt])
        visited.remove(pt)

        return m
    
    return search(start)

main()