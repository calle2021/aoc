input = "input.txt"


round = []
square = []
stationary = []
my = 0
mx = 0
for y, row in enumerate( open(input).read().split("\n")):
    my = max(my, y)
    for x, v in enumerate(row):
        mx = max(mx, x)
        if v == "O":
            round.append(x + y * 1j) 
        elif v == "#":
            square.append(x + y * 1j)
            stationary.append(x + y * 1j)

round = sorted(round, key=lambda x: x.imag)

i = 0
load = 0
while round:
    curr = round.pop(0)
    while curr not in stationary and curr.imag >= 0:
        curr -= 1j
    curr += 1j
    load += int(my - curr.imag + 1)
    stationary.append(curr)
    i += 1
print(load)