import numpy as np
from math import ceil
input = "input.txt"

rows = open(input).read().split("\n")

gardens = set()
rocks = set()
start = 0
mx = len(rows[0])
my = len(rows)
for y, row in enumerate(rows):
    for x, c in enumerate(row):
        g =  x + y * 1j
        if c == "S":
            start = g
            gardens.add(g)
        elif c == "#":
            rocks.add(g)
        elif c == ".":
            gardens.add(g)

dirs = [1, -1, 1j, -1j]

def count(start, steps):
    reached = {start}
    for _ in range(steps):
        new = set()
        while reached:
            r = reached.pop()
            garden = set()
            for d in dirs:
                s = r + d
                s = s.real % mx + s.imag % mx * 1j
                if s in rocks:
                    continue
                garden.add(r + d)
            new |= garden
        reached = new
    return len(reached)

steps = 26501365
xs = [0, 1, 2]
ys = []
for s in [1, 3, 5]:
    ys.append(count(start, s * mx // 2))
p = np.polyfit(xs, ys, 2)
x = steps // mx
print(ceil(p[0] * x ** 2 + p[1] * x + p[2]))