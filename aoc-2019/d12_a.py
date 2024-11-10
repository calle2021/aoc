import re

from aocd.models import Puzzle
year = 2019
day = 12

puzzle = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
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

def energy(moons, velocity):
    return sum([(abs(m[0]) + abs(m[1]) + abs(m[2])) * (abs(v[0]) + abs(v[1]) + abs(v[2])) for m, v in zip(moons, velocity)])

steps = 1000
for _ in range(steps):
    velocity = gravity(moons, velocity)
    moons = motion(moons, velocity)
e = energy(moons,velocity)
print(e)
