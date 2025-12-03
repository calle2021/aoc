from aocd.models import Puzzle
puzzle = """987654321111111
811111111111119
234234234234278
818181911112111"""
#puzzle = Puzzle(year=2025, day=3).input_data
joltage = 0
def jolt(curr="", i=0):
    if len(curr) == 12 or i == len(numbers):
        if curr == "": return 0
        return int(curr)
    x = jolt(curr + numbers[i], i + 1)
    y = jolt(curr, i + 1)
    if y == "": return int(x)
    return max(int(x), int(y))

for line in puzzle.splitlines():
    numbers = tuple([n for n in line])
    jolts = jolt()
    joltage += jolts
print(joltage)