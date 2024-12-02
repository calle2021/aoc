from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=2).input_data
reports = []
for x in puzzle.split("\n"):
    reports.append([int(y) for y in x.split()])

def issafe(x):
    asc = sorted(x)
    desc = asc[::-1]
    if x != asc and x != desc:
        return False
    for i in range(1, len(x)):
        if abs(x[i-1] - x[i]) > 3:
            return False
        if abs(x[i-1] - x[i]) < 1:
            return False
    return True

n1 = n2 = 0
for report in reports:
    if issafe(report):
        n1 += 1
        n2 += 1
        continue
    for i in range(len(report)):
        tmp = report.pop(i)
        if issafe(report):
            n2 += 1
            break
        report.insert(i, tmp)
print(n1, n2)
