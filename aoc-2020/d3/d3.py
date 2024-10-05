infile = "input.txt"

trees = set()
empty = set()

y = 0 
w = 0
h = 0
for line in open(infile):
    line = line.strip()
    x = 0
    for c in line:
        if c == ".":
            empty.add((x,y))
        elif c == "#":
            trees.add((x,y))
        w = max(w, x)
        x += 1
    h = max(h, y)
    y += 1

#part 1
trees_encountered = 0
curr = (0,0)
for i in range(h+2):
    if curr in trees:
        trees_encountered += 1

    x = curr[0] + 3
    if x > w:
        rem = w - curr[0] 
        x = 3 - rem - 1

    curr = (x, curr[1] + 1)
print(trees_encountered)


#part 2
trees_encountered = [0, 0, 0, 0, 0]
curr = [(0,0), (0,0), (0,0), (0,0), (0,0)]
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]
for i in range(h+1):
    for idx in range(len(curr)):
        if curr[idx] in trees:
            trees_encountered[idx] += 1
    
        x = curr[idx][0] + right[idx]
        if x > w:
            rem = w - curr[idx][0] 
            x = right[idx] - rem - 1

        curr[idx] = (x, curr[idx][1] + down[idx])

res = 1
for t in trees_encountered:
    res *= t
print(res)