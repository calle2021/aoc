import re
import numpy as np
from collections import deque

infile = "input.txt"

data = []
w = 0
h = 0
with open(infile) as f:
    tiles = f.read().split("\n\n")
    for t in tiles:
        grid = t.splitlines()
        tile = grid.pop(0)
        tile = re.findall(r'\d+', tile)[0]
        s = []
        [s.append(list(str(x))) for x in grid ]
        w = len(s[0])
        h = len(s)
        arr = np.array(s)
        data.append([eval(tile), arr])

def get_boarders(arr, w, h):
    top = ''.join(map(str, arr[0, :]))
    right = ''.join(str(e) for e in arr[:, w-1])
    down = ''.join(str(e) for e in arr[h-1, :])
    left = ''.join(str(e) for e in arr[:, 0])
    return [top, right, down, left]

edges = []
ids = []
for d in data:
    ids.append(d[0])
    edges.append(get_boarders(d[1], w, h))

def reverse(x):
  return x[::-1]

corner_ids = []
while edges:
    edge = edges.pop(0)
    id = ids.pop(0)
    count = 0
    for e in edge:
        for e_ in edges:
            if e in e_ or reverse(e) in e_:
                count += 1
    if count == 2:
        corner_ids.append(id)
    if len(corner_ids) == 4:
        break
    edges.append(edge)
    ids.append(id)

prod = 1
for c in corner_ids:
    prod *= c
print(prod)