input = "input.txt"

data = open(input).read().splitlines()

bricks = []
for d in data:
    s, e = d.split("~")
    s = eval(s)
    e = eval(e)
    dx = e[0] - s[0]
    dy = e[1] - s[1]
    dz = e[2] - s[2]
    dx = dx // abs(dx) if dx else dx
    dy = dy // abs(dy) if dy else dy
    dz = dz // abs(dz) if dz else dz
    delta = (dx, dy, dz)
    brick = set()   
    while s != e:
        brick.add(s)
        s = (s[0] + delta[0], s[1] + delta[1], s[2] + delta[2])
    else:
        brick.add(e)
    bricks.append(brick)

settled = []
while bricks:
    brick = bricks.pop(0)
    if any(z == 1 for x, y, z in brick):
        settled.append(brick)
        continue
    
    b = {(x, y, z - 1) for x, y, z in brick}

    if any(b & x for x in bricks): # collision
        bricks.append(brick)
        continue

    if any(b & x for x in settled):
        settled.append(brick)
        continue
    bricks.append(b)

tot = 0
for _ in range(len(settled)):
    s = settled.pop(0)
    safe = True
    for brick in settled:
        if any(z == 1 for x, y, z in brick):
            continue
        b = {(x, y, z - 1) for x, y, z in brick}
        if any(b & x for x in settled if x != brick):
            continue
        safe = False
        break
    tot += 1 if safe else 0
    settled.append(s)
print(tot)