from aocd import get_data
from heapq import *
from collections import defaultdict
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
#puzzle = """#################
##...#...#...#..E#
##.#.#.#.#.#.#.#^#
##.#.#.#...#...#^#
##.#.#.#.###.#.#^#
##>>v#.#.#.....#^#
##^#v#.#.#.#####^#
##^#v..#.#.#>>>>^#
##^#v#####.#^###.#
##^#v#..>>>>^#...#
##^#v###^#####.###
##^#v#>>^#.....#.#
##^#v#^#####.###.#
##^#v#^........#.#
##^#v#^#########.#
##S#>>^..........#
##################"""
#puzzle = get_data(day=16, year=2024)

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
    for y in range(my+1):
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
#print_grid()

#Dijkstra
front = []
heappush(front, (0, (1, 0), start))
cost_so_far = {}
came_from = defaultdict(list)
came_from[start].append(None)
cost_so_far[(start, (1,0))] = 0
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
            came_from[pos].append(curr[2])
print(cost_so_far[goal])
print("here",came_from[goal])

q = [goal]
visited = set()
visited.add(goal)
count = 0
path = [goal]
while q:
    curr = q.pop(0)
    neighbours = came_from[curr]
    for next in neighbours:
        if next not in visited:
            q.append(next)
            visited.add(next)
            count += 1
            path.append(next)
print_grid()
print(count)
