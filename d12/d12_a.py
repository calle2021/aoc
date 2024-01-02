
input = "input.txt"
rows = [d.strip() for d in open(input).readlines()]

cache = {}
def rec(s, g, checking = False):
    key = (s, *g, checking)
    if key in cache:
        return cache[key]
    if not s:
        return 1 if g == [] or g == [0] else 0
    if not g:
        return 0 if "#" in s else 1
    
    res = 0
    if s[0] == ".":
        if checking:
            if g[0] == 0:
                res += rec(s[1:], g[1:], False)
        else:
            res += rec(s[1:], g, False)
    elif s[0] == "#":
        if checking:
            if g[0] != 0:
                res += rec(s[1:], [g[0] - 1] + g[1:], True)
        else:
            res +=  rec(s[1:], [g[0] - 1] + g[1:], True)
    elif s[0] == "?":
        if checking:
            if g[0] == 0:
                res += rec(s[1:], g[1:], False)
            else:
                res += rec(s[1:], [g[0] - 1] + g[1:], True)
        else:
            if g[0] == 0:
                res += rec(s[1:], g[1:], False)
            else:
                res += rec(s[1:], g, False) + rec(s[1:], [g[0] - 1] + g[1:], True)
    cache[key] = res
    return res

count = 0 
for row in rows:
    spring, group = row.split(" ")
    group = list(eval(group))
    count += rec(spring, group)
#part 1
print(count)
