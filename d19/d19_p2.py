from math import prod
input = "input.txt"

workflows, _ = open(input).read().split("\n\n")

workflow = {}
for row in workflows.splitlines():
    name, content = row.split("{")
    content = content[:-1].split(",")
    rules = []
    for c in content:
        r = {}
        if ":" not in c:
            rules.append(c)
            continue
        op, dest = c.split(":")
        if "<" in op:
            part, val = op.split("<")
            r = {part : ["<", int(val)], "d": dest}
        else:
            part, val = op.split(">")
            r = {part : [">", int(val)], "d": dest}
        rules.append(r)
    workflow[name] = rules

def combinations(ratings, curr="in"):
    if curr == "A":
        return prod([r[1] - r[0] + 1 for r in ratings.values()])
    if curr == "R":
        return 0
    res = 0
    for w in workflow[curr]:
        if type(w) == str:
            res += combinations(ratings, w)
            continue
        key = list(w.keys())[0]
        op, val = w[key]
        r = ratings.copy()
        if op == "<":          
            r[key] = (r[key][0], val - 1)
            ratings[key] = (val, ratings[key][1])
        else:
            r[key] = (val + 1, r[key][1])
            ratings[key] = (ratings[key][0], val)
        res += combinations(r, w["d"])
    return res

res = combinations({"x": (1, 4000), "m" : (1, 4000), "a" : (1, 4000), "s" : (1, 4000)})
#part 2
print(res)

