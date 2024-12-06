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
            
while guard in grid:
    visited.add(guard)
    if guard + facing in obstacles:
        facing = facing * 1j
    guard = guard + facing

print(len(visited))