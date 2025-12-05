from aocd.models import Puzzle
puzzle = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
puzzle = Puzzle(year=2025, day=5).input_data
ranges = set()
numbers = set()
for range in puzzle.splitlines():
    if not len(range): continue
    if "-" in range:
        lo, hi = range.split("-")
        ranges.add((int(lo), int(hi)))
    else:
        numbers.add(int(range))

#print(ranges)
#print(numbers)
fresh = 0
def inside(number, range):
    if number >= range[0] and number <= range[1]:
        #print(number, range)
        return True
    return False
for number in numbers:
    isfresh = False
    for range in ranges:
        if inside(number, range):
            isfresh = True
            #print(number)
            break
    fresh += 1 if isfresh else 0
print(fresh)