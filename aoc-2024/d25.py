from aocd import get_data

puzzle = get_data(day=25, year=2024)

locks = []
keys = []
for schematic in puzzle.split("\n\n"):
    rows = schematic.split("\n")
    islock = rows[0] == "#####"
    heights = []
    for x in range(5):
        col = [v[x] for v in rows[1:-1] if v[x] == "#"]
        heights.append(len(col))
    if islock:
        locks.append(heights)
    else:
        keys.append(heights)
fit = 0
for lock in locks:
    for key in keys:
        combined = [x + y for x, y in zip(lock, key)]
        if all(c <= 5 for c in combined):
            fit += 1
print(fit)



