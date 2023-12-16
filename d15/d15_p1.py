input = "input.txt"

seq = [l.strip() for l in open(input).read().split(",")]

def hash(init):
    value = 0
    for i in init:
        value += ord(i)
        value *= 17
        value %= 256
    return value

res = sum([hash(init) for init in seq])
#part 1
print(res)