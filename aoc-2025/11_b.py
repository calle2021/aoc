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


puzzle = Puzzle(year=2025, day=11).input_data
paths = {}
for line in puzzle.splitlines():
    x, y = line.split(": ")
    y = y.split(" ")
    paths[x] = y

cache = {}
def dfs(curr):
    if curr in cache:
        return cache[curr]
    if curr == "out":
        return 0
    if curr == "dac" or curr == "fft":
        return 1
    neighbors = paths[curr]

    timelines = 0
    for next in neighbors:
        timelines += dfs(next)
    cache[curr] = timelines
    return timelines

res = dfs("svr")
print(res)