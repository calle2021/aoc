from aocd import get_data

from heapq import *

puzzle = get_data(day=18, year=2024)

grid = set()
w = h = 71
for y in range(h):
    for x in range(w):
        grid.add((x , y))

for i, x in enumerate(puzzle.split("\n")):
    if i == 1024:
        break
    curr = eval(x)
    grid.remove(curr)

dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
bytes = [eval(x) for x in puzzle.split("\n")][1024:]

for b in bytes:
    grid.remove(b)
    paths = grid.copy()

    q = []
    start = (0, 0)
    heappush(q, (0, start))
    cost_so_far = {}
    cost_so_far[start] = 0
    goal = (w - 1, h - 1)
    while q:
        curr = heappop(q)
        x, y = curr[1]

        if curr[1] == goal:
            break
        neighbours = []
        for dx, dy in dirs:
            pos = (x + dx, y + dy)
            if pos in paths:
                neighbours.append(pos)
        for next in neighbours:
            new_cost = cost_so_far[curr[1]] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heappush(q, (new_cost, next))

    if goal not in cost_so_far:
        print(b)
        break
    