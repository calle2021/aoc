file = "input.txt"

d = {2: 0, 4: 0, 3: 0, 7: 0}
for f in open(file).readlines():
    output = f.split(" | ")[1].split()
    for o in output: 
        l = len(o)
        if l in d.keys():
            d[l] += 1

print(sum(d.values()))

