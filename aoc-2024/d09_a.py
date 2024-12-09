from aocd import get_data

puzzle = """2333133121414131402"""

puzzle = get_data(day=9, year=2024)

puzzle = list(map(int, [x for x in puzzle]))
system = []

for i, x in  enumerate(puzzle):
    if i % 2 == 0:
        system = system + [str(i // 2)] * x
    else:
        system = system + ["."] * x

free = [i for i, x in enumerate(system) if x == "."]
files = [i for i, x in enumerate(system) if x != "."][::-1]

while free:
    f = free.pop(0)
    file = files.pop(0)
    system[f] = system[file]
    system[file] = "."
    idx = system.index(".")
    if set(system[idx:]) == set("."):
        break

checksum = 0
for i, s in enumerate(system):
    if s == ".":
        break
    checksum += i * int(s)
print(checksum)
