input = "input.txt"

dirs = {"R" : 1, "L" : -1, "D" : 1j, "U" : -1j}

plan = open(input).read().split("\n")
edges = set()
curr = 0
for edge in plan:
    d, a, color = edge.split(" ")
    for a in range(int(a)):
        curr += dirs[d]
        edges.add(curr)
interior = set()
for edge in plan:
    d, a, color = edge.split(" ")
    for a in range(int(a)):
        curr += dirs[d]
        r = dirs[d] * 1j
        s = curr + r
        while s not in edges:
            interior.add(s)
            s += r
edges |= interior
#part 1
print(len(edges))