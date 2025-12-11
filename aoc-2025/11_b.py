from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=11).input_data
paths = {}
for line in puzzle.splitlines():
    x, y = line.split(": ")
    y = y.split(" ")
    paths[x] = y

cache = {}
def dfs(curr, fft, dac):
    if (curr, fft, dac) in cache:
        return cache[(curr, fft, dac)]
    if curr == "out":
        if fft and dac:
            return 1
        return 0
    neighbors = paths[curr]
    count = 0
    for next in neighbors:
        count += dfs(next, fft if fft else next == "fft", dac if dac else next == "dac")
    cache[(curr, fft, dac)] = count
    return count
res = dfs("svr", 0, 0)
print(res)
