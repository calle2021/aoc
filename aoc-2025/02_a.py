from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=2).input_data
invalid = 0
for line in puzzle.strip().split(","):
    x, y = line.split("-")
    x = int(x)
    y = int(y)

    for number in range(x, y + 1):
        s = str(number)
        half = len(s) // 2
        left = s[:half]
        right = s[half:]
        if left == right:
            invalid += number
print(invalid)
