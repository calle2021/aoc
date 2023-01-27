ex = "389125467"
input = "123487596"

s = [int(i) for i in input]
l = len(s)
curr = 0
for _ in range(100):
    pick = []
    this_ = s[curr]
    dest = s[curr] - 1
    if dest == 0:
        dest = 9
    for i in range(3):
        if curr+1 < len(s):
            pick.append(s.pop(curr+1))
        else:
            pick.append(s.pop(0))

    while dest in pick:
        if dest != 1:
            dest -= 1
        else:
            dest = 9
    idx = s.index(dest)
    s.insert(idx+1, pick[0])
    s.insert(idx+2, pick[1])
    s.insert(idx+3, pick[2])
    curr = s.index(this_) + 1
    if curr == 9:
        curr = 0

idx_ = s.index(1)
s.pop(idx_)
res = []
while s:
    if idx_ < len(s):
        res.append(s.pop(idx_))
    else:
        res.append(s.pop(0))
res = ''.join(map(str, res))

print(res)