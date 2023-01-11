infile = "input.txt"

data = []
for line in open(infile):
    line = line.strip()
    data.append(eval(line))

data = sorted(data)
data.append(max(data) + 3)
data.insert(0, 0)

#part 1
jolt_1 = 0
jolt_3 = 0

for i in range(0, len(data)-1):
    d = data[i+1] - data[i]
    if d == 1:
        jolt_1 += 1
    elif d == 3:
        jolt_3 += 1
print(jolt_1*jolt_3)

#part 2 dynamic
dyn = {}
def rec(i):
    if i == len(data) - 1:
        return 1
    if i in dyn:
        return dyn[i]
    res = 0
    for idx in range(i+1, len(data)):
        if data[idx] - data[i] > 3:
            break
        res += rec(idx)
    dyn[i] = res
    return res
print(rec(0))