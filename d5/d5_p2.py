import re
input = "ex0.txt"

almanac = [d.strip() for d in open(input).read().split("\n\n")]

data = list(map(int, re.findall("\d+", almanac.pop(0).split("seeds: ")[1])))
seeds = [(x, x + y) for x, y in zip(data[::2], data[1::2])]

maps = []
for a in almanac:
    t = []
    for i in a.split("\n")[1:]:
        t.append(list(map(int, re.findall("\d+", i))))
    maps.append(t)


## soil, fert, wat, light, temp, hum , loc
# 50 98 2 dest range, source range, range length

def inside(x, s ,l):
    return s <= x <= s + l

# idea split current range up in smaller ranges that fit the correct range, and add thsoe to new seeds
for m in maps:
    new_seeds = []
    while seeds:
        start, end = seeds.pop(0)
        for d, s, l in m:
            if not inside(start,s, l):
                continue

            start_dest = d + abs(start - s)
            max_s = s + l
            if max_s >= end:
                end_dest = d + abs(end - s)
                new_seeds.append((start_dest, end_dest))
                break
            else:
                seeds.append((max_s, end))
                break
        else:
            new_seeds.append((start, end))

    seeds = new_seeds
    print(seeds)

print(seeds)

