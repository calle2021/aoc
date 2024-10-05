infile = "input.txt"

data = []
for line in open(infile):
    line = line.strip()
    data.append(eval(line))

target = 2020

#part 1
res = 0 
for i in data:
    for j in data:
        if i + j == target:
            res = i * j 
print(res)

#part 2
for i in data:
    for j in data:
        for k in data:
            if i + j + k == target:
                res = i * j * k 
print(res)