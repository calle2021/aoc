from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=3).input_data
joltage = 0
for line in puzzle.splitlines():
    numbers = list(map(int, line))
    number = ""
    consumed = 0
    while consumed < 12:
        need = 12 - consumed
        window = len(numbers) - need
        i = numbers.index(max(numbers[:window + 1]))
        number += str(numbers[i])
        numbers = numbers[i + 1:]
        consumed += 1
    joltage += int(number)
print(joltage)
