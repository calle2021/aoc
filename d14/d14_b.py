import numpy as np

input = "input.txt"

grid = np.array([[x for x in y] for y in open(input).read().split("\n")])
dim = len(grid)

def tilt(grid):
    for col in grid.T:
        squares = np.asarray(np.where(col == "#")).flatten().tolist()
        squares.insert(0, -1)
        squares.append(dim)
        for s1, s2 in zip(squares[:], squares[1:]):
            counts = np.count_nonzero(col[s1+1:s2] == "O")
            col[s1+1:s2] = "."
            col[s1+1:s1+1 + counts] = "O"
cycle = 0
seen = [hash(tuple(grid.flatten()))]
goal = 1000000000
while cycle < goal:
    cycle += 1
    for _ in range(4):
        tilt(grid)
        grid = np.rot90(grid, k=-1)

    key = hash(tuple(grid.flatten()))
    if key in seen:
        l = cycle - seen.index(key)
        steps = (goal - cycle) // l
        cycle += steps * l
    seen.append(key)

res = 0
for y, row in enumerate(grid):
    count = np.count_nonzero(row == "O")
    res += count * (dim - y)
print(res)

