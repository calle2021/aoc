from aocd import get_data
import regex as re
import numpy as np
puzzle = get_data(day=4, year=2024)
grid = []
for row in puzzle.split("\n"):
    r = []
    for x in row:
        r.append(x)
    grid.append(r)
grid = np.array(grid)

XMAS = 0
for col in range(grid.shape[1]):
    s = ''.join(grid[:, col])
    XMAS += len(re.findall(r"XMAS", s))
    XMAS += len(re.findall(r"SAMX", s))
for row in range(grid.shape[0]):
    s = ''.join(grid[row, :])
    XMAS += len(re.findall(r"XMAS", s))
    XMAS += len(re.findall(r"SAMX", s))
row, col = grid.shape
diag = [grid.diagonal(x) for x in range(-row, col)]
for d in diag:
    s = ''.join(d)
    XMAS += len(re.findall(r"XMAS", s))
    XMAS += len(re.findall(r"SAMX", s))
flipped = np.fliplr(grid)
diag = [flipped.diagonal(x) for x in range(-row, col)]
for d in diag:
    s = ''.join(d)
    XMAS += len(re.findall(r"XMAS", s))
    XMAS += len(re.findall(r"SAMX", s))
print(XMAS)