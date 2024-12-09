from aocd import get_data

puzzle = get_data(day=9, year=2024)
diskmap = list(map(int, [x for x in puzzle]))

filesystem = []
id = 0
for i, d in enumerate(diskmap):
    if i % 2 == 0:
        filesystem += [id] * d
        id += 1
    else:
        filesystem += ["."] * d

while True:
    file = filesystem.pop()
    if file == ".": continue
    found = False
    for i, x in enumerate(filesystem):
        if x != ".": continue
        filesystem[i] = file
        break
    else:
        filesystem.append(file)
        break
checksum = sum([i * x for i, x in enumerate(filesystem)])
print(checksum)
