from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=1).input_data
curr = 50
ans = 0
ans2 = 0
for line in puzzle.splitlines():
    d = line[0]
    clicks = int(line[1:])
    for click in range(clicks):
        if curr == 0 and click > 0:
            ans2 += 1
        if d == "L":
            if curr == 0:
                curr = 99
            else:
                curr -= 1
        if d == "R":
            if curr == 99:
                curr = 0
            else:
                curr += 1
    if curr == 0:
        ans += 1
        ans2 += 1

print(ans, ans2)
