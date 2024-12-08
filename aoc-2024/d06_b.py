from aocd import get_data

puzzle = get_data(day=6, year=2024)
grid = set()
obstacles = set()
facings = {"v" : 1j, "<" : -1, ">" : 1, "^" : -1j}
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
        grid.add(curr)
        if col == "#":
            obstacles.add(curr)
        if col in ["v", "<", ">", "^"]:
            guard = curr
            facing = facings[col]

stuck = 0
for i, o in enumerate(grid):
    if o in obstacles:
        continue
    obstacles.add(o)
    visited = set()
    g = guard
    f = facing
    visited.add((g, f))
    while g in grid:
        if g + f in obstacles:
            f = f * 1j
        g = g + f
        if (g, f) in visited:
            stuck += 1
            break
        visited.add((g, f))
    obstacles.remove(o)
print(stuck)