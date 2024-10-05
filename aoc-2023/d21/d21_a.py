input = "input.txt"

rows = open(input).read().split("\n")

gardens = set()
rocks = set()
start = 0
mx = len(rows[0])
my = len(rows)
for y, row in enumerate(rows):
    for x, c in enumerate(row):
        g =  x + y * 1j
        if c == "S":
            start = g
            gardens.add(g)
        elif c == "#":
            rocks.add(g)
        elif c == ".":
            gardens.add(g)

dirs = [1, -1, 1j, -1j]
reached = {start}
for _ in range(64):
    new = set()
    while reached:
        r = reached.pop()
        garden = {r + x for x in dirs if r + x not in rocks}
        new |= garden
    reached = new
print(len(reached))
