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
#puzzle = Puzzle(year=2025, day=5).input_data
ranges = []
for r in puzzle.splitlines():
    if not len(r): continue
    if "-" in r:
        lo, hi = r.split("-")
        ranges.append((int(lo), int(hi)))
print(ranges)

merged = [ranges.pop(0)]
print(merged)
def merge(r):
    update = False
    i = 0
    new = None
    for m in merged:
        lo = m[0]
        hi = m[1]
        if r[0] >= m[0] and r[0] <= m[1]:
            hi = max(m[1], r[1])
            update = True
        if r[1] >= m[0] and r[1] <= m[1]:
            lo = min(r[0], m[0])
            update = True
        if update:
            new = (lo, hi)
            break
        i += 1
    if update:
        merged[i] = new
    else:
        merged.append(r)

for r in ranges:
    merge(r)
print(merged)
fresh = 0
for m in merged:
    s = m[1] - m[0] + 1
    fresh += s
print(fresh)
