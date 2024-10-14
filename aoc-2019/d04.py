import re

puzzle = "136760-595730"

double_digits = [str(x) + str(x) for x in range(10)]

l, r = puzzle.split("-")
numbers = [l] if l == r else range(int(l), int(r))
a = b = 0
for n in numbers:
    n = str(n)
    if not any([d in n for d in double_digits ]): continue
    if not all( int(n[i]) <= int(n[i+1]) for i in range(len(n) - 1)): continue
    a += 1
    pattern = r"(.)\1{1,}"
    rep = [m.group() for m in re.finditer(pattern, n)]
    if any([len(x) == 2 for x in rep]):
        b += 1
print(a)
print(b)

