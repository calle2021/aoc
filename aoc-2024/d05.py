from aocd import get_data

puzzle = get_data(day=5, year=2024)
rules, updates = puzzle.split("\n\n")

rules = [tuple(map(int, x.split("|"))) for x in rules.split("\n")]
updates = [list(map(int, x.split(","))) for x in updates.split("\n")]

before = {}
after = {}

for rules in rules:
    x, y = rules
    if x in before:
        before[x].append(y)
    else:
        before[x] = [y]
    if y in after:
        after[y].append(x)
    else:
        after[y] = [x]

mid = 0
incorrect = []
for update in updates:
    ok = True
    for i, u in enumerate(update):
        b = update[:i]
        a = update[i+1:]
        if u in before:
            if any([x in before[u] for x in b]):
                ok = False
                incorrect.append(update)
                break
        if u in after:
            if any([x in after[u] for x in a]):
                ok = False
                incorrect.append(update)
                break
    if ok:
        mid += update[len(update) // 2]
print(mid)

def bubble(inc):
    l = len(inc)
    for i in range(len(inc)):
        for j in range(l - i - 1):
            if inc[j + 1] not in before:
                continue
            if inc[j] in before[inc[j + 1]]:
                inc[j], inc[j + 1] = inc[j + 1], inc[j]
    return inc

mid = 0
for inc  in incorrect:
    inc = bubble(inc)
    mid += inc[len(inc)//2]
print(mid)