
lst = [0,13,1,8,6,15]
last_idx = {}
for i, n in enumerate(lst):
        last_idx[n] = i
turn = 2020 #part 1
turn = 30000000 #part 2

while len(lst) < 2020:
    prev = lst[-1]
    prev_idx = last_idx.get(prev, -1)
    last_idx[prev] = len(lst) - 1
    if prev_idx == -1:
        nxt_ = 0
    else:
        nxt_ = len(lst) - prev_idx - 1
    lst.append(nxt_)
print(lst[-1])
