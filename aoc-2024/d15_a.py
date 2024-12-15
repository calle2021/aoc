from aocd import get_data

puzzle = get_data(day=15, year=2024)

grid, moves = puzzle.split("\n\n")
m = {"<" : -1, ">" : 1, "^" : -1j, "v" : 1j}
moves = moves.replace("\n", "")
moves = [m[x] for x in moves.strip()]

boxes = set()
walls = set()

for y, row in enumerate(grid.split("\n")):
    for x, col in enumerate(row):
        curr = x + y * 1j
        if col == ".":
            continue
        if col == "#":
            walls.add(curr)
        if col == "O":
            boxes.add(curr)
        if col == "@":
            robot =  curr

def moveboxes(curr, dir):
    q = []
    while True:
        curr += dir
        if curr in walls:
            q = []
            break
        if curr not in walls and curr not in boxes:
            break
        q.append(curr)
    return q

for i, move in enumerate(moves):
    curr = robot + move
    if curr not in walls and curr not in boxes:
        robot += move
        continue
    if curr in walls:
        continue
    Q = moveboxes(robot, move)
    if not Q: continue
    robot += move
    for q in Q:
        boxes.remove(q)
    for q in Q:
        boxes.add(q + move)
        
GPS = sum([int(b.real + b.imag * 100) for b in boxes])
print(GPS)



