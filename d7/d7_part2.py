infile = "input.txt"

with open(infile) as f:
    data = [ int(i) for i in f.read().split(",") ]

mx = max(data)
mn = min(data)
fuel = float("inf")

for i in range(mn, mx):
    s = 0
    for x in data:
        s += sum([x for x in range(1, abs(x - i) + 1)])
    fuel = min(fuel, s)
print(fuel)