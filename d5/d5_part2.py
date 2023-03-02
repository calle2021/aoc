infile = "input.txt"

data = []
for line in open(infile):
    line = line.strip()
    line = line.replace(" -> ", ",")
    line = [int(l) for l in line.split(",")]
    data.append(line)

def interval(start, end):
    if start < end:
        return [n for n in range(start, end + 1)]
    else:
        return [n for n in range(end, start + 1)]
def sign(start, end):
    if start < end:
        return 1
    else:
        return -1
d = {}
for l in data:
    points = []
    if l[0] == l[2]:
        i = interval(l[1], l[3])
        points = [(l[0], y) for y in i]
    elif l[1] == l[3]:
        i = interval(l[0], l[2])
        points = [(x, l[1]) for x in i]
    else:
        rx = [x for x in range(l[0], l[2] + sign(l[0], l[2]), sign(l[0], l[2]))]
        ry = [y for y in range(l[1], l[3] + sign(l[1], l[3]), sign(l[1], l[3]))]
        for i, _ in enumerate(rx):
            points.append((rx[i], ry[i]))
    for p in points:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1

sum = 0
for d_ in d.values():
    if d_ > 1:
        sum += 1
print(sum)


