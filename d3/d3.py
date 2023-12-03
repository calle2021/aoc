import re
input = "input.txt"

schematic = [s.strip() for s in open(input).readlines()]

numbers = {}
symbols = {}
for y, row in enumerate(schematic):
    pattern = re.compile(r"\d+")
    indicies = [i.start() for i in pattern.finditer(row)]
    ns =  [n for n in pattern.findall(row)]

    for x, start in enumerate(indicies):
        indexes = [(start + dx, y) for dx in range(len(ns[x]))]
        numbers[tuple(indexes)] = ns[x]

    for x, c in enumerate(row):
        if not c.isdigit() and c != ".":
            symbols[(x, y)] = c

adjacent = [(1, 0), (-1, 0), (0, -1) , (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)] 

part_numbers = 0
gears = []
for s in symbols:
    adj = {(s[0] + a[0], s[1] + a[1]) for a in adjacent}
    gear = []
    for n in numbers:
        if adj & set(n):
            part_numbers += int(numbers[n])
            if symbols[s] == "*": gear.append(int(numbers[n]))
    gears.append(gear)
#part 1
print(part_numbers)

gear_ratios = 0
for g in gears:
    if len(g) != 2: continue
    gear_ratio = g[0] * g[1]
    gear_ratios += gear_ratio
#part 2
print(gear_ratios)