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
h = max([r[1] for r in rocks])

sand = set()
void = False
while not void:
    s = (500, 0)

    while True:
        down = (s[0], s[1] + 1)
        left = (s[0] - 1, s[1] + 1)
        right = (s[0] + 1, s[1] + 1)

        if down not in rocks and down not in sand:
            s = down
        elif left not in rocks and left not in sand:
            s = left
        elif right not in rocks and right not in sand:
            s = right
        else:
            sand.add(s)
            break

        if s[1] > h:
            void = True
            break

#part 1
print(len(sand))