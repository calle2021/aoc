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
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[(start, (1, 0))] = 0
while front:
    curr = heappop(front)
    cost, dir, pos = curr

    if pos == goal:
        cost_so_far[pos] = cost
        break
    neighbours = []
    if (pos[0] + dir[0], pos[1] + dir[1]) in paths:
        neighbours.append((1, dir, (pos[0] + dir[0], pos[1] + dir[1])))
    neighbours.append((1000, (dir[1], -dir[0]), pos))
    neighbours.append((1000, (-dir[1], dir[0]), pos))
    for next in neighbours:
        cost, dir, pos = next
        if pos not in paths:
            continue
        new_cost = cost_so_far[(curr[2], curr[1])] + cost
        if (pos, dir) not in cost_so_far or new_cost < cost_so_far[(pos, dir)]:
            cost_so_far[(pos, dir)] = new_cost
            priority = new_cost
            heappush(front, (priority, dir, pos))
            came_from[pos] = curr
print(cost_so_far[goal])