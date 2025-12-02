from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=1).input_data
curr = 50
password = 0
for line in puzzle.splitlines():
    rot = line[0]
    clicks = int(line[1:])
    for click in range(clicks):
        if rot == "L":
            if curr == 0:
                curr = 99
            else:
                curr -= 1
        if rot == "R":
            if curr == 99:
                curr = 0
            else:
                curr += 1
    if curr == 0:
        password += 1
print(password)
