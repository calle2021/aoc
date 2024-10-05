input = "input.txt"

insturctions = [r.strip() for r in open(input).readlines()]

H = (0, 0)
T = (0, 0)

def touching(T, H):
    cords = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            cords.append((H[0] + i, H[1] + j))
    return T in cords

visited = set((0,0))
dirs = {"R" : (1, 0), "L" : (-1, 0), "U" : (0, -1) , "D" : (0, 1)}
for i in insturctions:
    d, steps = i.split(" ")
    d = dirs[d]
    for s in range(int(steps)):
        H = (H[0] + d[0], H[1] + d[1])
        if touching(T, H):
            continue
        T = (H[0] - d[0], H[1] - d[1])
        visited.add(T)
#part 1
print(len(visited))

