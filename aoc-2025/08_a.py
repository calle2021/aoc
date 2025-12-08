from aocd.models import Puzzle
import numpy as np
puzzle = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
puzzle = Puzzle(year=2025, day=8).input_data
junktions = [eval(x) for x in puzzle.splitlines()]
connections = []
dists = []
pairs = []
def euc(x, y):
    return np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)
for i, x in enumerate(junktions):
    for j, y in enumerate(junktions):
        if j == i: continue
        add = sorted((x, y))
        if add in pairs: continue
        dist = euc(x, y)
        dists.append(dist)
        pairs.append(add)
pairs = [x for _, x in sorted(zip(dists, pairs))]
dists = sorted(dists)
for k in range(10):
    x, y = pairs[k]
    ids = []
    for i, c in enumerate(connections):
        if x in c or y in c:
            ids.append(i)
    if not ids:
        connections.append({x ,y})
        continue
    i = ids[0]
    if len(ids) == 1:
        connections[i].add(x)
        connections[i].add(y)
        continue
    connections[i].add(x)
    connections[i].add(y)
    updated = []
    circ = set()
    for j in ids:
        circ |= connections[j]
    for j in range(len(connections)):
        if j in ids:
            continue
        updated.append(connections[j])
    updated.append(circ)
    connections = updated
lens = sorted([len(x) for x in connections])
print(lens[-1] * lens[-2] * lens[-3])
