
import re
input = "input.txt"

data = [list(map(int, re.findall(r'-?\d+', d.strip()))) for d in open(input).readlines()]
print(data)
def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])
beacons = set()
sensors = set()
row = 2000000
count = set()
for i in data:
    sensor, beacon = (i[0], i[1]), (i[2], i[3])
    if beacon[1] == row:
        beacons.add(beacon)
    if sensor[1] == row:
        sensors.add(sensor)
    
    dist = manhattan(sensor, beacon)
    reach = abs(sensor[1] - row)
    if reach > dist: # too far away
        continue
    remainder = (dist - reach)
    for i in range(-remainder, remainder+1):
        count.add((sensor[0] + i, row))
print(len(count - sensors - beacons))
