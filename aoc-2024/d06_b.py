from aocd import get_data

puzzle = get_data(day=6, year=2024)
grid = set()
obstacles = set()
visited = set()
dirs = [1, -1, 1j, -1j]
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

x = 10000
stuck = 0
for i, o in enumerate(grid):
    if o in obstacles:
        continue
    obstacles.add(o)
    g = guard
    f = facing
    count = 0
    while g in grid:
        if g + f in obstacles:
            f = f * 1j
        g = g + f
        count += 1
        if count > x:
            stuck += 1
            break
    obstacles.remove(o)
print(stuck)