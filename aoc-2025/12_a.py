from aocd.models import Puzzle
import numpy as np
puzzle = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
#puzzle = Puzzle(year=2025, day=11).input_data
puzzle = puzzle.split("\n\n")
allgrids = puzzle[-1]
allshapes = puzzle[:-1]
grids = []
quant = []
shapes = []
print(allgrids)
for grid in allgrids.splitlines():
    print(grid)
    x, y = grid.split(": ")
    y = [int(n) for n in y.split()]
    m, n = x.split("x")
    m = int(m)
    n = int(n)
    g = np.zeros((m, n))
    grids.append(g)
    quant.append(y)
for shape in allshapes:
    print(shape)