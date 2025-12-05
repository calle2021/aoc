from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=5).input_data

ranges = []
for r in puzzle.splitlines():
    if not len(r): continue
    if "-" in r:
        lo, hi = r.split("-")
        ranges.append((int(lo), int(hi)))

def merge(window, data):
    i = 0
    if window in data:
        i = data.index(window)
        data.pop(i)
    for j, w in enumerate(data):
        lo = w[0]
        hi = w[1]
        update = False
        if window[0] >= w[0] and window[0] <= w[1]:
            hi = max(w[1], window[1])
            update = True
        if window[1] >= w[0] and window[1] <= w[1]:
            lo = min(window[0], w[0])
            update = True
        if update:
            data[j] = (lo, hi)
            return data[j]
    data.insert(i, window)
    return window

merged = []
for window in ranges:
    while True:
        res = merge(window, merged)
        if res == window:
            break
        window = res

for window in merged:
    while True:
        res = merge(window, merged)
        if res == window:
            break
        window = res

fresh = 0
for win in merged:
    fresh += win[1] - win[0] + 1
print(fresh)
