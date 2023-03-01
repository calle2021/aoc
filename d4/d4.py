import numpy as np
infile = "input.txt"

boards = []
with open(infile) as f:
    f = f.read()
    input = f.split("\n\n")
    seq = list(map(int, input.pop(0).split(",")))

    for board in input:
        rows = board.split("\n")
        row = []
        for r in rows:
            row_ = [int(r_) for r_ in r.split()]
            row.append(row_)
        arr = np.array(row)
        boards.append(arr)

def bingo(b, ns):
    for i in range(len(b)):
        if set(b[:, i]).issubset(ns):
            return True
        if set(b[i, :]).issubset(ns):
            return True

def sum_board(b, ns):
    s = 0
    for x in range(len(b)):
        for y in range(len(b)):
            if b[x, y] not in ns:
                s += b[x,y]
    return s

ns = set()
unique = set()
wons = []
for n in seq:
    ns.add(n)
    for i, b in enumerate(boards):
        if bingo(b, ns):
            if i not in unique:
                s = sum_board(b, ns)
                wons.append(s*n)
                unique.add(i)
#part 1
print(wons[0])

#part 2
print(wons[-1])