infile = "input.txt"

data = []
for i in open(infile):
    data.append(int(i))

count = 0
for i in range(1,len(data)):
    if data[i-1] < data[i]:
        count += 1
#part 1
print(count)

count = 0
prev = data[0] + data[1] + data[2]
for i in range(1, len(data)-2):
    curr = data[i] + data[i+1] + data[i+2]
    if curr > prev:
        count += 1
    prev = curr
#part 2
print(count)