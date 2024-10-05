input = "input.txt"

trees = {}
for r, row in enumerate(open(input).readlines()):
    row = row.strip()
    for c, col in enumerate(row):
        trees[(r, c)] = int(col)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visible = 0
for t in trees:
    if t[0] == 0 or t[1] == 0:
        visible += 1
        continue

    h = trees[t]
    for d in dirs:
        vis = True
        p = (t[0] + d[0], t[1] + d[1])
        while p in trees:
            if trees[p] >= h:
                vis = False
                break
            p = (p[0] + d[0], p[1] + d[1])
        if vis:
            visible += 1
            break
#part 1
print(visible)