from aocd import get_data
from collections import defaultdict
from itertools import combinations

puzzle = get_data(day=23, year=2024)

connections = defaultdict(list)
for connection in puzzle.split("\n"):
    c1, c2 = connection.split("-")
    connections[c1].append(c2)
    connections[c2].append(c1)

lans = set()
for key, vals in connections.items():
    comb = list(combinations(vals, 2))
    combs = [(key, c[0], c[1]) for c in comb]
    for c in combs:
        x, y, z = c
        if y in connections[z] and z in connections[y] and any([x[0] == "t" for x in [x, y, z]]):
            lans.add(tuple(sorted([x, y, z])))
print(len(lans))