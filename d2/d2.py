infile = "input.txt"

with open(infile) as f:
    input = f.read()
    ins = input.splitlines()

aim = 0
p1 = (0, 0)
p2 = (0, 0)
for i in ins:
    dir , dist = i.split()
    dist = int(dist)
    if dir == "forward":
        p1 = (p1[0] + dist, p1[1])
        p2 = (p2[0] + dist, p2[1] + aim * dist)
    elif dir == "down":
        p1 = (p1[0], p1[1] + dist)
        aim += dist
    else:
        p1 = (p1[0], p1[1] - dist)
        aim -= dist

print(p1[0] * p1[1]) #part 1
print(p2[0] * p2[1]) #part 2
