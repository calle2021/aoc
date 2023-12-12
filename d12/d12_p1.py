
import re
input = "input.txt"
rows = [d.strip() for d in open(input).readlines()]

arrangements = 0 
for row in rows:
    r, c = row.split(" ")
    group = list(eval(c))
    indicies = [i.start() for i in re.finditer(r"\?", r)]

    combinations = []
    for x in r:
        if x == "?":
            new = []
            if len(combinations) == 0:
                new.append("#")
                new.append(".")
            else:
                for comb in combinations:
                    new.append(comb + "#")
                    new.append(comb + ".")
            combinations = new
        else:
            if len(combinations) == 0:
                combinations.append(x)
            else:
                combinations = [c + x for c in combinations ]

    for c in combinations:
        arrangement = [len(r) for r in re.findall(r"#*",c) if len(r) > 0]
        if arrangement == group:
            arrangements += 1

print(arrangements)

