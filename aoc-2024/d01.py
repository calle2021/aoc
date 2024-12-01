from aocd.models import Puzzle
puzzle = Puzzle(year=2024, day=1).input_data
data = puzzle.split("\n")
a = []
b = []
for d in data:
    x, y = d.strip().split("   ")
    a.append(int(x))
    b.append(int(y))
a.sort()
b.sort()

diff = 0
for x, y in zip(a, b):
    diff += abs(x - y)
print(diff)

common = set(a) & set(b)
sim = 0
for c in common:
    sim += c * b.count(c)
print(sim)