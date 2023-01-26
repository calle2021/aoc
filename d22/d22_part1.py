infile = "input.txt"

with open(infile) as f:
    lines = f.read().split("\n\n")
    p1 =  list(map(int, lines[0].split(":")[1].split()))
    p2 =  list(map(int, lines[1].split(":")[1].split()))

while p1 and p2:
    c1 = p1.pop(0)
    c2 = p2.pop(0)

    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)
        
if p1:
    res = p1
else:
    res = p2

s = 0
for i, v in enumerate(reversed(res)):
    s += (i+1) * v
print(s)