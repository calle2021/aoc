input = "input.txt"

patterns = open(input).read().split("\n\n")


def reflection(ash, rock, mx, my):

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

        if top == bottom and len(top) != 0 and len(bottom) != 0:
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

        if left == right and len(left) != 0 and len(right) != 0:
            return col + 1


pattern = []
s = 0
for p in patterns:
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
    res = reflection(ash, rocks, mx + 1, my + 1)
    s += res

print(s)