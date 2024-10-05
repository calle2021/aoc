input = "input.txt"

buffer = open(input).read()

def solve(buffer, size):
    window = []
    for i, c in enumerate(buffer):
        if len(window) < size:
            window.append(c)
            continue
        window.pop(0)
        window.append(c)
        if len(set(window)) == size:
            return i + 1
#part 1
print(solve(buffer, 4))
#part 2
print(solve(buffer, 14))