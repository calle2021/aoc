import sympy
input = "input.txt"

data = [t.strip() for t in open(input).read().splitlines()]

trajectories = []
for d in data:
    vals = eval(d.replace(" @ " ,", "))
    trajectories.append(vals)

b = [200000000000000, 400000000000000]
count = 0
while trajectories:
    t1 = trajectories.pop(0)
    for t2 in trajectories:
        mx1, my1, mz1, x1, y1, z1 = t1
        mx2, my2, mz2, x2, y2, z2 = t2
        x, y = sympy.symbols("x y")
        eq1 = sympy.Eq(x1 * x + mx1,  x2 * y + mx2)
        eq2 = sympy.Eq(y1 * x + my1, y2 * y + my2)
        solution = sympy.solve((eq1, eq2), (x, y))
        if not solution:
            continue
        if solution[x] < 0 or solution[y] < 0:
            continue
        x_val = x1 * solution[x] + mx1
        y_val = y1 * solution[x] + my1
        if b[0] <= x_val <= b[1] and b[0] <= y_val <= b[1]:
            count += 1
print(count)
