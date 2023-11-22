input = "input.txt"
#input = "ex2.txt"
program = [p.strip() for p in open(input).readlines()]

multiple = [40, 80, 120, 160, 200, 240]
X = 1
cycle = 1
tot = 0

for p in program:
    if cylce in multiple:
        print("")
    
    tot += signal_strength(X, cycle)
    if p == "noop":
        cycle += 1
        continue
    cycle += 1
    tot += signal_strength(X, cycle)
    cycle += 1

    X += int(p.split(" ")[1])

print(tot)