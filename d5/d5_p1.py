import re
input = "input.txt"

almanac = [d.strip() for d in open(input).read().split("\n\n")]

seeds = list(map(int, re.findall("\d+", almanac.pop(0).split("seeds: ")[1])))



maps = []
for a in almanac:
    t = []
    for i in a.split("\n")[1:]:
        t.append(list(map(int, re.findall("\d+", i))))
    maps.append(t)

def inside(x, range):
    for i, r in enumerate(range):
        if r[1] <= x <= r[1] + r[2]:
            return i, True
    return 0, False

## soil, fert, wat, light, temp, hum , loc
# 50 98 2 dest range, source range, range length
locs =[]
for s in seeds:
    s_ = s
    for m in maps:
        idx, res = inside(s_, m)
        if not res:
            dest = s_
            #print("Seed n", s , "correspond", dest)
        else: 
            ## i know what range to check 
            dest = m[idx][0] + (s_ - m[idx][1])
            #print("Seed n", s , "correspond", dest)
        s_ = dest
    else:
        locs.append(s_)
print(min(locs))