from aocd import get_data

puzzle = get_data(day=10, year=2024)
grid = {}
start = []
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
        if col == "0":
            start.append(curr)
        grid[curr] = int(col)

dirs = [1, -1, 1j, -1j]
trails = set()
def walk(curr, path):
    if grid[curr] == 9:
        return tuple(path)
    for d in dirs:
        c = curr + d
        if c not in grid:
            continue
        if grid[c] - grid[curr] != 1:
            continue
        if c in path:
            continue
        trails.add(walk(c, path + [c]))
for s in start:
    walk(s, [s])
print(len(trails) - 1)