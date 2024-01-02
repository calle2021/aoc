import numpy as np
input = "input.txt"

patterns = open(input).read().split("\n\n")

def reflect(grid, mx, my):
    for row in range(0, my):
        dy = min(my - row - 1, row + 1)
        top = grid[row - dy + 1: row + 1, :]
        bottom = np.flip(grid[row + 1: row + dy + 1, :], axis=0)
        if top.size == 0 or bottom.size == 0: continue
        if np.array_equal(top, bottom):
            return (row + 1) * 100
    
    for col in range(0, mx):
        dx = min(mx - col - 1, col + 1)
        left = grid[:, col - dx + 1: col + 1]
        right = np.flip(grid[:, col + 1 : col + dx + 1], axis=1)
        if left.size == 0 or left.size == 0: continue
        if np.array_equal(left, right):
            return col + 1
        
res = 0
for p in patterns:
    grid = np.array([[ord(x) for x in y] for y in p.split("\n")])
    mx = len(grid[0, :])  
    my = len(grid[:, 0])
    res += reflect(grid, mx, my)
#part 1
print(res)