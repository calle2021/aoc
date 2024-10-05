file = "ex.txt"

dict = {2: 1, 3: 7, 7: 8, 4: 4}
s = 0
for line in open(file).readlines():
    left, right = line.split(" | ")
    left = left.split()
    right = [set(x) for x in right.split()]
    d = {}
    q = []
    # get unique ones
    while left:
        x = left.pop()
        if len(x) in dict.keys():
            d[dict[len(x)]] = set(x)
        else:
            q.append(set(x))
    # find 9
    for i, x in enumerate(q):
        if d[4].issubset(x):
            d[9] = x
            break
    q.pop(i)

    # find 3
    for i, x in enumerate(q):
        if x.issubset(d[9]) and d[1].issubset(x):
            d[3] = x
            break
    q.pop(i)

    # find 5
    for i, x in enumerate(q):
        if x.issubset(d[9]):
            d[5] = x
            break
    q.pop(i)

    # find 0
    for i, x in enumerate(q):
        if d[1].issubset(x):
            d[0] = x
            break
    q.pop(i)

    # find 6
    for i, x in enumerate(q):
        if d[5].issubset(x):
            d[6] = x
            break
    q.pop(i)
    d[2] = q.pop()
    digits = ""
    for i in right:
        for n in d.keys():
            if d[n] == i:
                digits += str(n)
                break
    s += int(digits)

print(s)
