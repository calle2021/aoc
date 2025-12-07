from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=7).input_data
diagram = []
for line in puzzle.splitlines():
    diagram.append([x for x in line])
start = (diagram[0].index("S"), 0)
cache = {}
splits = set()
def dfs(curr):
    if curr in cache:
        return cache[curr]
    x, y = curr
    if y == len(diagram) - 1:
        return 1
    neighbors = []
    if diagram[y][x] == "^":
        splits.add(curr)
        neighbors = [(x + 1, y + 1), (x - 1, y + 1)]
    else:
        neighbors = [(x, y + 1)]
    timelines = 0
    for next in neighbors:
        timelines += dfs(next)
    cache[curr] = timelines
    return timelines
timelines = dfs(start)
splits = len(splits)
print(splits)
print(timelines)