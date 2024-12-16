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
# puzzle = """#################
##...#...#...#..E#
##.#.#.#.#.#.#.#.#
##.#.#.#...#...#.#
##.#.#.#.###.#.#.#
##...#.#.#.....#.#
##.#.#.#.#.#####.#
##.#...#.#.#.....#
##.#.#####.#.###.#
##.#.#.......#...#
##.#.###.#####.###
##.#.#...#.....#.#
##.#.#.#####.###.#
##.#.#.........#.#
##.#.#.#########.#
##S#.............#
##################"""
# puzzle = get_data(day=16, year=2024)

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
                print(".", end="")
            if curr in walls:
                print("#", end="")
        print("")


# print_grid()

# Dijkstra
q = []
heappush(q, (0, (1, 0), start))
cost_so_far = {}
came_from = defaultdict(set)
came_from[start] = None
cost_so_far[start] = 0
while q:
    curr = heappop(q)
    cost, dir, pos = curr

    if pos == goal:
        break

    neighbours = []
    straight = (pos[0] + dir[0], pos[1] + dir[1])
    left = (pos[0] + dir[1], pos[1] - dir[0])
    right = (pos[0] - dir[1], pos[1] + dir[0])
    if straight in paths:
        neighbours.append((1, dir, straight))
    if left in paths:
        neighbours.append((1001, (dir[1], -dir[0]), left))
    if right in paths:
        neighbours.append((1001, (-dir[1], dir[0]), right))

    for next in neighbours:
        cost, dir, pos = next
        if pos not in paths:
            continue
        new_cost = cost_so_far[curr[2]] + cost
        if pos not in cost_so_far or new_cost < cost_so_far[pos]:
            cost_so_far[pos] = new_cost
            heappush(q, (new_cost, dir, pos))
            came_from[pos] = {curr[2]}
        if pos not in cost_so_far or new_cost == cost_so_far[pos]:
            cost_so_far[pos] = new_cost
            heappush(q, (new_cost, dir, pos))
            came_from[pos].add(curr[2])
            if pos == (3, 9):
                print(curr[2], "here")

path = []
print_grid()

print(came_from[(3, 9)])
print(cost_so_far[(3, 9)])
exit()
print("PART 1", cost_so_far[goal])
q = [goal]
visited = set()
path = []
print(came_from[goal])
while q:
    curr = q.pop(0)
    if curr == None or came_from[curr] == None:
        break
    neighbors = [x for x in came_from[curr]]
    if curr == (5, 7):
        print(curr, neighbors)
        time.sleep(1)
    for next in neighbors:
        if next in visited:
            continue
        q.append(next)
        path.append(next)
print_grid()


print(came_from[(5, 7)])
