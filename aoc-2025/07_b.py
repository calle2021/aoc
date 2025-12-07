from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=7).input_data
diagram = []
for line in puzzle.splitlines():
    diagram.append([x for x in line])
start = (diagram[0].index("S"), 0)
cache = {}
def timelines(curr):
    if curr in cache:
        return cache[curr]
    x, y = curr
    if y == len(diagram) - 1:
        return 1
    neighbors = []
    if diagram[y][x] == "^":
        neighbors = [(x + 1, y + 1), (x - 1, y + 1)]
    else:
        neighbors = [(x, y + 1)]
    splits = 0
    for next in neighbors:
        splits += timelines(next)
    cache[curr] = splits
    return splits
splits = timelines(start)
print(splits)