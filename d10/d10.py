input = "input.txt"
#input = "ex2.txt"
program = [p.strip() for p in open(input).readlines()]

multiple = [20, 60, 100, 140, 180, 220]
X = 1
cycle = 1
tot = 0

def signal_strength(X, cycle):
    if cycle in multiple:
        return X * cycle
    return 0

for p in program:
    tot += signal_strength(X, cycle)
    if p == "noop":
        cycle += 1
        continue
    cycle += 1
    tot += signal_strength(X, cycle)
    cycle += 1

    X += int(p.split(" ")[1])

print(tot)