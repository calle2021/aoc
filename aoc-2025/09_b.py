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
            for i in range(x.real, y.real):
                green.add(i + x.imag)

        if (x.real == y.real):
            for i in range(x.imag, y.imag):
                green.add(x.real + i * 1j)
bounds = red | green
