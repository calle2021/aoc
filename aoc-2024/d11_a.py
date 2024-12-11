from aocd import get_data
from collections import defaultdict

puzzle = get_data(day=11, year=2024)

stones = {x : 1 for  x in list(map(int, puzzle.split())) }

for _ in range(25):
    new = defaultdict(int)
    for key, val in stones.items():
        l = len(str(key))
        if key == 0:
            new[1] += val
        elif l % 2 == 0:
            x = int(str(key)[:l//2])
            y = int(str(key)[l//2:])
            new[x] += val
            new[y] += val
        else:
            new[key * 2024] = val
    stones = new
print(sum([x for x in stones.values()]))