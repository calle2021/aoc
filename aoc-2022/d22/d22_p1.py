import re
input = "input.txt"

board, instructions = open(input).read().split("\n\n")

tiles = set()
void = set()
walls = set()
start_x = float("inf")
for y, b in enumerate(board.split("\n")):
    for x, tile in enumerate(b):
        if tile == " ":
            void.add((x, y))
        if tile == ".":
            tiles.add((x, y))
            if y == 0:
                start_x = min(start_x, x)
        if tile == "#":
            walls.add((x, y))
rot = {
    "R" : lambda x, y: (-y, x),
    "L" : lambda x, y: (y, -x)
}
tot = tiles | void | walls
d = (1, 0)
s = (start_x, 0)

instructions = list(re.findall(r"[A-Z]+|\d+", instructions))
paths = set()
paths.add(s)
for i in instructions:
    if not i.isdigit():
        d = rot[i](d[0], d[1])
        continue
    for _ in range(int(i)):
        step = (s[0] + d[0], s[1] + d[1])
        if step in walls:
            break
        if step in void or step not in tot:
            s_ = (step[0] - d[0], step[1] - d[1])
            while s_ in tiles or s_ in walls:
                s_ = (s_[0] - d[0], s_[1] - d[1])
            s_ = (s_[0] + d[0], s_[1] + d[1])
            if s_ in walls:
                break
            step = s_
        s = step
        paths.add(s)

facing_score = {(1, 0) : 0, (0, -1) : 1, (-1, 0) : 2, (0, 1) : 3}
print( 1000 * (s[1] + 1) + 4 * (s[0] + 1)  + facing_score[d] )


