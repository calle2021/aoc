file = "input.txt"

lines = [l.strip() for l in open(file).readlines()]

data = {}
for y, l in enumerate(lines):
    for x, d in enumerate(l):
        cor = (x, y)
        data[(x, y)] = int(d)

xy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

lp_sum = 0
lp_cords = []
for x, y in data.keys():
    val = data[(x, y)]
    is_lp = True
    for xy_ in xy:
        p = (x + xy_[0], y + xy_[1])
        if p in data:
            if data[p] <= val:
                is_lp = False
    if is_lp:
        lp_cords.append((x, y))
        lp_sum = lp_sum + 1 + val

# part 1
print(lp_sum)


def get_basin(p):
    q = [p]
    visited = set()
    while q:
        q_ = q.pop(0)
        visited.add(q_)

        for xy_ in xy:
            p_ = (q_[0] + xy_[0], q_[1] + xy_[1])
            if p_ in data:
                if data[p_] == 9 or p_ in visited:
                    continue
                q.append(p_)
    return visited


basins = []
for lp in lp_cords:
    basins.append(len(get_basin(lp)))

basins.sort()
# part 2
print(basins[-1] * basins[-2] * basins[-3])
