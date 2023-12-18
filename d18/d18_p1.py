input = "input.txt"

dirs = {"R" : 1, "L" : -1, "D" : 1j, "U" : -1j}

plan = open(input).read().split("\n")
edges = set()
curr = 0
for edge in plan:
    d, amt, color = edge.split(" ")
    for a in range(int(amt)):
        curr += dirs[d]
        edges.add(curr)
interior = set()
for edge in plan:
    d, amt, color = edge.split(" ")
    for a in range(int(amt)):
        curr += dirs[d]
        r = dirs[d] * 1j
        s = curr + r
        while s not in edges:
            interior.add(s)
            s += r
edges |= interior
print(len(edges))