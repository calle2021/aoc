import sys
sys.setrecursionlimit(3000)

input = "input.txt"

rows = open(input).read().splitlines()
grid = {}
mx = len(rows[0]) - 1
my = len(rows) - 1
for y, row in enumerate(rows):
    for x, tile in enumerate(row):
        if tile != "#":
            grid[(x, y)] = tile

start = (1, 0)
goal = (mx - 1, my)

dirs = {
        "." : [(1, 0), (-1, 0), (0, 1), (0, -1)],
        ">" : [(1, 0)],
        "<" : [(-1, 0)],
        "^" : [(0, -1)],
        "v" : [(0, 1)]
        }

def hike(path, curr):
    if curr == goal:
        return len(path)
    possible = []
    for d in dirs[grid[curr]]:
        next = (curr[0] + d[0], curr[1] + d[1])
        if next in grid and next not in path:
            possible.append(next)
    if not possible:
        return 0
    res = 0
    for pos in possible:
        res = max(res, hike(path + [pos], pos))

    return res

res = hike([], start)
print(res)