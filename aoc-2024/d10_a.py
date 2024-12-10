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
count = 0
for s in start:
    q = [s]
    visited = set()
    visited.add(s)
    while q:
        curr = q.pop(0)
        neighbors = []
        for d in dirs:
            c = curr + d
            if c not in grid:
                continue
            if grid[c] - grid[curr] != 1:
                continue
            neighbors.append(c)

        for next in neighbors:
            if next not in visited:
                if grid[next] == 9:
                    count += 1
                q.append(next)
                visited.add(next)
print(count)