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
topleft = (float("inf"), float("inf"))
for x in red:
    maxx = max(x[0], maxx)
    maxy = max(x[1], maxy)
    minx = min(x[0], minx)
    miny = min(x[1], miny)
    topleft = min(topleft, x)
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
redandgreen = red | green
print(topleft)
topleft = (topleft[0] - 1, topleft[1] - 1)
green -= red
inside = set()

## walk on the ouside of if
print(minx, maxx, miny, maxy)
start = ((maxx- minx)// 2 + minx, (maxy - miny) // 2 + miny)
inside = set()
q = [start]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.pop(0)
    print(x, y)
    neighbours = [(x + d[0], y + d[1]) for d in dirs]
    for next in neighbours:
        if next in red or next in green or next in inside:
            continue
        q.append(next)
        inside.add(next)
inside |= red
inside |= green
areas = []
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
for y in range(miny - 2, maxy + 4):
    for x in range(minx - 2, maxx + 4):
        if (x, y) == start:
            print("S", end="")
        elif (x, y) in red:
            print("#", end="")
        elif (x, y) in green:
            print("X", end="")
        elif (x, y) in inside:
            print("o",end="")
        else:
            print(".", end="")
    print("")
