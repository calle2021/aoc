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
    d = (dx, dy, dz)
    brick = [s]
    while s != e:
        s = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
        brick.append(s)
    bricks.append(sorted(brick, key=lambda x: x[2]))

bricks = sorted(bricks, key=lambda x : x[0][2])

for i, brick in enumerate(bricks):
    stack = set()
    for brick_ in bricks[:i]:
        stack |= {b_ for b_ in brick_}
    while True:
        if any(z == 1 for x, y, z in bricks[i]):
            break
        b = {(x, y, z - 1) for x, y, z in bricks[i]}

        if b & stack: # collision
            break

        bricks[i] = list(b)

bricks = sorted(bricks, key=lambda x : x[0][2])
supports = {}

i = len(bricks)
for i in range(len(bricks)):
    dis = bricks.pop(i)
    count = set()
    bricks_ = bricks.copy()
    for j, brick in enumerate(bricks_):
        stack = set()
        for brick_ in bricks_[:j]:
            stack |= {b_ for b_ in brick_}
        while True:
            if any(z == 1 for x, y, z in bricks_[j]):
                break
            b = {(x, y, z - 1) for x, y, z in bricks_[j]}

            if b & stack: # collision
                break

            bricks_[j] = list(b)
            count.add(j)

    supports[i] = len(count)

    bricks.insert(i, dis)
#part 1
print(sum([1 for s in supports.values() if s == 0]))
#part 2
print(sum([s for s in supports.values() if s != 0]))
