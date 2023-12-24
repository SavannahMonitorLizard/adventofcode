"""
https://adventofcode.com/2023/day/20
"""
from collections import deque
import math
from itertools import count

def main():
    with open("inputs\day20.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    ff = {}
    con = {}
    mods = {}

    for line in lines:
        source, dests = line.split('->')
        source = source.strip()
        dests = dests.strip().split(', ')

        if source[0] == '%':
            source = source[1:]
            ff[source] = False
        elif source[0] == '&':
            source = source[1:]
            con[source] = {}

        mods[source] = dests

    for source, dests in mods.items():
        for dest in dests:
            if dest in con:
                con[dest][source] = False
    
    print(p1(mods, ff, con))
    print(p2(mods, ff, con))

def p1(mods, ff, con):
    thi = 0
    tlo = 0
    for _ in range(1000):
        hi, lo = solve(mods, ff, con)
        thi += hi
        tlo += lo

    return thi * tlo

def p2(mods, ff, con):
    for f in ff:
        ff[f] = False

    for inputs in con.values():
        for i in inputs:
            inputs[i] = False

    return math.lcm(*findperiods(mods, ff, con))

def solve(mods, ff, con):
    q = deque([('button', 'broadcaster', False)])
    nhi = 0
    nlo = 0

    while q:
        sender, receiver, pulse = q.popleft()
        nhi += pulse
        nlo += not pulse
        q.extend(propagate(mods, ff, con, sender, receiver, pulse))

    return nhi, nlo

def propagate(mods, ff, con, sender, receiver, pulse):
    if receiver in ff:
        if pulse:
            return
        next_pulse = ff[receiver] = not ff[receiver]
    elif receiver in con:
        con[receiver][sender] = pulse
        next_pulse = not all(con[receiver].values())
    elif receiver in mods:
        next_pulse = pulse
    else:
        return

    for new_receiver in mods[receiver]:
        yield receiver, new_receiver, next_pulse

def findperiods(mods, ff, con):
    periodic = set()

    for rx_source, dests in mods.items():
        if dests == ['rx']:
            break

    for source, dests in mods.items():
        if rx_source in dests:
            periodic.add(source)

    for i in count(1):
        q = deque([('button', 'broadcaster', False)])

        while q:
            sender, receiver, pulse = q.popleft()

            if not pulse:
                if receiver in periodic:
                    yield i

                    periodic.discard(receiver)
                    if not periodic:
                        return

            q.extend(propagate(mods, ff, con, sender, receiver, pulse))

main()