input = "input.txt"

ins, maps = [d for d in open(input).read().split("\n\n")]
ins = [ 1 if i == "R" else 0 for i in ins]

network = {}
for m in maps.split("\n"):
    node, t = m.split(" = ")
    t = tuple(t.replace("(", "").replace(")","").split(", "))
    network[node] = t

start = "AAA"
goal = "ZZZ"
i = 0
steps = 0
while start != goal:
    start = network[start][ins[i]]
    i = (i + 1) % len(ins)
    steps += 1
#part 1
print(steps)