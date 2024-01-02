from heapq import *

input = "input.txt"

rows = [row for row in open(input).read().split("\n")]
grid = {}
my = len(rows) - 1
mx = len(rows[0]) - 1
for y, row in enumerate(rows):
    for x, v in enumerate(row):
        grid[(x, y)] = int(v)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbours(curr):
    p = curr[1]
    c = curr[2]
    d = curr[3]

    s = (p[0] + d[0] , p[1] + d[1])
    l = (d[1], -d[0])
    r = (-d[1], d[0])
    left = (p[0] + l[0], p[1] + l[1])
    right = (p[0] + r[0], p[1] + r[1])
    
    ns = []
    if c < 10 and s in grid:
        ns.append((s, c + 1, d))
    if left in grid and c >= 4:
        ns.append((left, 1, l))
    if right in grid and c >= 4:
        ns.append((right, 1, r))
    return ns

start = (0, 0)
goal = (mx, my)

#A*
q = []
heappush(q, (0, start, 0, (1, 0)))
heappush(q, (0, start, 0, (0, 1)))
cost_so_far = {}
cost_so_far[(start, 0, (1, 0))]  = 0
cost_so_far[(start, 0, (0, 1))]  = 0

while q:
    curr = heappop(q)
    if curr[1] == goal:
        break
    ns = neighbours(curr)
    for next in ns:
        new_cost = cost_so_far[curr[1:]] + grid[next[0]]
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost + heuristic(goal, next[0])
            heappush(q, (priority, *next))
#part 2
print(curr[0])