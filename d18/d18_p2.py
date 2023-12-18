input = "input.txt"

dirs = {0 : 1, 1 : 1j, 2 : -1, 3 : -1j}

plan = open(input).read().split("\n")
edges = [0]
border = 0
curr = 0
for edge in plan:
    _, _, color = edge.split(" ")
    d = int(color[-2])
    a = int(color[2:-2], 16)
    curr += a * dirs[d]
    border += a
    edges.append(curr)

e = len(edges)
areas = []
for i in range(e):
    areas.append(edges[i].real * (edges[(i + 1) if i + 1 < e else 0].imag - edges[i - 1].imag)) # shoelace formula
area = int(sum(areas) / 2 + border / 2 + 1)
#part 2
print(area)
