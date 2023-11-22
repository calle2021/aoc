input = "input.txt"

trees = {}
for r, row in enumerate(open(input).readlines()):
    row = row.strip()
    for c, col in enumerate(row):
        trees[(r, c)] = int(col)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_scenic_score = 0
for t in trees:
    scenic_score = 1
    h = trees[t]
    for d in dirs:
        viewing_distance = 0
        p = (t[0] + d[0], t[1] + d[1])
        while p in trees:
            viewing_distance += 1
            if trees[p] >= h:
                break
            p = (p[0] + d[0], p[1] + d[1])
        scenic_score *= viewing_distance
    max_scenic_score = max(max_scenic_score, scenic_score)
#part 2
print(max_scenic_score)