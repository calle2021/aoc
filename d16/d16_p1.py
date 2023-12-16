import numpy as np
input = "input.txt"

grid = np.array([[c for c in g] for g in open(input).read().split("\n")])
mx = len(grid[0, :]) - 1 
my = len(grid[:, 0]) - 1


mirrors = {"/" : {(1, 0) : [(0, -1)], (-1, 0) : [(0, 1)], (0, 1) : [(-1, 0)], (0, -1) : [(1, 0)]}, 
           "\\" : {(1, 0) : [(0, 1)], (-1, 0) : [(0, -1)], (0, 1) : [(1, 0)], (0, -1) : [(-1, 0)]},
           "|" :  {(1, 0) : [(0, 1), (0, -1)], (-1, 0) : [(0, -1), (0, 1)], (0, 1) : [(0, 1)], (0, -1) : [(0, -1)]},
           "-" :  {(1, 0) : [(1, 0)], (-1, 0) : [(-1, 0)], (0, 1) : [(-1, 0), (1, 0)], (0, -1) : [(-1, 0), (1, 0)]}}


def neighbours(curr):
    symbol = grid[curr[1], curr[0]]
    if symbol == ".":
        next = (curr[0] + curr[2], curr[1] + curr[3], curr[2], curr[3])
        next = [next] if 0 <= next[0] <= mx and 0 <= next[1] <= my else []
        return next
    ds = mirrors[symbol][(curr[2], curr[3])]
    ns = []
    for d in ds:
        next = (curr[0] + d[0], curr[1] + d[1], d[0], d[1])
        if 0 <= next[0] <= mx and 0 <= next[1] <= my:
            ns.append(next)
    return ns
    
q = [(0, 0, 1, 0)]
reached = set()
reached.add((0, 0, 1, 0))
while q:
    curr = q.pop(0)
    ns = neighbours(curr)
    for next in ns:
        if next not in reached:
            q.append(next)
            reached.add(next)

energized = {(r[0], r[1]) for r in reached}

#part 1
print(len(energized))