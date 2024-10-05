infile = "input.txt"

with open(infile) as f:
    lines = f.read().split("\n\n")
    p1 =  list(map(int, lines[0].split(":")[1].split()))
    p2 =  list(map(int, lines[1].split(":")[1].split()))

def game(p1, p2):
    
    visited_1 = set()
    visited_2 = set()

    while p1 and p2: 

        p1_ = tuple(p1)
        p2_ = tuple(p2)

        if p1_ in visited_1 or p2_ in visited_2:
            return p1, p2, "p1"
        visited_1.add(p1_)
        visited_2.add(p2_)
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if len(p1) >= c1 and len(p2) >= c2:
            _, _, win = game(p1[:c1], p2[:c2])
            if win == "p1":
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:    

            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
    if p1:
        res = "p1"
    else:
        res = "p2"
    return p1, p2, res


p1, p2, w = game(p1, p2)

if p1:
    res = p1
else:
    res = p2

s = 0
for i, v in enumerate(reversed(res)):
    s += (i+1) * v
print(s)