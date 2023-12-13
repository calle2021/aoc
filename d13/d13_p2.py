input = "input.txt"

patterns = open(input).read().split("\n\n")

def reflection(rock, mx, my, res=0):
    for row in range(0, my): # reference horizontal line
        top = set()
        bottom = set()
        dy = min(my - row - 1, row + 1)
        for y in range(row - dy + 1, row + 1):
            for x in range(0, mx):
                if (x + y * 1j) in rock:
                    top.add(x + (row  + 1 - y) * 1j)
        for y in range(row + 1, row + dy + 1):
            for x in range(0, mx):
                if (x + y * 1j) in rock:
                    bottom.add(x + (y - row) * 1j)

        if top == bottom and top and bottom and res != (row + 1) * 100:
            return (row + 1) * 100

    for col in range(0, mx): # reference vertical line
        left = set()
        right = set()
        dx = min(mx - col - 1, col + 1)
        for x in range(col - dx + 1 , col + 1):
            for y in range(0, my):
                if (x + y * 1j) in rock:
                    left.add((col  + 1 - x) + y * 1j)
        for x in range(col + 1, col + dx + 1):
            for y in range(0, my):
                if (x + y * 1j) in rock:
                    right.add((x - col) + y * 1j)

        if left == right and left and right and res != col + 1:
            return col + 1

    return None

def replace_rock(rocks, res):
    for _ in range(len(rocks)):
        r = rocks.pop(0)
        new = reflection(rocks, mx, my, res)
        rocks.append(r)
        if not new:
            continue
        return new
    else:
        return None

def replace_ash(ash, rocks, res):
    for _ in range(len(ash)):
        a = ash.pop(0)
        rocks.append(a)
        new = reflection(rocks, mx, my, res)
        rocks.pop()
        if not new:
            continue
        return new
    else:
        return None


pattern = []
s = 0
for i, p in enumerate(patterns):
    ash = []
    rocks = []
    my = 0
    mx = 0
    for y, row in enumerate(p.split("\n")):
        my = max(my, y)
        for x, v in enumerate(row):
            mx = max(mx, x)
            if v == "#":
                rocks.append(x + y * 1j)
            else:
                ash.append(x + y * 1j)
    mx += 1
    my += 1
    res = reflection(rocks, mx, my)
    
    smudge = replace_rock(rocks[:], res)
    if smudge == None:
        smudge = replace_ash(ash[:], rocks[:], res)

    if smudge == None:
        print(p)
    else:
        s += smudge

print(s)