from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=3).input_data
joltage = 0
for line in puzzle.splitlines():
    numbers = [int(n) for n in line]
    number = 0
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers[i+1:]):
            candidate = int(str(x) + str(y))
            number = max(number, candidate)
    joltage += number
print(joltage)
