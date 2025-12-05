from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=5).input_data
ranges = set()
numbers = set()
for window in puzzle.splitlines():
    if not len(window): continue
    if "-" in window:
        lo, hi = window.split("-")
        ranges.add((int(lo), int(hi)))
    else:
        numbers.add(int(window))
fresh = 0
def inside(number, window):
    if number >= window[0] and number <= window[1]:
        return True
    return False
for number in numbers:
    isfresh = False
    for window in ranges:
        if inside(number, window):
            isfresh = True
            break
    fresh += 1 if isfresh else 0
print(fresh)
