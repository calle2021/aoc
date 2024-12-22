from aocd import get_data

puzzle = """029A
980A
179A
456A
379A"""
puzzle = get_data(day=21, year=2024)

numpad = {7 : (0, 0), 8 : (1, 0), 9 : (2, 0), 4 : (0, 1), 5 : (1, 1), 6 : (2, 1), 1 : (0, 2), 2 : (1, 2), 3 : (2, 2), 0 : (1, 3), "A" : (2, 3)}
numgrid = {v : k for k, v in numpad.items()}

dirpad = {(1, 0) : (2, 1), (-1, 0) : (0, 1), (0, -1) : (1, 0), (0, 1) : (1, 1), "A" : (2, 0)}
dirgrid = {v : k for k, v in dirpad.items()}

codes = puzzle.split("\n")

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def pathfind(start, goal, grid):
    q = [(start, 0, [], [])]
    sequance = []
    mh = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    while q:
        curr, cost, path, seq = q.pop(0)
        x, y = curr
        if curr == goal:
            if cost > mh: continue
            sequance.append(seq)
            continue

        for dx, dy in dirs:
            next = (x + dx, y + dy)
            if next not in grid or next in path: continue
            q.append((next, cost + 1, path + [next], seq + [(dx, dy)]))
    return sequance

def get_sequance(keys, pad, grid):
    start = pad["A"]
    sequances = [[]]
    for key in keys:
        goal = pad[key]
        sequance = pathfind(start, goal, grid)
        sequancesx = []
        for seq in sequance:
            for seqs in sequances:
                sequancesx.append(seqs + seq + ["A"])
        sequances = sequancesx
        start = goal
    return sequances

def print_sequance(sequance):
    output = ""
    for seq in sequance:
        match seq:
            case (-1, 0): output += "<"
            case (1, 0): output += ">"
            case (0, 1): output += "v"
            case (0, -1): output += "^"
            case "A": output += "A"
    output += "\n"
    return output

def write_sequance(sequance):
    output = ""
    for seq in sequance:
        output += print_sequance(seq)
    with open("sequance.txt", "a") as file:
        file.write(output)

complexities = 0
for code in puzzle.split("\n"):
    numeric =  numeric = int(''.join(c for c in code if c.isdigit()))
    code = [int(x) if x.isdigit() else x for x in code]
    sequances = get_sequance(code, numpad, numgrid)
    sequancesx = []
    for seq in sequances:
        seq_ = get_sequance(seq, dirpad, dirgrid)
        for s in seq_:
            sequancesx.append(s)
    sequances = sequancesx

    sequancesx = []
    for seq in sequances:
        seq_ = get_sequance(seq, dirpad, dirgrid)
        for s in seq_:
            sequancesx.append(s)
    sequances = sequancesx
    length = []
    for seq in sequances:
        length.append(len(seq))
    print(min(length), numeric)
    complexities += min(length) * numeric
    #write_sequance(sequancesx)
print(complexities)