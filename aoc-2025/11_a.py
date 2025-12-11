from aocd.models import Puzzle
import re
puzzle = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""


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

    timelines = 0
    for next in neighbors:
        timelines += dfs(next)
    return timelines

res = dfs("you")
print(res)