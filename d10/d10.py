input = "input.txt"

loops = [d.strip() for d in open(input).readlines()]

pipes = {}
for y, loop in enumerate(loops):
    for x, pipe in enumerate(loop):
        if pipe == ".": continue
        p = (x, y)
        pipes[p] = pipe
        if pipe == "S": start = p

connections = {"|" : [(0, 1), (0, -1)],
                "-" : [(-1, 0), (1, 0)],
                "L" : [(1, 0), (0, -1)],
                "J" : [(-1, 0), (0, -1)],
                "7" : [(-1, 0), (0, 1)],
                "F" : [(1, 0), (0, 1)]
}

def neighbour(curr, came_from):
    for c in connections[pipes[curr]]:
        n =  (curr[0] + c[0], curr[1] + c[1])
        if n == came_from: continue
        return n

start_node = (start[0] - 1, start[1]) #hardcoded for my input data

curr = start_node
came_from = start
steps = 1
paths = [start]
while curr != start:
    paths.append(curr)
    next = neighbour(curr, came_from)
    came_from = curr
    curr = next
    steps += 1

#part 1
print(int(steps / 2))

dirs = {"|" : {(0, -1) : [(-1, 0)], (0, 1) : [(1, 0)]}, 
         "-" : {(1, 0) : [(0, -1)], (-1, 0) : [(0, 1)]},
         "L" : {(1, 0) : [], (0, -1) : [(-1, 0), (0, 1)]},
         "J" : {(0, -1) : [], (-1, 0) : [(1, 0), (0, 1)]},
         "7" : {(-1, 0) : [], (0, 1) : [(0, -1), (1, 0)]},
         "F" : {(0, 1) : [], (1, 0) : [(-1, 0), (0, -1)]},
}

enclosing = set()
for came_from, curr in zip(paths[:], paths[1:]):
    dxy = (came_from[0] - curr[0], came_from[1] - curr[1])
    d = [x for x in connections[pipes[curr]] if x != dxy][0]
    tiles = dirs[pipes[curr]][d]
    for t in tiles:
        tile = (curr[0] + t[0], curr[1] + t[1])
        while tile not in paths:
            enclosing.add(tile)
            tile = (tile[0] + t[0], tile[1] + t[1])
#part 2
print(len(enclosing))

