from aocd.models import Puzzle
puzzle = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
puzzle = Puzzle(year=2025, day=9).input_data

red = set()
for y, line in enumerate(puzzle.splitlines()):
    red.add(eval(line))
areas = []
pairs = []
green = set()
maxx = 0
maxy = 0
minx = float("inf")
miny = float("inf")
for x in red:
    maxx = max(x[0], maxx)
    maxy = max(x[1], maxy)
    minx = min(x[0], minx)
    miny = min(x[1], miny)
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
green -= red
print("OMG")
minx -= 1
miny -= 1
maxx += 1
maxy += 1
inside = set()
for x in range(minx, maxx):
    for y in range(miny, maxy):
        inside.add((x, y))

outside = set()
q = [(minx, miny)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.pop(0)

    neighbours = [(x + d[0], y + d[1]) for d in dirs]
    for next in neighbours:
        if next in red or next in green or next in outside:
            continue
        if next[0] < minx or next[0] > maxx:
            continue
        if next[1] < miny or next[1] > maxy:
            continue
        q.append(next)
        outside.add(next)
#print(outside)
inside -= outside

for x in red:
    for y in red:
        if x == y: continue
        c0 = (x[0], y[1])
        c1 =  (y[0], x[1])
        if c0 not in inside:
            continue
        if c1 not in inside:
            continue
        left = abs(x[0] - y[0]) + 1
        right = abs(x[1] - y[1]) + 1
        areas.append(left * right)
print(max(areas))
exit()
for y in range(miny, maxy):
    for x in range(minx, maxx):
        if (x, y) in red:
            print("#", end="")
        elif (x, y) in green:
            print("X", end="")
        elif (x, y) in inside:
            print("o",end="")
        else:
            print(".", end="")
    print("")
