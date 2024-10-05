from math import lcm
input = "input.txt"

module_config = [m for m in open(input).read().splitlines()]

conjunction = {}
flip_flop = {}
broadcaster = {}
connections = []

for m in module_config:
    t, dest = m.split(" -> ")
    dest = dest.split(", ")
    name = t[1:]
    if "%" in t:
        flip_flop[name] = {"dest" : dest, "memory" : False}
    elif "&" in t:
        conjunction[name] = {"dest" : dest, "memory" : {}}
    else:
        broadcaster = {"dest" : dest}
    connections.append([name, dest])

master = "ql"
controllers = {}

for c, dest in connections:
    for d in dest:
        if d in conjunction:
            conjunction[d]["memory"].update({c : False})
        if d == master:
            controllers.update({c : 0})

q = [("broadcaster", False)]
i = 1
while True:
    curr, signal = q.pop(0)

    if curr == "broadcaster":
        modules = broadcaster["dest"]
    elif curr in conjunction:
        modules = conjunction[curr]["dest"]
    else:
        modules = flip_flop[curr]["dest"]
        
    for m in modules:
        if m in flip_flop:
            if signal:
                continue
            if flip_flop[m]["memory"]:
                flip_flop[m]["memory"] = False
                q.append((m, False))
            else:
                flip_flop[m]["memory"] = True
                q.append((m, True))
        elif m in conjunction:
            conjunction[m]["memory"][curr] = signal
            if all(c for c in conjunction[m]["memory"].values()):
                q.append((m, False))
            else:
                q.append((m, True))
                if m in controllers and controllers[m] == 0:
                    controllers[m] = i
    if all(c for c in controllers.values()):
        break
    if q: continue
    q.append(("broadcaster", False))
    i += 1
    
print(lcm(*controllers.values()))