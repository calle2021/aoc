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
        numbers = re.findall(r"\d+", line)
        homework.append(list(map(int, numbers)))
ans = 0
for i in range(len(symbols)):
    numbers = [homework[j][i] for j in range(len(homework))]
    ans += sum(numbers) if symbols[i] == "+" else math.prod(numbers)
print(ans)