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
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

## connect intersections with more than 2 connections
intersections = [g for g in grid if sum([1 for d in dirs if (g[0] + d[0], g[1] + d[1]) in grid]) > 2 ]
intersections.append(start)
intersections.append(goal)

## finding the distance from each intersection to all other intersections
map = {i : {} for i in intersections}
for i in intersections:
    q = [(0, i)]
    visited = set()
    visited.add(i)

    while q:
        dst, node = q.pop(0)
        if dst and node in intersections:
            map[i][node] = dst
            continue
        for d in dirs:
            n = (node[0] + d[0], node[1] + d[1])
            if n in grid and n not in visited:
                q.append((dst + 1, n))
                visited.add(n)

def hike(path, cost, curr):
    if curr == goal:
        return cost
    res = 0
    for next in map[curr]:
        if next in path:
            continue
        res = max(res, hike(path + [next], cost + map[curr][next], next))
    return res

res = hike([], 0, start)
print(res)
