from aocd import get_data

puzzle = get_data(day=15, year=2024)

grid, moves = puzzle.split("\n\n")
m = {"<" : -1, ">" : 1, "^" : -1j, "v" : 1j}
moves = moves.replace("\n", "")
moves = [m[x] for x in moves.strip()]

boxes = set()
boxesx = {}
walls = set()
for y, row in enumerate(grid.split("\n")):
    for x, col in enumerate(row):
        x = x + x
        curr = x + y * 1j
        extra = curr + 1
        if col == ".":
            continue
        if col == "#":
            walls.add(curr)
            walls.add(extra)
        if col == "O":
            boxes.add(curr + 0.5)
            boxesx[curr] = curr + 0.5
            boxesx[extra] = curr + 0.5
        if col == "@":
            robot = curr

def moveboxesx(curr, dir):
    q = []
    while True:
        curr += dir
        if curr in walls:
            q = []
            break
        if curr not in walls and curr not in boxesx:
            break
        q.append(curr)
    return q

def moveboxesy(curr, dir):
    q = []
    #find all boxes that are connected in the current direction?
    box = boxesx[curr + dir]
    q = [box]
    connected = set()
    connected.add(box)
    while q:
        c = q.pop(0)
        neighbours = []
        for offset in [-1, 0, 1]:
            box = c + offset + move
            if box in boxes:
                neighbours.append(box)
        for next in neighbours:
            q.append(next)
            connected.add(next)
    #check if any of these are facing a wall in the current direction
    q = []
    for box in connected:
        left = box - 0.5
        right = box + 0.5
        if left + move in walls or right + move in walls:
            q = []
            break
        q.append(left)
        q.append(right)
    return q

for i, move in enumerate(moves):
    curr = robot + move
    if curr not in walls and curr not in boxesx: #immediate empty
        robot += move
        continue
    if curr in walls: #immediate wall
        continue
    Q = []
    if move == 1 or move == -1: #moving in x (don't consider half steps)
        Q = moveboxesx(robot, move)
    else:
        Q = moveboxesy(robot, move)
    if not Q: continue
    robot += move

    newboxes = []
    for q in Q:
        b = boxesx[q]
        boxes -= {b}
        newboxes.append(b + move)
        del boxesx[q]
    for q, nb in zip(Q, newboxes):
        boxesx[q + move] = nb
        boxes.add(nb)
        
GPS = sum([int(b.real - 0.5 + b.imag * 100) for b in boxes])
print(GPS)



