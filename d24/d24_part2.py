infile = "ex.txt"

dirs = { "e" : (1, 0), "se": (0.5, -1), "sw" : (-0.5, -1), "w" : (-1, 0), "nw" : (-0.5, 1), "ne" : (0.5, 1)}
data = []
for line in open(infile):
    line = line.strip()
    line = [i for i in line]
    lst = []
    while line:
        d = line.pop(0)
        if d in dirs.keys():
            lst.append(d)
        else:
            d += line.pop(0)
            lst.append(d)
    data.append(lst)

tiles = {(0, 0) : 0}

for tile in data:
    ref = (0, 0)
    for d in tile:
        ref = (ref[0] + dirs[d][0], ref[1] + dirs[d][1])
    if ref in tiles:
        if tiles[ref] == 1:
            tiles[ref] = 0
        else:
            tiles[ref] = 1
    else:
        tiles[ref] = 1

def adj(t, tiles):
    b = 0
    w = 0

    for d in dirs.values():
        a = (t[0] + d[0], t[1] + d[1])
        if a in tiles:
            if tiles[a] == 1:
                b += 1
            else:
                w += 1
        return b, w

for _ in range(2):
    tiles_ = {}
    for t in tiles:
        b, w = adj(t, tiles)
        print(b, w)
        if tiles[t] == 1:
            if b == 0 or b > 2:
                tiles_[t] = 0
            else:
                tiles_[t] = 1
        else:
            if b == 2:
                tiles_[t] = 1
            else:
                tiles_[t] = 0
    tiles = tiles_.copy()

print(tiles)
black  = 0
for k in tiles.values():
    if k == 1:
        black += 1 
print(black)