from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=9).input_data

red = set()
for y, line in enumerate(puzzle.splitlines()):
    red.add(eval(line))
areas = []
pairs = []
green = set()
minx = float("inf")
maxx = 0
miny = float("inf")
maxy = 0
for x in red:
    minx = min(minx, x[0])
    maxx = max(maxx, x[0])
    miny = min(miny, x[1])
    maxy = max(maxy, x[1])
    for y in red:
        if x == y: continue
        c0 = (x[0], y[1])
        c1 =  (y[0], x[1])
        if (x[1] == y[1]):
            for i in range(x[0], y[0]):
                green.add((i, x[1]))
        if (x[0] == y[0]):
            for i in range(x[1], y[1]):
                green.add((x[0], i))
bounds = red | green

outside = set()
maxx += 1
maxy += 1
minx -= 1
miny -= 1

start = min(bounds)
q = [start]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
adirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

while q:
    x, y = q.pop(0)
    neighbours = [(x + d[0], y + d[1]) for d in dirs]
    for next in neighbours:
        if next in bounds or next in outside:
            continue
        if next[0] < minx or next[0] > maxx:
            continue
        if next[1] < miny or next[1] > maxy:
            continue
        adj = {(next[0] + d[0], next[1] + d[1]) for d in adirs}
        if not adj & bounds:
            continue
        q.append(next)
        outside.add(next)

def walkx(start, dest):
    diff = dest[0] - start[0]
    if diff == 0:
        return False
    d = int(diff / abs(diff))
    curr = start
    while curr != dest:
        curr = (curr[0] + d, curr[1])
        if curr in outside:
            return False
    return True

def walky(start, dest):
    diff = dest[1] - start[1]
    if diff == 0:
        return False
    d = int(diff / abs(diff))
    curr = start
    while curr != dest:
        curr = (curr[0], curr[1] + d)
        if curr in outside:
            return False
    return True

red = list(red)
area = 0
i = 0
for c0 in red:
    for c1 in red:
        if c0 == c1: continue
        c2 = (c0[0], c1[1])
        c3 = (c1[0], c0[1])
        res = False
        if not walky(c0, c2): continue
        if not walkx(c0, c3): continue
        if not walkx(c1, c2): continue
        if not walky(c1, c3): continue
        left = abs(c0[0] - c1[0]) + 1
        right = abs(c0[1] - c1[1]) + 1
        area = max(area, left * right)
    i += 1
print(area)
