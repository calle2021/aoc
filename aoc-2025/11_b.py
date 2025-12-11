from aocd.models import Puzzle
import re
from collections import defaultdict
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

q = ["svr"]
came_from = defaultdict(list)
came_from["svr"].append(None)
while q:
    curr = q.pop(0)
    if curr == "out":
        print("out")
        continue
    neighbors = paths[curr]
    for next in neighbors:
        if next in came_from:
            continue
        came_from[next].append(next)
        q.append(next)
print(came_from["out"])
print("Done")
