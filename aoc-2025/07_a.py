from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=7).input_data
diagram = []
for line in puzzle.splitlines():
    diagram.append([x for x in line])
start = (diagram[0].index("S"), 0)
splits = set()
def split(curr):
    x, y = curr
    if y == len(diagram) - 1:
        return
    symbol = diagram[y][x]
    if symbol == "^":
        if (x, y) in splits:
            return
        splits.add((x, y))
        split((x + 1, y + 1))
        split((x - 1, y + 1))
    else:
        split((x, y + 1))
split(start)
print(len(splits))
