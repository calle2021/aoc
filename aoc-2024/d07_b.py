from aocd import get_data

puzzle = get_data(day=7, year=2024)
def combs(i, v, e):
    if i == len(e) - 1:
        unique.append(v + e[i])
        unique.append(v * e[i])
        unique.append(int(str(v) + str(e[i])))
        return
    combs(i+1, v + e[i], e)
    combs(i+1, v * e[i], e)
    combs(i+1, int(str(v) + str(e[i])), e)

tot = 0
for eq in puzzle.split("\n"):
    r, e = eq.split(":")
    e = list(map(int, e.strip().split()))
    r = int(r)
    unique = []
    combs(1, e[0], e)
    if r in unique:
        tot += r
print(tot)