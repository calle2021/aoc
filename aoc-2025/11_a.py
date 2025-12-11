from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=11).input_data
paths = {}
for line in puzzle.splitlines():
    x, y = line.split(": ")
    y = y.split(" ")
    paths[x] = y

def dfs(curr):
    if curr == "out":
        return 1
    neighbors = paths[curr]

    count = 0
    for next in neighbors:
        count += dfs(next)
    return count

res = dfs("you")
print(res)
