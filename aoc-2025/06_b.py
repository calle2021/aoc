from aocd.models import Puzzle
import re
import math
puzzle = Puzzle(year=2025, day=6).input_data
homework = []
symbols = []
for line in puzzle.splitlines():
    if "+" in line or "*" in line:
        symbols = re.findall(r"[*+]", line)
    else:
        homework.append(line)
length = max([len(x) for x in homework])
ans = 0
curr = 0
numbers = []
for i in range(length):
    number = ""
    for j in range(len(homework)):
        if len(homework[j]) <= i: continue
        number += homework[j][i]
    number = number.replace(" ", "")
    empty = number == ""
    if not empty:
        numbers.append(int(number))
    if empty or  i == length - 1:
        symbol = symbols[curr]
        ans += sum(numbers) if symbols[curr] == "+" else math.prod(numbers)
        numbers = []
        curr += 1
print(ans)