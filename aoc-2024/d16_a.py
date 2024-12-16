from aocd import get_data
from heapq import *

puzzle = get_data(day=16, year=2024)

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

front = []
heappush(front, (0, (1, 0), start))
cost_so_far = {}
cost_so_far[((1, 0), start)] = 0
while front:
    curr = heappop(front)
    cost, dir, pos = curr

    if pos == goal:
        cost_so_far[pos] = cost
        break
    neighbours = []
    straight = (pos[0] + dir[0], pos[1] + dir[1])
    if straight in paths:
        neighbours.append((1, dir, straight))
    neighbours.append((1000, (dir[1], -dir[0]), pos))
    neighbours.append((1000, (-dir[1], dir[0]), pos))
    for next in neighbours:
        ncost, ndir, npos = next
        new_cost = cost_so_far[(dir, pos)] + ncost
        if (ndir, npos) not in cost_so_far or new_cost < cost_so_far[(ndir, npos)]:
            cost_so_far[(ndir, npos)] = new_cost
            heappush(front, (new_cost, ndir, npos))
print(cost_so_far[goal])