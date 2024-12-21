from aocd import get_data
from heapq import *

puzzle = get_data(day=20, year=2024)

paths = set()
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = (x, y)
        if col == "#":
            continue
        paths.add(curr)
        if col == "S":
            start = curr
        if col == "E":
            goal = curr

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

curr = start
path = [start]
cache = {}
cache[start] = 0
cost = 0
while True:
    x, y = curr
    for dx, dy in dirs:
        pos = (x + dx, y + dy)
        if pos in path or pos not in paths:
            continue
        next = pos
        break
    cost += 1
    path.append(next)
    cache[next] = cost
    curr = next
    if next == goal:
        break
best = cache[goal]

for mcheat in [2, 20]:
    cheats = [
        (x, y, abs(x) + abs(y))
        for x in range(-mcheat, mcheat + 1)
        for y in range(-mcheat, mcheat + 1)
        if abs(x) + abs(y) <= mcheat
    ]
    msaved = 100
    saved = 0
    for pos in path:
        x, y = pos
        neighbours = []
        for cheat in cheats:
            cx, cy, cd = cheat
            cpos = (x + cx, y + cy)
            if cpos in paths:
                neighbours.append((cpos, cd))
        for next in neighbours:
            npos, nd = next
            dist = cache[pos] + nd + best - cache[npos]
            if best - dist >= msaved:
                saved += 1
    print(saved)
