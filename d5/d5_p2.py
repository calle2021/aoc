import re
input = "ex0.txt"

almanac = [d.strip() for d in open(input).read().split("\n\n")]

data = list(map(int, re.findall("\d+", almanac.pop(0).split("seeds: ")[1])))
seeds = [(x, y) for x, y in zip(data[::2], data[1::2])]

maps = []
for a in almanac:
    t = []
    for i in a.split("\n")[1:]:
        t.append(list(map(int, re.findall("\d+", i))))
    maps.append(t)


## soil, fert, wat, light, temp, hum , loc
# 50 98 2 dest range, source range, range length

def inside(x, d, s ,l):
    return s <= x <= s + l

# idea split current range up in smaller ranges that fit the correct range, and add thsoe to new seeds
for m in maps:
    new_seeds = []

    while seeds:
        start, end = seeds.pop(0)
        for d, s, l in m:
            i, res = inside(start, d, s, l)
            if not res:
                seeds.append((start,end))
            start_dest = d + start - s
            
