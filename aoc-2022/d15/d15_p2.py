
import re
import time
input = "ex.txt"

data = [list(map(int, re.findall(r'-?\d+', d.strip()))) for d in open(input).readlines()]

def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

beacons = set()
sensors = set()
count = {}
for i in data:
    sensor, beacon = (i[0], i[1]), (i[2], i[3])

    for row in range(0, 20):
        dist = manhattan(sensor, beacon)
        reach = abs(sensor[1] - row)
        if reach > dist: # too far away
            continue
        remainder = (dist - reach)
        if row in count:
            count[row].append((sensor[0]-remainder, sensor[0] + remainder))
        else:
            count[row] = [(sensor[0]-remainder, sensor[0] + remainder)]
# i want to check if the ranges cover 0, 20 completely

def overlap(x, y):
    return x[1] >= y[0] and x[0] <= y[0] or y[1] >= x[0] and y[0] <= x[0]

def cover(v):
    x = v.pop(0)
    while v:
        pop = None
        for y in v:
            print("comparing", (x, y))
            if overlap(x, y):
                print("Found overlap!!",(min(x[0], y[0]), max(x[1], y[1])) )
                new = (min(x[0], y[0]), max(x[1], y[1]))
                v.append(new)
                pop = y
                break

        if pop != None:
            print("popping y", v[v.index(y)])
            v.pop(v.index(y))
            x = v.pop(0)
        else:
            v.append(x)
            x = v.pop(0)
        print(v)
        time.sleep(1)

print(count[0])
cover(count[0])
exit()

for x in range(0, 20):
    for y in range(0, 20):
        if (x,y) in count:
            print("#", end="")
        else:
            print(".", end="")
    print("")
