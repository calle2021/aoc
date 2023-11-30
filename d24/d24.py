from heapq import *
input = "ex0.txt"

data = open(input).read().split("\n")
directions = {">" : 1, "<" : -1, "^" : -1j, "v" : 1j}

ground = set()
blizzards = []
walls = set()

mx = 1
my = 1
My = len(data) - 2
Mx = len(data[0]) - 2

for y, line in enumerate(data):
    for x, c in enumerate(line):
        b =  x + y * 1j
        if y == 0 and c == ".":
            start = b
            ground.add(b)
            continue
        if y == len(data) - 1 and c == ".":
            goal = b
            ground.add(b)
            continue
        if c == "#":
            walls.add(b)
            continue
        if c in directions:
            blizzards.append([b ,  directions[c]])
            continue
        ground.add(c)

adj = {1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j}
mod = {1 : mx, -1 : Mx, 1j : my, -1j : My}
timestamp = [blizzards[:]]
p = {1 : ">" , -1 : "<" , 1j : "v", -1j : "^"}
def printer(blizz):
    b = [b_[0] for b_ in blizz]
    d = [b_[1] for b_ in blizz]
    for y in range(My + 2):
        for x in range(Mx + 2):
            curr = x + y * 1j
            if curr in walls:
                print("#", end="")
            elif curr in b:
                if b.count(curr) == 1:
                    print(p[d[b.index(x + y * 1j)]], end="")
                else:
                    print(b.count(curr), end="")
            else:
                print(".", end="")
        print("")

# find repetitions of storms and stack them 
blizzard = blizzards[:]
while True:
    t = []
    for i, b in enumerate(blizzard):
        new = b[0] + b[1]
        if isinstance(b[1], complex):
            if new in walls:
                t.append((b[0].real + mod[b[1]] * 1j, b[1]))
                continue
            t.append((new, b[1]))
        else:
            if new in walls:
                t.append((mod[b[1]] + b[0].imag * 1j, b[1]))
                continue
            t.append((new, b[1]))
    if t in timestamp:
        break
    timestamp.append(t)
    blizzard = t

def heuristic(a, b):
    return abs(int(a.real - b.real)) + abs(int(a.imag + b.imag))

front = []
heappush(front, (0, start))
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far = 0

while front:
    curr = heappop(front)
    if curr == goal:
        break
    