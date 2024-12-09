from aocd import get_data

puzzle = get_data(day=9, year=2024)

puzzle = list(map(int, [x for x in puzzle]))

q = []
free = []
p = 0
for i, x in enumerate(puzzle):
    if i % 2 == 0:
        q.append((p, x))
    else:
        free.append((p, x))
    p += x
res = q.copy()
i = len(q) - 1
while i > 0:
    start, number = q[i]
    for j, f in enumerate(free):
        if f[0] >= start:
            break
        if f[1] == number:
            res[i] = (f[0], number)
            free.pop(j)
            break
        if f[1] > number:
            res[i] = (f[0], number)
            free[j] = (f[0] + number, f[1] - number)
            break
    i -= 1
checksum = 0
for i, r in enumerate(res):
    for j in range(r[0], r[0] + r[1]):
        checksum += j * i
print(checksum)
