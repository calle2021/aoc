from aocd.models import Puzzle
import re
puzzle = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


#puzzle = Puzzle(year=2025, day=11).input_data
paths = {}
for line in puzzle.splitlines():
    x, y = line.split(": ")
    y = y.split(" ")
    paths[x] = y

cache = {}
def dfs(curr, path):
    tpath = tuple(path)
    if (curr, tpath) in cache:
        return cache[(curr, tpath)]
    if curr == "out":
        if "dac" in path and "fft" in path:
            return 1
        return 0
    neighbors = paths[curr]

    timelines = 0
    for next in neighbors:
        timelines += dfs(next, path | {next})
    cache[(curr, tpath)] = timelines
    return timelines

res = dfs("svr", {"svr"})
print(res)