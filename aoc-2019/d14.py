from aocd.models import Puzzle
from math import ceil
year = 2019
day = 14
puzzle = Puzzle(year=year, day=day).examples[2].input_data
puzzle = Puzzle(year=year, day=day).input_data
reactions = {}
for r in puzzle.strip().splitlines():
    m, c = r.split("=>")
    c = c.split(" ")[-2:]
    m = m.split(",")
    m = [x.strip() for x in m]
    m = [x.split() for x in m]
    m = [(x[1], int(x[0])) for x in m]
    reactions[c[1]] = [int(c[0]), m]

excess = {}
def rec(curr, n):
    if curr == "ORE":
        return n

    if curr in excess:
        if excess[curr] >= n:
            excess[curr] -= n
            return 0
        else:
            n -= excess[curr]
            excess[curr] = 0
    batches = ceil(n / reactions[curr][0])
    excess_produced = batches * reactions[curr][0] - n

    if excess_produced > 0:
        if curr in excess:
            excess[curr] += excess_produced
        else:
            excess[curr] = excess_produced

    need = 0
    for next, amount in  reactions[curr][1]:
        tot = amount * batches
        need += rec(next, tot)
    return need
ores = rec("FUEL", 1)
print(ores)

low = 0
high = 1E12
cargo = 1E12

while low <= high:
    mid = (low + high) // 2
    excess = {}
    ores = rec("FUEL", mid)
    if ores <= cargo:
        low = mid + 1
    else:
        high = mid - 1
print(int(high))
