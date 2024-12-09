from aocd import get_data
import re

puzzle = """2333133121414131402"""

#puzzle = get_data(day=9, year=2024)

puzzle = list(map(int, [x for x in puzzle]))
system = []

for i, x in  enumerate(puzzle):
    if i % 2 == 0:
        system = system + [str(i // 2)] * x
    else:

        system = system + ["."] * x

files = [x.group() for x in re.finditer(r"(\d)\1*", ''.join(system))][::-1]
free = [x.group() for x in re.finditer("\.+", ''.join(system))]

print(files)
print(free)
exit()
while files:
    f = files.pop(0)
    for i in range(len(free)):
        if len(free[i]) >= len(f):
            for j in range(len(f)):
                free[i].pop()
            
checksum = 0
for i, x in enumerate(system):
    if x == ".":
        continue
    checksum += i * int(x)
print(checksum)