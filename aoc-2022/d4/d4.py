input = "input.txt"

ranges = []
for r in open(input).readlines():
    ranges.append(list(map(int, r.replace("-", ",").split(","))))

def range_contains(x):
    return x[0] <= x[2] and x[1] >= x[3] or x[2] <= x[0] and x[3] >= x[1] 

def range_overlap(x):
    l = set(range(x[0], x[1] + 1))
    r = set(range(x[2], x[3] + 1))
    return len(l.intersection(r)) != 0

contains = 0
overlap = 0
for r in ranges:
    if range_contains(r):
        contains += 1
    if range_overlap(r):
        overlap += 1
#print 1
print(contains)
#print 2
print(overlap)