from aocd import get_data
import regex as re
import numpy as np
puzzle = get_data(day=4, year=2024)
grid = []
for row in puzzle.split("\n"):
    grid.append([r for r in row])
grid = np.array(grid)
XMAS = 0
def check(subs):
    global XMAS
    for s in subs:
        XMAS += len(re.findall(r"XMAS", s))
        XMAS += len(re.findall(r"SAMX", s))

cols = [''.join(grid[:, col]) for col in range(grid.shape[1])]
rows = [''.join(grid[row, :]) for row in range(grid.shape[1])]
row, col = grid.shape
d1 = [''.join(grid.diagonal(x)) for x in range(-row, col)]
flipped = np.fliplr(grid)
d2 = [''.join(flipped.diagonal(x)) for x in range(-row, col)]

check(cols)
check(rows)
check(d1)
check(d2)
print(XMAS)