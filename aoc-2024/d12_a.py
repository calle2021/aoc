from aocd import get_data

puzzle = get_data(day=12, year=2024)

grid = {}
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
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
            x = curr + d
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

dirs = [1, -1, 1j, -1j]
gardens = []
regions = []
visited = set()
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
        if curr in visited:
            continue
        g = find(col, curr)
        gardens.append(g)

price = 0
for garden in gardens:
    perim = 0
    for g in garden:
        p = 0
        for d in dirs:
            if g + d in garden:
                continue
            p += 1
        perim += p
    price += len(garden) * perim
print(price)
