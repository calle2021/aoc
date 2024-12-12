from aocd import get_data
puzzle = get_data(day=12, year=2024)

grid = {}
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = (x, y)
        grid[curr] = col

def find(region, curr):
    garden = set()
    garden.add(curr)
    visited.add(curr)
    q = [curr]
    while q:
        curr = q.pop(0)
        neighbours = []
        for d in dirs:
            x = (curr[0] + d[0], curr[1] + d[1])
            if x not in grid:
                continue
            if grid[x] != region:
                continue
            neighbours.append(x)
        for next in neighbours:
            if next not in garden:
                q.append(next)
                garden.add(next)
                visited.add(next)
    return garden
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
gardens = []
visited = set()
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = (x, y)
        if curr in visited:
            continue
        g = find(col, curr)
        gardens.append(g)

offsets = [(0.5, 0.5), (-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5)]
price = 0
for garden in gardens:
    corners = set()
    for g in garden:
        corners |= {(g[0] + o[0], g[1] + o[1]) for o in offsets}
    count = 0
    for c in corners:
        quads = [(c[0] + o[0], c[1] + o[1]) for o in offsets]
        a = [q for q in quads if q in garden]
        l = len(a)
        if l == 4:
            continue
        if l == 3 or l == 1:
            count += 1
        if l == 2:
            if a[0][0] == a[1][0] or a[0][1] == a[1][1]:
                continue
            count += 2
    price += len(garden) * count
print(price)
