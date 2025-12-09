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
for x in red:
    for y in red:
        if x == y: continue
        c0 = (x[0], y[1])
        c1 =  (y[0], x[1])
        green.add(c0)
        green.add(c1)

for y in range(9):
    for x in range(15):
        if (x, y) in red:
            print("#", end="")
        elif (x, y) in green:
            print("X", end="")
        else:
            print(".",end="")
    print("")