from aocd import get_data
from heapq import *
from collections import defaultdict

puzzle = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
#puzzle = get_data(day=20, year=2024)

grid = set()
path = set()
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = (x , y)
        grid.add(curr)
        if col == "#":
            continue
        path.add(curr)
        if col == "S":
            start = curr
        if col == "E":
            goal = curr
            
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = []
heappush(q, (0, start))
cache = {}
cache[start] = 0
while q:
    cost, curr = heappop(q)
    x, y = curr
    if curr == goal:
        break

    neighbours = []
    for dx, dy in dirs:
        pos = (x + dx, y + dy)
        if pos in path:
            neighbours.append(pos)
    for next in neighbours:
        new_cost = cache[curr] + 1
        if next not in cache or new_cost < cache[next]:
            cache[next] = new_cost
            heappush(q, (new_cost, next))
best = cache[goal]
print(best)
q = [(0, 0, -1, start)]
# priority que with cheat?
cost_so_far = defaultdict(list)
cost_so_far[start].append(0)
max_cheat = 20
while q:
    cost, cheat, prev, curr = q.pop(0)
    x, y = curr

    if cheat == max_cheat and curr not in path:
        continue
    if cheat == max_cheat:
        cost_so_far[goal].append(cost + best - cache[curr])
        continue
    if curr == goal:
        continue
    
    neighbours = []
    for dx, dy in dirs:
        pos = (x + dx, y + dy)
        if pos == prev:
            continue
        if cheat < max_cheat and pos in grid:
            neighbours.append((cost + 1, cheat + 1, curr, pos))
        if pos in path and curr in path:
            neighbours.append((cost + 1, cheat, curr, pos))
    for next in neighbours:
        ncost, ncheat, nprev, npos = next
        q.append((ncost, ncheat, nprev, npos))
        cost_so_far[npos].append(ncost)

count = defaultdict(int)
for x in cost_so_far[goal]:
    diff = best - x
    if diff > 0:
        count[diff] += 1
for c in count.items():
    print(c)
exit() 
count = 0
for x in cost_so_far[goal]:
    diff = best - x
    if diff >= 100:
        count += 1
print(count - 1)