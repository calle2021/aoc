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

def check_above(tile, s):
    if ''.join(str(e) for e in tile[:, 0]) == s:
        return True
    return False


def check_left(tile, s):
    if ''.join(str(e) for e in tile[0, :]) == s:
        return True
    return False

g = {}
visited = set()
GRID_SIZE = 12
f = {}
first = True
res = []
def align(r, c, visited) :
    if r == GRID_SIZE:
        res.append(g.copy())
        print(res[0][(0, 0)][0] * res[0][(11, 0)][0] * res[0][(0, 11)][0] * res[0][(11, 11)][0] )
        exit()
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
            align(r + 1, 0, visited)
        else:
            align(r, c + 1, visited)
        visited.remove(tiles[0])
align(0, 0, visited)