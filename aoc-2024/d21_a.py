from aocd import get_data
from collections import defaultdict
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

def bfs(start, goal, grid):
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
        seq = bfs(nx, ny, numgrid)
        for s in seq:
            nsequances[(numgrid[nx], numgrid[ny])].append(s)
dsequances = defaultdict(list)
for dx in dirgrid:
    for dy in dirgrid:
        if dx == dy:
            dsequances[(dirgrid[dx], dirgrid[dy])].append("A")
            continue
        seq = bfs(dx, dy, dirgrid)
        for s in seq:
            dsequances[(dirgrid[dx], dirgrid[dy])].append(s)


def dfs(sequance, robot):
    if robot == 0:
        return
    for seq in sequance:
        print(seq)
        break

def combinations(comb, i, curr=""):
    if i == len(comb):
        combs.append(curr)
        return
    for c in comb[i]:
        combinations(comb, i+1, curr + c + "A")
    return

complexities = 0
for code in puzzle.split("\n"):
    numeric = int(''.join(c for c in code if c.isdigit()))
    code = [int(x) if x.isdigit() else x for x in code]
    start = "A"
    comb = []
    for c in code:
        goal = c
        comb.append(nsequances[(start, goal)])
        start = goal
    combs = []
    combinations(comb, 0, "")
    for comb in combs:
        print(comb)
        dfs(comb, 2)
        break
    break
print(complexities)