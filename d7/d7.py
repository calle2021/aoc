from collections import deque
infile = "input.txt"

data = {} # for part 1
vals = {} # for part 2
zeros = set()
for line in open(infile):
    line = line.strip()
    line = line.replace(" ", "")
    line = line.replace("contain", ",")
    line = line.replace("bags", "")
    line = line.replace("bag", "")
    line = line.replace("noother", "0")
    line = line.replace(".", "")
    first = line.split(",")[0]
    lst = line.split(",")[1:]
    for l in lst:
        x = l[0]
        s = l[1:]
        if x == "0":
            zeros.add(first)
        if first in vals:
            vals[first].append((s,int(x)))
        else:
            vals[first] = [(s, int(x))]
        if s not in data:
            data[s] = []
        data[s].append(first)

#part 1 BFS
tar = "shinygold"
seen = set()
q = deque([tar])
while q:
    curr = q.popleft()
    if curr in seen:
        continue 
    seen.add(curr)
    for x in data.get(curr, []):
        q.append(x)

print(len(seen)-1)    

#part 2 DFS
def dfs(target):
    size = 1
    if target in zeros:
        return size
    for (s, x) in vals[target]:
        size += x*dfs(s)
    return size
print(dfs(tar)-1)