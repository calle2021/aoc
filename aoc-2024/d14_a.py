from aocd import get_data
import re

puzzle = get_data(day=14, year=2024)

robots = []
for line in puzzle.split("\n"):
    x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
    robots.append(((x, y), (vx, vy)))
w = 101
h = 103

for s in range(100):
    for i, r in enumerate(robots):
        p, v = r
        x, y = p
        vx, vy = v
        x = (x + vx) % w
        y = (y + vy) % h
        robots[i] = ((x, y), v)

quads = [0, 0, 0, 0]
for r in robots:
    p, v = r
    x, y = p
    if x < (w-1) // 2 and y < (h-1) // 2:
        quads[0] += 1
    if x > (w-1) // 2 and y < (h-1) // 2:
        quads[1] += 1
    if x < (w-1) // 2 and y > (h-1) // 2:
        quads[2] += 1
    if x > (w-1) // 2 and y > (h-1) // 2:
        quads[3] += 1
factor = 1
for q in quads:
    factor *= q
print(factor)