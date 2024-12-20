from aocd import get_data
from heapq import *
from collections import defaultdict
import time

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
# puzzle = get_data(day=20, year=2024)

grid = set()
path = set()
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = (x, y)
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


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


s = time.time()
best = cache[goal]
q = []
heappush(q, (0, 0, 0, [-1], start))
saved_so_far = []
mcheat = 20
msaved = 50
while q:
    prio, cost, cheat, prev, curr = heappop(q)
    x, y = curr

    if cheat == mcheat and curr not in path:
        continue
    if cheat == mcheat:
        cost = cost + best - cache[curr]
        saved = best - cost
        if saved >= msaved:
            saved_so_far.append(saved)
        continue
    if curr == goal and best - cost < msaved:
        break

    neighbours = []
    for dx, dy in dirs:
        pos = (x + dx, y + dy)
        nprev = prev + [curr]
        if pos in prev:
            continue
        if cheat < mcheat and pos in grid:
            neighbours.append((cost + 1, cheat + 1, nprev[0:20], pos))
            continue
        if pos in path:
            neighbours.append((cost + 1, cheat, nprev[0:20], pos))
    for next in neighbours:
        ncost, ncheat, nprev, npos = next
        heappush(q, (ncost + manhattan(curr, npos), ncost, ncheat, nprev, npos))

print(len(saved_so_far))
print(time.time() - s)
