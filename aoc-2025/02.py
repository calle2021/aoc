from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=2).input_data
puzzle = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
puzzle = Puzzle(year=2025, day=2).input_data
invalids = 0
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
            invalids+=number

print(invalids)