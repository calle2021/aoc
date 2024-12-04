from aocd import get_data
import regex as re

puzzle = get_data(day=4, year=2024)
rows = [row for row in puzzle.split("\n")]
XMAS = 0
def check(pattern, x, y):
    global XMAS
    for m in re.finditer(pattern, row, overlapped=True):
        r1 = rows[i+1][m.start(): m.end()]
        r2 = rows[i+2][m.start(): m.end()]
        if r1[1] == "A" and r2[0] == x and r2[2] == y:
            XMAS += 1

for i in range(len(rows) - 2):
    row = rows[i]
    check(r"M.S", "M", "S")
    check(r"S.M", "S", "M")
    check(r"S.S", "M", "M")
    check(r"M.M", "S", "S")

print(XMAS)