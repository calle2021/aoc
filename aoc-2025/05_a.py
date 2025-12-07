from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=5).input_data
ranges, numbers = puzzle.split("\n\n")
ranges = ranges.split("\n")
ranges = [eval(x.replace("-", ",")) for x in ranges]
numbers = list(map(int, numbers.split("\n")))
fresh = 0
for number in numbers:
    for window in ranges:
        if number >= window[0] and number <= window[1]:
            fresh += 1
            break
print(fresh)
