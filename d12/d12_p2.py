import re
input = "ex0.txt"
rows = [d.strip() for d in open(input).readlines()]

arrangements = 0 
for row in rows:
    r, c = row.split(" ")
    group = list(eval(c))
    indicies = [i.start() for i in re.finditer(r"\?", r)] 
    pattern = ["(?=([.?]*"]

    for g in group:
        pattern.append(("[?#]{" + str(g) + "}"))
    pattern.append("[.?]*))")
    pattern = '[.?]+'.join(pattern)
    print(pattern)
    #res = re.findall(pattern, r)
    break
