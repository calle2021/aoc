import re
input = "input.txt"

almanac = [d.strip() for d in open(input).read().split("\n\n")]

data = list(map(int, re.findall("\d+", almanac.pop(0).split("seeds: ")[1])))
seeds = [(x, x + y) for x, y in zip(data[::2], data[1::2])]

maps = []
for a in almanac:
    m = []
    for i in a.split("\n")[1:]:
        dst, src, len = list(map(int, re.findall("\d+", i)))
        m.append([dst, src, len])
    maps.append(m)

for m in maps:
    seed_dest = []
    while seeds:
        start, end = seeds.pop(0)
        for dst, src, len in m:
            s = max(start, src)
            e = min(end, src + len)
            if s >= e: continue #no overlap
            seed_dest.append((dst + s - src, dst + e - src))
            if start < s :
                seeds.append((start, s))
            if e < end:
                seeds.append((e, end))
            break
        else:
            seed_dest.append((start, end))
    seeds = seed_dest

#part 2
print(min([s[0] for s in seeds]))