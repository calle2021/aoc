import re
input = "input.txt"

time, distance = [d.strip() for d in open(input).readlines()]

time = list(map(int, re.findall("\d+", time.replace(" ", ""))))[0]
distance = list(map(int, re.findall("\d+", distance.replace(" ", ""))))[0]

records = 0
for wait in range(time + 1):
    speed = wait
    dist = speed * (time - wait)
    if dist > distance: records += 1
#part 2
print(records)