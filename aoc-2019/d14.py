from aocd.models import Puzzle
from math import ceil
year = 2019
day = 14
puzzle = Puzzle(year=year, day=day).examples[3].input_data

reactions = {}
for r in puzzle.strip().splitlines():
    m, c = r.split("=>")
    c = c.split(" ")[-2:]
    m = m.split(",")
    m = [x.strip() for x in m]
    m = [x.split() for x in m]
    m = [(x[1], int(x[0])) for x in m]
    reactions[c[1]] = {
        "produced" : int(c[0]),
        "material" :  m
    }

excess = {r : 0 for r in reactions}
material = {}
def rec(curr, n):
    if reactions[curr]["material"][0][0] == "ORE":
        return curr, n
    n = ceil(n / reactions[curr]["produced"])
    for next, amount in reactions[curr]["material"]:
        amount *= n
        if amount > excess[next]:
            amount -= excess[next]
            excess[next] = 0
        else:
            excess[next] -= amount
            continue
        val = rec(next, amount)
        if not val: continue
        base, v = val
        prod = ceil(v / reactions[base]["produced"]) * reactions[base]["produced"]
        e = prod - v
        excess[base] += e
        if base in material:
            material[base] += prod
        else:
            material[base] = prod
    return
rec("FUEL", 1)
print(sum([ceil(material[x] / reactions[x]["produced"]) * reactions[x]["material"][0][1] for x in material]))