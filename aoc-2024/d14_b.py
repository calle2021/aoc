from aocd import get_data
import re
import numpy as np

puzzle = get_data(day=14, year=2024)

robots = []
for line in puzzle.split("\n"):
    x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
    robots.append(((x, y), (vx, vy)))

w = 101
h = 103

vars = []
for s in range(10000):
    xs = []
    ys = []
    for i, r in enumerate(robots):
        p, v = r
        x, y = p
        vx, vy = v
        x = (x + vx) % w
        y = (y + vy) % h
        robots[i] = ((x, y), v)
        xs.append(x)
        ys.append(y)
    vars.append(np.var(xs) + np.var(ys))
print(np.argmin(vars) + 1)