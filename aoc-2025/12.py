from aocd.models import Puzzle
import numpy as np
puzzle = Puzzle(year=2025, day=12).input_data
puzzle = puzzle.split("\n\n")
allgrids = puzzle[-1]
allshapes = puzzle[:-1]
grids = []
quant = []
shapes = {}
for grid in allgrids.splitlines():
    x, y = grid.split(": ")
    y = [int(n) for n in y.split()]
    m, n = x.split("x")
    m = int(m)
    n = int(n)
    g = np.zeros((m, n))
    grids.append(g)
    quant.append(np.array(y))
shapes = []
for shape in allshapes:
    arr = []
    rows = shape.splitlines()
    index = int(rows[0].split(":")[0])
    for row in rows[1:]:
        arr.append([1 if x == "#" else 0 for x in row])
    arr = np.array(arr)
    shapes.append(np.sum(arr))
ans = 0
for q, g in zip(quant, grids):
    dims = g.shape
    area = dims[0] * dims[1]
    if sum(q * shapes) < area:
        ans += 1
print(ans)
