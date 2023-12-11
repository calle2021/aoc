import numpy as np

input = "input.txt"
data = [d.strip() for d in open(input).readlines()]

space = 1000000 - 1
grid = []
galaxies = []
for y, row in enumerate(data):
    r = []
    for x, p in enumerate(row):
        r.append(p)
        if p == "#":
            galaxies.append((x, y))
    grid.append(r)

grid = np.array(grid)
rows = sorted(np.where(np.all(grid == ".", axis = 1))[0], reverse=True)
cols = sorted(np.where(np.all(grid == ".", axis = 0))[0], reverse=True)

for r in rows:
    galaxies = [(g[0], g[1] + space) if g[1] > r else g for g in galaxies]

for c in cols:
    galaxies = [(g[0] + space, g[1]) if g[0] > c else g for g in galaxies]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

s = 0
for g1 in galaxies:
    for g2 in galaxies:
        s += manhattan(g1, g2)
print(s // 2)