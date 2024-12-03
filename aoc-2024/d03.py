from aocd import get_data
import re

data = get_data(day=3, year=2024)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, data)
a = sum([int(m[0]) * int(m[1]) for m in matches])
print(a)

idxs = re.finditer(pattern, data)
dos = [m.start() for m in re.finditer( r"do\(\)", data)]
donts = [m.start() for m in re.finditer(r"don't\(\)", data)]
valid = []
v = True
for x in range(len(data)):
    if x in dos:
        v = True
    elif x in donts:
        v = False
    valid.append(v)

b = 0
for m, i in zip(matches, idxs):
    if not valid[i.start()]:
        continue
    b += int(m[0]) * int(m[1])
print(b)