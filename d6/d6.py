infile = "input.txt"

with open(infile) as f:
    f = [int(x) for x in f.readline().split(",")]

data = [i for i in range(0, 9)]

for i, _ in enumerate(data):
    data[i] = f.count(i)

for i in range(256):
    d = data.pop(0)
    data.append(d)
    data[6] += d

    if i == 80:
        #part 1
        print(sum(data))
else:
    #part 2
    print(sum(data))
