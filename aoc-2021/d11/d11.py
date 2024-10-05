file = "ex.txt"

lines = [l.strip() for l in open(file).readlines()]

data = {}

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        data[(x, y)] = int(c)

a = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

flashes = 0
for i in range(1000):
    q = []
    for o in data.keys():
        data[o] += 1
        if data[o] > 9:
            q.append(o)
    visited = set()
    while q:
        q_ = q.pop()
        visited.add(q_)
        for x, y in a:
            p = (q_[0] + x, q_[1] + y)
            if p in data and p not in q and p not in visited:
                data[p] += 1
                if data[p] > 9:
                    q.append(p)
    flashes += len(visited)
    if i == 99:
        # part 1
        print(flashes)
    if len(visited) == len(data):
        # part 2
        print(i + 1)
        break
    for o in visited:
        data[o] = 0
