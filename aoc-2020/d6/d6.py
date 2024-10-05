infile = "input.txt"

data = []
res = 0
with open(infile) as file:
    lines = file.readlines()
    last = lines[-1]
    count = 0
    d = {}
    for line in lines:
        if line == "\n":
            for k in d:
                if d[k] >= count:
                    res += 1
            data.append(d)
            d = {}
            count = 0 
        else:
            l = line.strip()
            count += 1
            for c in l:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
            if line is last:
                for j in d:
                    if d[j] >= count:
                        res += 1
                data.append(d)
sum = 0
for d in data:
    for c in d:
        sum += len(c)
#part 1
print(sum)

#part 2
print(res)