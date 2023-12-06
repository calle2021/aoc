import re
input = "input.txt"

time, distance = [d.strip() for d in open(input).readlines()]

time = list(map(int, re.findall("\d+", time)))
distance = list(map(int, re.findall("\d+", distance)))

rec = 1
for t, d in zip(time, distance):
    records = 0
    for wait in range(t + 1):
        speed = wait
        dist = speed * (t - wait)
        if dist > d: records += 1
    rec *= records
#part 1
print(rec)