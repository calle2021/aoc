from collections import deque
infile = "input.txt"
mask = {}

for line in open(infile):
    line = line.strip()
    if "mask" in line:
        mask[line.split("= ")[1]] = []
        curr = line.split("= ")[1]
    else:
        line = line.replace("mem[", "")
        line = line.replace("]", "")
        m, i = line.split(" = ")
        mask[curr].append((int(m) , int(i)))

def bfs(s, idxs):
    q = deque([s])
    seen = set()
    while q:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)

        for n in idxs:
            zero = curr[:n] + "0" + curr[n + 1:]
            one = curr[:n] + "1" + curr[n + 1:]
            q.append(zero)
            q.append(one)
    return seen

memory = {}
for key in mask:
    for nbr in mask[key]:
        address = '{0:036b}'.format(nbr[0])
        idxs = []
        res = ""
        for i, b in enumerate(address):
            if key[i] == "X":
                res += "0"
                idxs.append(i)
            elif key[i] == "1":
                res += "1"
            else:
                res += address[i]
        ads = bfs(res, idxs)
        for ad in ads:
            memory[ad] = nbr[1]
s = 0
for m in memory:
    s += memory[m]
print(s)
