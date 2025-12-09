from aocd.models import Puzzle
puzzle = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
#puzzle = Puzzle(year=2025, day=9).input_data

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
green -= red
inside = set()
areas = []
def walk(curr):

for x in red:
    for y in red:
        if x == y: continue
        c0 = (x[0], y[1])
        c1 =  (y[0], x[1])
        c0_valid = c0 in redandgreen
        c1_valid = c1 in redandgreen
        
        left = abs(x[0] - y[0]) + 1
        right = abs(x[1] - y[1]) + 1
        areas.append(left * right)
print(max(areas ))
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
