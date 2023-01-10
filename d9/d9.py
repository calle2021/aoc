infile = "input.txt"
data = []
for line in open(infile):
    line = line.strip()
    data.append(eval(line))
#print(data)

#part 1
l = 25
mean = []
res = 0
for i, n in enumerate(data):
    if i < l:
        mean.append(n)
        continue

    var = False
    for x in mean:
        for y in mean:
            if x + y == n:
                var = True
    
    if not var:
        res = n
        print(n)
        break
    else:
        mean.pop(0)
        mean.append(n)
        
var = True
x = 0
while var:
    sum = 0
    mn = float("inf")
    mx = 0
    n = x
    while True:
        sum += data[n]
        if sum > res:
            break
        mn = min(mn, data[n])
        mx = max(mx, data[n])
        if sum == res:
            print(mn + mx)
            var = False
            break
        n += 1
    x += 1



