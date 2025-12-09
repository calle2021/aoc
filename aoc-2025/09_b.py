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
    x, y = eval(line)
    red.add(x + y * 1j)

green = set()
for x in red:
    for y in red:
        if x == y: continue
        c0 = (x.real, y.imag)
        c1 =  (y.real, x.imag)
        if (x.imag == y.imag):
            for i in range(int(x.real), int(y.real)):
                green.add(i + x.imag * 1j)
        if (x.real == y.real):
            for i in range(int(x.imag), int(y.imag)):
                green.add(x.real + i * 1j)

bounds = red | green

dir = -1j
right = 1

start = 0
for x in bounds:
    start = x
    break
curr = start
inside = set()
while True:
    next = curr + dir
    if next in bounds:
        print(next)
        break
    dir *= 1j
    right *= 1j
    if curr == start:
        break

for i in range(9):
    for j in range(15):
        im = j + i * 1j
        if im == start:
            print("S", end="")
        elif im in red:
            print("#", end="")
        elif im in green:
            print("X", end="")
        elif im in inside:
            print("o", end="")
        else:
            print(".", end="")
    print("")
