import re
from math import gcd

from aocd.models import Puzzle
year = 2019
day = 12


puzzle = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""

puzzle = Puzzle(year=year, day=day).input_data

moons = []
pattern = r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>"
for moon in puzzle.strip().splitlines():
    x, y, z = map(int, re.match(pattern, moon).groups())
    moons.append((x, y, z))
velocity = [(0, 0, 0) for m in moons]

def gravity(m, v):
    for i in range(len(m)):
        x1, y1, z1 = m[i]
        vx, vy, vz = v[i]
        LT = lambda x, y: 1 if x < y else 0
        MT = lambda x, y: -1 if x > y else 0 
        for moon in m:
            x2, y2, z2 = moon
            vx += LT(x1, x2) + MT(x1, x2)
            vy += LT(y1, y2) + MT(y1, y2)
            vz += LT(z1, z2) + MT(z1, z2)
        v[i] = (vx , vy, vz)
    return v

def motion(moons, velocity):
    return [(m[0] + v[0], m[1] + v[1], m[2] + v[2]) for m, v in zip(moons, velocity)]

def lcm(a, b):
    return abs(a) * abs(b) // gcd(a, b)

xi = hash((tuple([m[0] for m in moons]), (0, 0, 0, 0)))
yi = hash((tuple([m[1] for m in moons]), (0, 0, 0, 0)))
zi = hash((tuple([m[2] for m in moons]), (0, 0, 0, 0)))

steps = 0
x = 0
y = 0
z = 0
while True:
    velocity = gravity(moons, velocity)
    moons = motion(moons, velocity)
    steps += 1
    xc = hash((tuple([m[0] for m in moons]), tuple([v[0] for v in velocity])))
    yc = hash((tuple([m[1] for m in moons]), tuple([v[1] for v in velocity])))
    zc = hash((tuple([m[2] for m in moons]), tuple([v[2] for v in velocity])))

    if xc == xi and not x:
        x = steps
    if yc == yi and not y:
        y = steps
    if zc == zi and not z:
        z = steps
    if x and y and z:
        break
print(lcm(lcm(x, y), z))
