infile = "ex.txt"

with open(infile) as f:
    data = [ int(i) for i in f.read().split(",") ]

mx = max(data)
mn = min(data)
fuel = float("inf")

for i in range(mn, mx):
    fs = [abs(x - i) for x in data]
    s = sum(fs)
    fuel = min(fuel, s)
print(fuel)