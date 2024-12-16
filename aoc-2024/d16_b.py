from aocd import get_data
from heapq import *
from collections import defaultdict
import time

puzzle = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
puzzle = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
puzzle = get_data(day=16, year=2024)

paths = set()
walls = set()
mx = 0
my = 0
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        mx = max(x, mx)
        my = max(y, my)
        curr = (x, y)
        if col == "#":
            walls.add(curr)
            continue
        paths.add(curr)
        if col == "S":
            start = curr
        if col == "E":
            goal = curr


def print_grid():
    for y in range(my + 1):
        for x in range(mx + 1):
            curr = (x, y)
            if curr in path:
                print("O", end="")
                continue
            if curr == start:
                print("S", end="")
                continue
            if curr == goal:
                print("E", end="")
                continue
            if curr in paths:
                print(" ", end="")
            if curr in walls:
                print(" ", end="")
        print("")

q = []
heappush(q, (0, (1, 0), start))
cost_so_far = {}
came_from = defaultdict(set)
came_from[start].add(None)
cost_so_far[((1, 0), start)] = 0
while q:
    curr = heappop(q)
    cost, dir, pos = curr
    if pos == goal:
        cost_so_far[goal] = cost
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
        if (ndir, npos) not in cost_so_far or new_cost <= cost_so_far[(ndir, npos)]:
            cost_so_far[(ndir, npos)] = new_cost
            heappush(q, (new_cost, ndir, npos))
            came_from[npos].add(pos)

path = []
print_grid()

print(cost_so_far[goal])

q = [goal]
visited = set()
path = []
while q:
    curr = q.pop(0)
    if curr == None or came_from[curr] == None:
        break
    neighbors = []
    for x in came_from[curr]:
        if x == curr:
            continue
        neighbors.append(x)
    for next in neighbors:
        if next in visited:
            continue
        q.append(next)
        visited.add(next)
        path.append(next)
print_grid()
print(len(path))

