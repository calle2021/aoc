from aocd import get_data
import re

puzzle = get_data(day=13, year=2024)
machines = []
for line in puzzle.split("\n\n"):
    row = line.split("\n")
    a = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", row[0])[0]
    b = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", row[1])[0]
    p = re.findall(r"Prize: X=(\d+), Y=(\d+)", row[2])[0]
    machines.append([tuple(map(int, a)), tuple(map(int, b)), tuple(map(int, p))])

def play(a, b, pa, pb, p, cost, cache):
    if (pa, pb) in cache:
        return
    cache.add((pa, pb))
    if (a[0] * pa + b[0] * pb) > p[0]:
        return
    if (a[1] * pa + b[1] * pb) > p[1]:
        return
    
    if (a[0] * pa + b[0] * pb) == p[0] and (a[1] * pa + b[1] * pb) == p[1]:
        costs.append(cost)
        return
    
    play(a, b, pa+1, pb, p, cost+3, cache)
    play(a, b, pa, pb+1, p, cost+1, cache)
    return

spend = 0
for machine in machines:
    a, b, p = machine
    costs = []
    cache = set()
    play(a, b, 0, 0, p, 0, cache)
    if not costs:
        continue
    spend += costs[0]
print(spend)
