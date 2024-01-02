from math import lcm
input = "input.txt"

ins, maps = [d for d in open(input).read().split("\n\n")]
ins = [ 1 if i == "R" else 0 for i in ins]

network = {}
for m in maps.split("\n"):
    node, t = m.split(" = ")
    t = tuple(t.replace("(", "").replace(")","").split(", "))
    network[node] = t

start = [n for n in network if "A" in n]
i = 0
steps = 1
magic = {}
while True:
    for s, _ in enumerate(start):
        start[s] = network[start[s]][ins[i]]
        if "Z" in start[s] and s not in magic:
            magic[s] = steps
    if len(magic) == len(start): break
    i = (i + 1) % len(ins)
    steps += 1

ms = list(magic.values())
#part 2
print(lcm(*ms))
