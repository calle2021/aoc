input = "input.txt"

with open(input) as f:
    calories = sorted([sum(list(map(int, filter(None, c.split("\n"))))) for c in f.read().split("\n\n")])

print(calories[-1])
print(sum(calories[-3:]))
