input = "input.txt"

history = [list(map(int, h.strip().split(" "))) for h in open(input).readlines()]

def seq(h):
    return [h[i] - h[i-1] for i in range(1, len(h))]

values = []
for h in history:
    row = seq(h)
    rows= [h, row]
    while row.count(0) != len(row):
        row = seq(row)
        rows.append(row)
    rows = list(reversed(rows))
    rows[0].insert(0, 0)
    for i in range(1, len(rows)):
        d = rows[i-1][0]
        rows[i].insert(0, (rows[i][0] - d))
    else:
        values.append(rows[i][0])

print(sum(values))