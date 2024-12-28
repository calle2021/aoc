from aocd import get_data
from collections import defaultdict
from itertools import product

puzzle = """029A
980A
179A
456A
379A"""
puzzle = """029A"""
#puzzle = get_data(day=21, year=2024)

codes = puzzle.split("\n")

numpad = {7 : (0, 0), 8 : (1, 0), 9 : (2, 0), 4 : (0, 1), 5 : (1, 1), 6 : (2, 1), 1 : (0, 2), 2 : (1, 2), 3 : (2, 2), 0 : (1, 3), "A" : (2, 3)}
numgrid = {v : k for k, v in numpad.items()}

dirpad = {">" : (2, 1), "<" : (0, 1), "^" : (1, 0), "v" : (1, 1), "A" : (2, 0)}
dirgrid = {v : k for k, v in dirpad.items()}

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ddirs = {(1, 0) : ">", (-1, 0) : "<", (0, 1) : "v", (0, -1) : "^"}

def paths(start, goal, grid):
    q = [(start, [], [])]
    sequance = []
    mh = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    while q:
        curr, path, seq = q.pop(0)
        x, y = curr
        if curr == goal:
            if len(path) > mh: continue
            sequance.append(''.join(seq))
            continue
        for dx, dy in dirs:
            next = (x + dx, y + dy)
            if next not in grid or next in path: continue
            q.append((next, path + [next], seq + [ddirs[(dx, dy)]]))
    return sequance

nsequances = defaultdict(list)
for nx in numgrid:
    for ny in numgrid:
        if nx == ny:
            nsequances[(numgrid[nx], numgrid[ny])].append("A")
            continue
        seq = paths(nx, ny, numgrid)
        for s in seq:
            nsequances[(numgrid[nx], numgrid[ny])].append(s)

dsequances = defaultdict(list)
for dx in dirgrid:
    for dy in dirgrid:
        if dx == dy:
            dsequances[(dirgrid[dx], dirgrid[dy])].append("A")
            continue
        seq = paths(dx, dy, dirgrid)
        for s in seq:
            dsequances[(dirgrid[dx], dirgrid[dy])].append(s)
            
complexities = 0
for code in puzzle.split("\n"):
    numeric = int(''.join(c for c in code if c.isdigit()))
    keys = [int(x) if x.isdigit() else x for x in code]
    start = "A"
    path = []
    for key in keys:
        goal = key
        path.append(nsequances[(start, goal)])
        start = goal
    combs = ['A'.join(c) + "A" for c in product(*path)]


    length = 0
    q = [(combs[0][0], "A", 2, "")]
    visited = {}
    print(dsequances[("A", "<")])
    while q:
        curr, start, depth, path = q.pop()
        print("#### here" , curr, start, depth, path)
        if depth == 0:
            print("PATH", path)
            continue
        for seq in curr:
            print(seq, start)
            for dseq in dsequances[(start, seq)]:
                q.append((dseq, seq, depth-1, path + dseq + "A"))

    break