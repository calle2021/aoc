input = "input.txt"

seq = [l.strip() for l in open(input).read().split(",")]


boxes = [[] for _ in range(256)]
indicies = {}

def hash(label):
    value = 0
    for l in label:
        value += ord(l)
        value *= 17
        value %= 256
    return value

for op in seq:
    if "=" in op:
        label, focal_length = op.split("=")
        focal_length = int(focal_length)
        i = hash(label)

        if label in indicies:
            curr = indicies[label]
            boxes[curr] = [[label, focal_length] if x[0] == label else x for x in boxes[curr]]
        else:
            boxes[i].append([label, focal_length])
            indicies[label] = i
    if "-" in op:
        i = hash(label)
        label = op.split("-")[0]
        if label in indicies:
            curr = indicies[label]
            boxes[curr] = [ x for x in boxes[curr] if x[0] != label ]
            del indicies[label]
res = 0
for i, b in enumerate(boxes):
    if not b:
        continue
    for j, lens in enumerate(b):
        res += (i + 1) * (j + 1) * lens[1]
#part 2
print(res)
