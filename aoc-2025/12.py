from aocd.models import Puzzle
import numpy as np
puzzle = Puzzle(year=2025, day=12).input_data
puzzle = puzzle.split("\n\n")
allgrids = puzzle[-1]
allshapes = puzzle[:-1]
grids = []
quants = []
shapes = {}
for grid in allgrids.splitlines():
    x, y = grid.split(": ")
    y = [int(n) for n in y.split()]
    m, n = x.split("x")
    grids.append(int(n) * int(m))
    quants.append(np.array(y))
shapes = []
for shape in allshapes:
    arr = []
    rows = shape.splitlines()
    index = int(rows[0].split(":")[0])
    for row in rows[1:]:
        arr.append([1 if x == "#" else 0 for x in row])
    arr = np.array(arr)
    shapes.append(np.sum(arr))

shapes = np.array(shapes)
ans = 0
for quant, area in zip(quants, grids):
    if np.sum(quant * shapes) < area:
        ans += 1
print(ans)
