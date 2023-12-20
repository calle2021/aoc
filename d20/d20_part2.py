from math import lcm
input = "input.txt"

data = [m.strip() for m in open(input).read().splitlines()]

class Module:
    def __init__(self, right, memory):
        self.right = right
        self.memory = memory

conjunction = {}
flip_flop = {}
broadcaster = {}

for m in data:
    t, right = m.split(" -> ")
    right = right.split(", ")
    name = t[1:]
    if "%" in t:
        flip_flop[name] = Module(right, False)
    elif "&" in t:
        conjunction[name] = Module(right, {})
    else:
        broadcaster = Module(right, None)


master = "ql"
controllers = {}
for f in flip_flop:
    for r in flip_flop[f].right:
        if r in conjunction:
            conjunction[r].memory.update({f : False})
for c in conjunction:
    for r in conjunction[c].right:
        if r in conjunction:
            conjunction[r].memory.update({c : False})
        if r == master:
            controllers.update({c : 0})

q = [("broadcaster", False)]
i = 1
while q:
    curr, signal = q.pop(0)
    if curr == "broadcaster":
        module = broadcaster.right
    elif curr in conjunction:
        module = conjunction[curr].right
    elif curr in flip_flop:
        module = flip_flop[curr].right
    else:
        print("lol")

    for m in module:
        if m in flip_flop:
            if signal:
                continue
            if flip_flop[m].memory:
                flip_flop[m].memory = False
                q.append((m, False))
            else:
                flip_flop[m].memory = True
                q.append((m, True))
        elif m in conjunction:
            conjunction[m].memory[curr] = signal
            if all(x == True for x in conjunction[m].memory.values()):
                q.append((m, False))
            else:
                q.append((m, True))
                if m in controllers:
                    if controllers[m] == 0:
                        controllers[m] = i  
    
    if all(x != 0 for x in controllers.values()):
        print(lcm(*controllers.values()))
        break
    if q: 
        continue

    q.append(("broadcaster", False))
    i += 1
