file = "input.txt"

data = set()
instructions = []
with open(file) as f:
    f = f.read()

    dots, folds = f.split("\n\n")
    [data.add(eval(x)) for x in dots.split("\n")]
    for x in folds.split("\n"):
        x = x.strip().split()[2].split("=")
        instructions.append((x[0], int(x[1])))
for i, f in enumerate(instructions):
    dots = set()
    if f[0] == "y":
        for x, y in data:
            if y < f[1]:
                dots.add((x, y))
            else:
                dots.add((x, y - 2 * (y - f[1])))
    else:
        for x, y in data:
            if x < f[1]:
                dots.add((x, y))
            else:
                dots.add((x - 2 * (x - f[1]), y))
    data = dots
    if i == 0:
        # part 1
        print(len(data))

# part 2
data = sorted(data)
x_max, y_max = data[-1]
for y in range(y_max + 1):
    for x in range(x_max + 1):
        if (x, y) in data:
            print("#", end="")
        else:
            print(".", end="")
    print("")
