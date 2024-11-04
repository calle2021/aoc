from aocd.models import Puzzle
year = 2019
day = 6
puzzle = Puzzle(year=year, day=day)
com = {}
for node in puzzle.input_data.strip().split("\n"):
    x, y  = node.split(")")
    if x not in com:
        com[x] = [y]
        continue
    com[x].append(y)
paths = []
def rec(key, x=0):
    paths.append(x)
    if key not in com:
        return x
    for k in com[key]:
       rec(k, x+1)
rec("COM")
print(sum(paths))
