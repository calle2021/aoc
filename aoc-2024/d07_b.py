from aocd import get_data

puzzle = get_data(day=7, year=2024)

def equations(e, v):
    if len(e) == 1:
        eqs.append(v)
        return
    equations(e[1:], v + e[1])
    equations(e[1:], v * e[1])
    equations(e[1:], int(str(v) + str(e[1])))

res = 0
for eq in puzzle.split("\n"):
    r, e = eq.split(":")
    e = list(map(int, e.strip().split()))
    r = int(r)
    eqs = []
    equations(e, e[0])
    if r in eqs:
        res += r
print(res)
