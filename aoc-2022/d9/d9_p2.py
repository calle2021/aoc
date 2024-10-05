import numpy as np
input = "input.txt"

insturctions = [r.strip() for r in open(input).readlines()]

rope = [(0, 0) for i in range(10)]
print(rope)

def touching(T, H):
    cords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            cords.append((H[0] + i, H[1] + j))
    return T in cords

def diagonal(T, H):
    return T[0] != H[0] and T[1] != H[0]

def sign(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    return -1
def printer(rope):
    print(rope)
    print(rope[2])
    for y in range(-15, 15):
        for x in range(-15, 15):
            if (x, y) in rope:
                print(rope.index((x,y)), end="")
            else:
                print(".", end="")
        print("")
            


visited = set((0,0))
dirs = {"R" : (1, 0), "L" : (-1, 0), "U" : (0, -1) , "D" : (0, 1)}
for i in insturctions:
    d, steps = i.split(" ")
    print("==", d, steps, "==")
    d = dirs[d]
    
    for s in range(int(steps)):
        prev = rope[0]
        rope[0] = (rope[0][0] + d[0], rope[0][1] + d[1])
        for i in range(1, 10):
            nxt_prev = rope[i]
            if touching(rope[i], rope[i-1]):
                continue
            if diagonal(rope[i], rope[i-1]):
                rope[i] = (rope[i][0] - sign(rope[i][0] - rope[i-1][0]), rope[i][1] - sign(rope[i][1] - rope[i-1][1]))
            else:
                rope[i] = prev
            prev = nxt_prev
        visited.add(rope[-1])
        if int(steps) == 8 and d == (0, -1):
            printer(rope)
            print("")
    
#part 1
print(len(visited))

