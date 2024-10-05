import re
import numpy as np
from collections import deque

infile = "input.txt"

def transform(tile):
    tiles = []
    for _ in range(2):
        for _ in range(4):
            tiles.append(tile)
            tile = np.rot90(tile)
        tile = np.flip(tile, 0)
    return tiles

data = []
with open(infile) as f:
    tiles = f.read().split("\n\n")
    GRID_SIZE = int(len(tiles)**0.5)
    for t in tiles:
        tiles = t.splitlines()
        tile_id = tiles.pop(0)
        tile_id = re.findall(r'\d+', tile_id)[0]
        tile = []
        [tile.append(list(str(x))) for x in tiles ]
        
        tile = np.array(tile)
        ts_ = transform(tile)
        for t in ts_:
            data.append([eval(tile_id), t])
w = len(data[0][1][0, :])
h = len(data[0][1][:, 0])

g = {}
visited = set()
def align(r, c, visited) :
    if r == GRID_SIZE:
        return True
    for tiles in data:
        if tiles[0] in visited:
            continue
        if r > 0 and not np.array_equal(tiles[1][0, :], g[(r - 1, c)][1][h-1, :]):
                continue
        if c > 0 and not np.array_equal(tiles[1][:, 0], g[(r, c - 1)][1][:, w-1]):
                continue

        g[(r , c)] = tiles
        visited.add(tiles[0])
        if( c == GRID_SIZE -1):
            res = align(r + 1, 0, visited)
        else:
            res = align(r, c + 1, visited)
        visited.remove(tiles[0])
        if res:
            return True
align(0, 0, visited)
gz = GRID_SIZE - 1
#part 1
print(g[(0, 0)][0] * g[(gz, 0)][0] * g[(0, gz)][0] * g[(gz , gz)][0])
for r, c in g:
    g[(r, c)][1] = g[(r, c)][1][1:-1, 1:-1]

n = g[(0, 0)][1]

for c in range(1, GRID_SIZE):
    n = np.concatenate((n, g[(0, c)][1]), axis=1)
for r in range(1, GRID_SIZE):
    n_ = g[(r, 0)][1]
    for c in range(1, GRID_SIZE):
        n_ = np.concatenate((n_, g[(r, c)][1]), axis=1)
    n = np.concatenate((n, n_), axis=0)
s = []
n_ = transform(n)
for n in n_:
    s_ = []
    for r in range(len(n[:, 0])):
        s_.append(''.join(str(x) for x in n[r, :]))
    s.append(s_)

m1 = re.compile('(?=                  # )'.replace(' ', '.'))
m2 = re.compile('#    ##    ##    ###'.replace(' ', '.'))
m3 = re.compile(' #  #  #  #  #  #   '.replace(' ', '.'))

tags = sum( c == "#" for line in s[0] for c in line)
count = 0
for s_ in s:
    for i, line in enumerate(s_[:-2]):
        for m in m1.finditer(line):
            if m2.match(s_[i+1], m.start()) and m3.match(s_[i+2], m.start()):
                count += 1
#part 2
print(tags - count * 15)