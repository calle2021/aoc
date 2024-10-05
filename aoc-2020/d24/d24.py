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

b_tiles = set()

for tile in data:
    ref = (0, 0)
    for d in tile:
        ref = (ref[0] + dirs[d][0], ref[1] + dirs[d][1])
    if ref in b_tiles:
        b_tiles.remove(ref)
    else:
        b_tiles.add(ref)

#part 1
print(len(b_tiles))

for _ in range(100):
    counter = {}
    for x, y in b_tiles:
        for dx, dy in dirs.values():
            v = (x + dx, y + dy)
            if v in counter: 
                counter[v] += 1
            else:
                counter[v] = 1
    
    to_remove = set()
    for t in b_tiles:
        if t in counter:
            if counter[t] == 0 or counter[t] > 2 :
                to_remove.add(t)
        else:
            to_remove.add(t)
    for c in counter:
        if counter[c] == 2 and c not in b_tiles:
            b_tiles.add(c)
            
    b_tiles -= to_remove
        
#part 2     
print(len(b_tiles))