from aocd.models import Puzzle
year = 2019
day = 18
puzzle = Puzzle(year=year, day=day)
puzzle = puzzle.input_data
paths = set()
keys = {}
doors = {}

for r, row in enumerate(puzzle.splitlines()):
    for c, col in enumerate(row):
        cord = c + r * 1j
        if col == "#":
            continue
        if col == "@":
            start = cord
        elif c == ".":
            paths.add(cord)
        elif c == c.lower():
            keys[cord] = c
        elif c == c.upper():
            doors[cord] = c
print(doors)