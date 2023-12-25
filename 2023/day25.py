"""
https://adventofcode.com/2023/day/25
"""
import networkx as nx
import math

def main():
    with open("inputs\day25.txt") as f:
        lines = [[line.strip().split(": ")] for line in f.readlines()]

    G  = nx.Graph()
    for line in lines:
        line = line[0]
        start, dests = line[0], line[1]
        for dest in dests.split(" "):
            G.add_edge(start, dest)
            
    G.remove_edges_from(nx.minimum_edge_cut(G))
    print(math.prod(len(c) for c in nx.connected_components(G)))

main()