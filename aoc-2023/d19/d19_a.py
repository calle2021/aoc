input = "input.txt"

workflows, ratings = open(input).read().split("\n\n")

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

parts = []
for rating in ratings.splitlines():
    r = {}
    lst = rating.replace("{", "").replace("}", "").split(",")
    for l in lst:
        n, v = l.split("=")
        r[n] = int(v)
    parts.append(r)

s = 0
for p in parts:
    curr = "in"
    acc = None
    while acc == None:
        for w in workflow[curr]:
            if type(w) == str:
                if w == "A":
                    acc = True
                elif w == "R":
                    acc = False
                else:
                    curr = w
                break

            key = list(w.keys())[0]
            comp = w[key]
            res = False
            if comp[0] == "<":
                res = p[key] < comp[1]
            else:
                res = p[key] > comp[1]
            if not res:
                continue
            
            res = w["d"]

            if res == "A":
                acc = True
            elif res == "R":
                acc = False
            else:
                curr = res
            break
    if acc:
        s += sum(v for v in p.values())
print(s)