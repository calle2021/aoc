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
redandgreen = red | green

red = list(red)
areas = []
asd = 0
def walk(curr):
    count = 0
    for x in range(curr[0], maxx + 1):
        if (x, curr[1]) in redandgreen:
            count[0] = 1
            break
    for x in range(minx - 1, curr[0]):
        if (x, curr[1]) in redandgreen:
            count[1] = 1
            break
    for y in range(curr[1], maxy + 1):
        if (curr[0], y) in redandgreen:
            count[2] = 1
            break
    for y in range(miny - 1, curr[1]):
        if (curr[0], y) in redandgreen:
            count[3] = 1
            break
    return sum(count) == 4

areas = []
for x in red[::2]:
    for y in red[1::2]:
        if x == y: continue
        c0 = (x[0], y[1])
        c1 =  (y[0], x[1])
        c0_valid = c0 in redandgreen
        if not c0_valid:
            c0_valid = walk(c0)
        c1_valid = c1 in redandgreen
        if not c1_valid:
            c1_valid = walk(c1)
        if not c1_valid or not c0_valid:
            continue
        left = abs(x[0] - y[0]) + 1
        right = abs(x[1] - y[1]) + 1
        area = left * right
        areas.append(area)
        areas = sorted(areas)
        if len(areas) == 3:
            areas.pop(0)
    asd += 1
print(areas)
exit()
for y in range(9):
    for x in range(15):
        if (x, y) in red:
            print("#", end="")
        elif (x, y) in green:
            print("X", end="")
        elif (x, y) in inside:
            print("o",end="")
        else:
            print(".", end="")
    print("")
