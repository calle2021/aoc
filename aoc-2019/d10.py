import math
from aocd.models import Puzzle
year = 2019
day = 10

puzzle = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""
puzzle = Puzzle(year=year, day=day).input_data
space = set()
asteroids = set()
for y, row in enumerate(puzzle.strip().splitlines()):
    for x, col in enumerate(row):
        space.add((x, y))
        if col == "#":
            asteroids.add((x, y))

def visible(curr, target):
    if curr == target: return 0
    x1, y1, = curr
    x2, y2 = target
    dx = (x2 - x1)
    dy = (y2 - y1)
    points = set()
    if dx == 0:
        points = {(x1, i) for i in range(min(y1, y2) + 1, max(y1, y2))}
    elif dy == 0:
        points = {(i, y1) for i in range(min(x1, x2) + 1, max(x1, x2))}
    else:
        g = math.gcd(dx, dy)
        dx = dx // g
        dy = dy // g
        x, y = x1 + dx, y1 + dy
        while (x, y) != (x2, y2):
            points.add((x, y))
            x += dx
            y += dy
    collision = len(set(asteroids) & points)
    if not collision:
        return 1
    return 0

los = []
for curr in asteroids:
    los.append((sum([visible(curr, target) for target in asteroids]), curr))
station = max(los, key=lambda x: x[0])
print(station[0])

station = station[1]
asteroids.remove(station)
asteroids = list(asteroids)

def angle(a):
    x1, y1 = station
    x2, y2 = a
    dx = (x2 - x1)
    dy = (y1 - y2)
    angle = math.degrees(math.atan2(dx, dy))
    if angle < 0:
        angle += 360
    return angle

asteroids.sort(key=angle)
angles = [angle(x) for x in asteroids]
vaporized = []
while asteroids:
    i = 0
    vaporize = []
    for target in asteroids:
        if visible(station, target):
            vaporize.append(target)
    for x in vaporize:
        asteroids.remove(x)
        vaporized.append(x)
print(vaporized[199][0] * 100 + vaporized[199][1])
