from aocd.models import Puzzle
puzzle = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
puzzle = Puzzle(year=2025, day=9).input_data

tiles = []
for y, line in enumerate(puzzle.splitlines()):
    tiles.append(eval(line))
areas = []
pairs = []
for i in range(len(tiles)):
    for j in range(len(tiles)):
        if i == j: continue
        x = tiles[i]
        y = tiles[j]
        left = abs(x[0] - y[0]) + 1
        right = abs(x[1] - y[1]) + 1
        areas.append(left * right)
        pairs.append((x, y))
i = areas.index()
print(max(areas))