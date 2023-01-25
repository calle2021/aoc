import re
import numpy as np
from collections import deque

infile = "ex.txt"

data = []
ids = []
with open(infile) as f:
    tiles = f.read().split("\n\n")
    for t in tiles:
        grid = t.splitlines()
        tile = grid.pop(0)
        tile = re.findall(r'\d+', tile)[0]
        s = []
        [s.append(list(str(x))) for x in grid ]
        ids.append(eval(tile))
        data.append(np.array(s))

w = len(data[0][:, 0])
h = len(data[0][0, :])

print(len(data))

#matching top with down, down with up, etc
lambdas = {"top" : (lambda x: x[h-1, :]), "down" : (lambda x: x[0, :]), "right" : (lambda x: x[:, 0]), "left" : (lambda x: x[:, w-1])}

def transform(side, tile, orr):
    for _ in range(2):
        for _ in range(4):
            t_ = lambdas[orr](tile)
            s_ = ''.join(str(e) for e in t_)
            if side == s_:
                return tile
            tile = np.rot90(tile)
        tile = np.flip(tile, 0)
    return []

data2 = []
map = {}
pos = (0,0)

curr = data.pop(0)
curr_id = ids.pop(0)
map[curr_id] = pos


q = deque([curr])
ids_ = deque([curr_id])

visited = set()
count = 0
while q:
    
    curr = q.popleft()
    curr_id = ids_.popleft()
    if curr_id in visited:
        continue
    visited.add(curr_id)

    pos = map[curr_id]
    data2.append(curr)

    top = ''.join(str(e) for e in curr[0, :])
    right = ''.join(str(e) for e in curr[:, w-1])
    down = ''.join(str(e) for e in curr[h-1, :])
    left = ''.join(str(e) for e in curr[:, 0])

    for i, d in enumerate(data):
        t = transform(top, d, "top")
        if len(t) != 0:
            data2.append(t)
            q.append(t)
            ids_.append(ids[i])
            map[ids[i]] = (pos[0], pos[1] - 1)

        t = transform(right, d, "right")
        if len(t) != 0:
            data2.append(t)
            q.append(t)
            ids_.append(ids[i])
            map[ids[i]] = (pos[0] + 1 , pos[1])

        t = transform(down, d, "down")
        if len(t) != 0:
            data2.append(t)
            q.append(t)
            ids_.append(ids[i])
            map[ids[i]] = (pos[0], pos[1] + 1)
        
        t = transform(left, d, "left")
        if len(t) != 0 :
            data2.append(t)
            q.append(t)
            ids_.append(ids[i])
            map[ids[i]] = (pos[0] - 1, pos[1])

print(len(data2))
print(map)

grid = [ [0]*3 for i in range(3)]
print(grid)
