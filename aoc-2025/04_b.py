from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=4).input_data
rolls = set()
dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
for y, line in enumerate(puzzle.splitlines()):
    for x, c in enumerate(line):
        if c == "@":
            rolls.add((x, y))

def removable(roll):
    adj = 0
    for d in dirs:
        r = (roll[0] + d[0], roll[1] + d[1])
        if r in rolls:
            adj += 1
    return adj < 4

def remove(rolls):
    can_remove = []
    for roll in rolls:
        if removable(roll):
            can_remove.append(roll)
    for r in can_remove:
        rolls.remove(r)
    return len(can_remove)

removed = 0
while(True):
    rem = remove(rolls)
    if not rem: break
    removed += rem
print(removed)
