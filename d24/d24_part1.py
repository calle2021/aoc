infile = "input.txt"

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

black  = 0
for k in tiles.values():
    if k == 1:
        black += 1 
print(black)