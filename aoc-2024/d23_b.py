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
    comb = list(combinations(vals, len(vals) - 1))
    combs = [(key, *c) for c in comb]
    for c in combs:
        inter = list(combinations(c[1:], 2))
        if all([x[0] in connections[x[1]] and x[1] in connections[x[0]] for x in inter]):
            lans.add(tuple(sorted([*c])))
assert len(lans) == 1
lan = list(lans).pop()
print(','.join(lan))
