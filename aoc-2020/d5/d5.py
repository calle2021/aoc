infile = "input.txt"

data = []
for line in open(infile):
    line = line.strip()
    data.append(line)

def half( c, r, check):
    if c == check:
        r = (r[0], ( r[1] - r[0] ) // 2 + r[0])
    else:
        r = ( (r[1] - r[0] + 1) // 2 + r[0], r[1])
    return r

#part 1
ids = []
for d in data:
    FB = d[:-3]
    LR = d[-3:]
    row = (0, 127)

    for c in FB:
        row = half(c, row, "F")
    row = row[0]

    col = (0, 7)
    for c in LR:
        col = half(c, col, "L")

    col = col[0]
    ids.append(row * 8 + col)
        
print(max(ids))

#part 2
ids = sorted(ids)
last = ids[0]
for i in range(1, len(ids)):
    if ids[i] - last != 1:
        print(ids[i] - 1)
        break
    last = ids[i]
    