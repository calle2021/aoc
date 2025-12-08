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
#puzzle = Puzzle(year=2025, day=8).input_data
junktions = [eval(x) for x in puzzle.splitlines()]
connections = []
dists = []
pairs = []
for i, x in enumerate(junktions):
    for j, y in enumerate(junktions):
        if j == i: continue
        dist = np.linalg.norm(np.array(x) - np.array(y))
        dists.append(dist)
        pairs.append((x, y))

pairs = [x for _, x in sorted(zip(dists, pairs))]

for pair in pairs:
    x, y = pair
    add = False
    for c in connections:
        if x in c or y in c:
            c.append(x)
            c.append(y)
            add = True
            break
    if not add:
        connections.append([x, y])

print(len(connections))