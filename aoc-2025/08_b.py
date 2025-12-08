from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=8).input_data
junktions = [eval(x) for x in puzzle.splitlines()]
connections = []
pairs = []
unique = set()
def euc(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2
for i, x in enumerate(junktions):
    for j, y in enumerate(junktions):
        if j == i: continue
        add = tuple(sorted((x, y)))
        dist = euc(x, y)
        pairs.append((dist, add))
        unique.add(x)
        unique.add(y)

pairs = sorted(pairs)
pairs = pairs[::2]
last = (0, 0)
while pairs:
    a, b = pairs.pop(0)
    x, y = b
    if x in unique:
        unique.remove(x)
    if y in unique:
        unique.remove(y)
    last = (x, y)
    if not unique:
        break
    ids = []
    for i, c in enumerate(connections):
        if x in c or y in c:
            ids.append(i)
    if not ids:
        connections.append({x ,y})
        continue
    i = ids[0]
    if len(ids) == 1:
        connections[i].add(x)
        connections[i].add(y)
        continue
    connections[i].add(x)
    connections[i].add(y)
    updated = []
    circ = set()
    for j in ids:
        circ |= connections[j]
    for j in range(len(connections)):
        if j in ids:
            continue
        updated.append(connections[j])
    updated.append(circ)
    connections = updated
print(last[0][0] * last[1][0])
