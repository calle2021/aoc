infile = "input.txt"

data = []
for line in open(infile):
    line = line.strip()
    line = line.replace(" -> ", ",")
    line = [int(l) for l in line.split(",")]
    data.append(line)

def sign(start, end):
    if start < end:
        return 1
    else:
        return -1

d = {}
for l in data:
    if l[0] != l[2] and l[1] != l[3]:
        continue
    
    points = []
    if l[0] == l[2]:
        i = [n for n in range(l[1], l[3] + sign(l[1], l[3]), sign(l[1], l[3]))]
        points = [(l[0], y) for y in i]
    elif l[1] == l[3]:
        i = [n for n in range(l[0], l[2] + sign(l[0], l[2]), sign(l[0], l[2]))]
        points = [(x, l[1]) for x in i]
        
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
