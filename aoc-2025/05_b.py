from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=5).input_data
ranges, _ = puzzle.split("\n\n")
ranges = ranges.split("\n")
ranges = [eval(x.replace("-", ",")) for x in ranges]
ranges = sorted(ranges)
i = 0
while i < len(ranges) - 1:
    curr = ranges[i]
    next = ranges[i + 1]
    if next[0] <= curr[1]:
        ranges[i] = (curr[0], max(curr[1], next[1]))
        ranges.pop(i + 1)
        continue
    i += 1
fresh = sum([(x[1] - x[0]) + 1 for x in ranges])
print(fresh)