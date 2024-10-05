input = "ex.txt"
ms = [m.strip() for m in open(input).readlines()]

monkeys = []
called = {}
for m in ms:
    name, yell = m.split(": ")
    if yell.isnumeric():
        called[name] = int(yell)
        continue
    yell = yell.split(" ")
    if name == "root":
        root = [yell[0], yell[1], yell[2]]
        continue
    monkeys.append([name, yell[0], yell[1], yell[2]])

i = 0
while True:
    if root[0] in called and root[2] in called:
        break
    n, y1, o, y2 = monkeys.pop(0)
    if y1 in called and y2 in called:
        res = eval(f"{called[y1]} {o} {called[y2]}")
        called[n] = res
        continue

    monkeys.append([n, y1, o, y2])


print(int(eval(f"{called[root[0]]} {root[1]} {called[root[2]]}")))
