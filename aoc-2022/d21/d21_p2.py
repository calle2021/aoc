import sympy
input = "input.txt"

op = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y,
}

ms = [m.strip() for m in open(input).readlines()]


monkeys = []
called = {}
for m in ms:
    name, yell = m.split(": ")
    if yell.isnumeric():
        called[name] = sympy.Integer(yell)
        continue
    yell = yell.split(" ")
    if name == "root":
        root = [yell[0], yell[1], yell[2]]
        continue
    monkeys.append([name, yell[0], yell[1], yell[2]])
    
called["humn"] = sympy.Symbol("x")

while True:
    if root[0] in called and root[2] in called:
        print(sympy.solve(called[root[0]] - called[root[2]]))
        break
    n, y1, o, y2 = monkeys.pop(0)
    if y1 in called and y2 in called:
        res = op[o](called[y1], called[y2])
        called[n] = res
        continue
    monkeys.append([n, y1, o, y2])