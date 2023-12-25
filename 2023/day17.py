"""
https://adventofcode.com/2023/day/17
"""
import sys

def main():
    with open("inputs\day17.txt") as f:
        lines = [list(map(int, [*line.strip()])) for line in f.readlines()]

    p1(lines)
    p2(lines)

def p1(grid):
    def add_state(cost, x, y, dx, dy, distance):

        x += dx
        y += dy

        if not (x in range(0, w) and y in range(0, h)):
            return
        
        new_cost = cost + grid[y][x]

        if x == x_end and y == y_end:
            print(new_cost)
            sys.exit(0)

        state = (x, y, dx, dy, distance)

        if state not in seen_cost_by_state:
            state_queues_by_cost.setdefault(new_cost, []).append(state)
            seen_cost_by_state[state] = new_cost
    
    h = len(grid)
    w = len(grid[0])
    x_end = w - 1
    y_end = h - 1

    state_queues_by_cost = {}
    seen_cost_by_state = {}

    add_state(cost=0, x=0, y=0, dx=1, dy=0, distance=1)
    add_state(cost=0, x=0, y=0, dx=0, dy=1, distance=1)

    while True:
        current_cost = min(state_queues_by_cost.keys())
        next_states = state_queues_by_cost.pop(current_cost)

        for state in next_states:
            (x, y, dx, dy, distance) = state

            add_state(cost=current_cost, x=x, y=y, dx=dy, dy=-dx, distance=1)
            add_state(cost=current_cost, x=x, y=y, dx=-dy, dy=dx, distance=1)

            if distance < 3:
                add_state(cost=current_cost, x=x, y=y, dx=dx, dy=dy, distance=distance+1)

def p2(grid):
    def add_state(cost, x, y, dx, dy, distance):

        x += dx
        y += dy

        if not (x in range(0, w) and y in range(0, h)):
            return
        
        new_cost = cost + grid[y][x]

        if x == x_end and y == y_end and distance >= 4:
            print(new_cost)
            sys.exit(0)

        state = (x, y, dx, dy, distance)

        if state not in seen_cost_by_state:
            state_queues_by_cost.setdefault(new_cost, []).append(state)
            seen_cost_by_state[state] = new_cost
    
    h = len(grid)
    w = len(grid[0])
    x_end = w - 1
    y_end = h - 1

    state_queues_by_cost = {}
    seen_cost_by_state = {}

    add_state(cost=0, x=0, y=0, dx=1, dy=0, distance=1)
    add_state(cost=0, x=0, y=0, dx=0, dy=1, distance=1)

    while True:
        current_cost = min(state_queues_by_cost.keys())
        next_states = state_queues_by_cost.pop(current_cost)

        for state in next_states:
            (x, y, dx, dy, distance) = state

            if distance >= 4:
                add_state(cost=current_cost, x=x, y=y, dx=dy, dy=-dx, distance=1)
                add_state(cost=current_cost, x=x, y=y, dx=-dy, dy=dx, distance=1)

            if distance < 10:
                add_state(cost=current_cost, x=x, y=y, dx=dx, dy=dy, distance=distance+1)

main()