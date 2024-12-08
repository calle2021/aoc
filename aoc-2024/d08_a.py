from aocd import get_data

puzzle = get_data(day=8, year=2024)

grid = {}
antennas = {}
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
        grid[curr] = col
        if col == ".":
            continue
        if col in antennas:
            antennas[col].append(curr)
        else:
            antennas[col] = [curr]
            
antinodes = set()
for antenna in antennas:
    for a in antennas[antenna]:
        for b in antennas[antenna]:
            if b == a:
                continue
            p = a + a - b
            if p not in grid:
                continue
            antinodes.add(p)
print(len(antinodes))
