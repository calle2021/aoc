import numpy as np

input = "input.txt"

grid = np.array([[x for x in y] for y in open(input).read().split("\n")])
dim = len(grid)

for i, col in enumerate(grid.T):
    squares = np.asarray(np.where(col == "#")).flatten().tolist()
    squares.insert(0, -1)
    squares.append(dim)
    for s1, s2 in zip(squares[:], squares[1:]):
        counts = np.count_nonzero(col[s1+1:s2] == "O")
        col[s1+1:s2] = "."
        col[s1+1:s1+1 + counts] = "O"
res = 0
for y, row in enumerate(grid):
    count = np.count_nonzero(row == "O")
    res += count * (dim - y)
print(res)