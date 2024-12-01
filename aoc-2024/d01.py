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

diff = sum([abs(x - y) for x, y in zip(a, b)])
print(diff)

common = set(a) & set(b)
sim = sum([c * b.count(c) for c in common])
print(sim)