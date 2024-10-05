import re
input = "input.txt"

almanac = [d.strip() for d in open(input).read().split("\n\n")]

seeds = list(map(int, re.findall("\d+", almanac.pop(0).split("seeds: ")[1])))

maps = []
for a in almanac:
    m = []
    for i in a.split("\n")[1:]:
        dst, src, len = list(map(int, re.findall("\d+", i)))
        m.append([dst, src, len])
    maps.append(m)

locs =[]
for s in seeds:
    for m in maps:
        for dst, src, len in m:
            if not src <= s <= src + len:
                continue

            dest = dst + s - src
            s = dest
            break
    locs.append(s)
#part 1
print(min(locs))