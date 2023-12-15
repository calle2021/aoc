input = "input.txt"

seq = [l.strip() for l in open(input).read().split(",")]

def hash(label):
    value = 0
    for l in label:
        value += ord(l)
        value *= 17
        value %= 256
    return value

res = 0
for init in seq:
    res += hash(init)
#part 1
print(res)