import sympy
input = "input.txt"

data = [t.strip() for t in open(input).read().splitlines()]

trajectories = []
for d in data:
    vals = eval(d.replace(" @ " ,", "))
    trajectories.append(vals)

mx, my, mz, x, y, z = sympy.symbols("mx my mz x y z")
eqs = []
for t in trajectories:
    mx1, my1, mz1, x1, y1, z1 = t
    eqs.append(sympy.Eq((mx1 - mx) * (y - y1) - (my1 - my) * (x - x1), 0))
    eqs.append(sympy.Eq((mx1 - mx) * (z - z1) - (mz1 - mz) * (x - x1), 0))
    eqs.append(sympy.Eq((my1 - my) * (z - z1) - (mz1 - mz) * (y - y1), 0))

solution = sympy.solve(eqs, (mx, my, mz, x, y, z))
print(sum(solution[0][i] for i in [0, 1, 2]))

