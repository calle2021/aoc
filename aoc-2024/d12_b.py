from aocd import get_data
from collections import defaultdict
puzzle = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
puzzle = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
puzzle = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
#puzzle = get_data(day=12, year=2024)

grid = {}
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
        grid[curr] = col

def find(region, curr):
    garden = set()
    garden.add(curr)
    visited.add(curr)
    q = [curr]
    while q:
        curr = q.pop(0)
        neighbours = []
        for d in dirs:
            x = curr + d
            if x not in grid:
                continue
            if grid[x] != region:
                continue
            neighbours.append(x)
        for next in neighbours:
            if next not in garden:
                q.append(next)
                garden.add(next)
                visited.add(next)
    return garden
    


dirs = [1, -1, 1j, -1j]
gardens = []
regions = []
visited = set()
for y, row in enumerate(puzzle.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
        if curr in visited:
            continue
        g = find(col, curr)
        gardens.append(g)
        regions.append(col)

ans = 0
for r, g in zip(regions, gardens):
    perim = 0
    outside = set()
    for x in g:
        p = 0
        sides = []
        for d in dirs:
            if x + d in g:
                continue
            p += 1
            outside.add(x+d)
            sides.append(d)
        if p == 0 or p == 1:
            continue
        if p == 2:
            if sum(sides) == 0:
                continue
            print(r, "here")
            perim += 1
        if p == 3:
            perim += 2
        if p == 4:
            perim += 4
    for o in outside:
        p = 0
        sides = []
        for d in dirs:
            if o + d not in g:
                continue
            sides.append(d)
            p += 1
        if p == 2:
            if sum(sides) == 0:
                continue
            perim += 1
        if p == 3:
            perim += 2

            

    #print(outside)

    print(r, len(g), perim)
    ans += len(g) * perim
print(ans)
