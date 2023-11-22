input = "input.txt"

rock_structures = [[eval(r_) for r_ in r.strip().split(" -> ")] for r in open(input).readlines()]
rocks = set()
for strucutre in rock_structures:
    for i in range(1, len(strucutre)):
        r1 = strucutre[i-1]
        r2 = strucutre[i]
        dx = r1[0] - r2[0]
        dy = r1[1] - r2[1]
        l = abs(dx) + abs(dy)
        for j in range(l + 1):
            if dx == 0:
                rocks.add((r1[0], int(r1[1] - j * dy/abs(dy))))
            else:
                rocks.add((int(r1[0] - j * dx/abs(dx)), r1[1]))
floor = max([r[1] for r in rocks]) + 2

sand = set()
while True:
    s = (500, 0)

    falling = True
    while True:
        down = (s[0], s[1] + 1)
        left = (s[0]-1, s[1] + 1)
        right = (s[0]+ 1, s[1] + 1)

        if down not in rocks and down not in sand and down[1] != floor:
            s = down
        elif left not in rocks and left not in sand and left[1] != floor:
            s = left
        elif right not in rocks and right not in sand and right[1] != floor:
            s = right
        else:
            sand.add(s)
            break
    if (500, 0) in sand:
        break
#part 2
print(len(sand))