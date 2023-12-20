input = "ex.txt"

data = [m.strip() for m in open(input).read().splitlines()]
print(data)
class Module:
    def __init__(self, name, type, memory):
        self.n = name
        self.type = type
        self.right = None
        self.memory = memory
modules = {}
for m in data:
    t, right = m.split(" -> ")
    if "%" in t:
        type = t[0]
        name = t[1:]
        memory = False
    elif "&" in t:
        type = t[0]
        name = t[1:]
        memory = []
    else:
        type = None
        name = t
        memory = None
    right = right.split(", ")
    modules[name] = Module(name, type, memory)
    modules[name].right = right
#for m in modules:
#    print( modules[m].n, modules[m].type, modules[m].right, modules[m].memory)

broadcast = m["broadcast"]
while True:
