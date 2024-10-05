import string

input = "input.txt"
prio = list(string.ascii_lowercase) + list(string.ascii_uppercase)
rucksacks = [r.strip() for r in open(input).readlines()]

s1 = 0
for r in rucksacks:
    left = set(r[:len(r)//2])
    right = set(r[len(r)//2:])
    s1 += prio.index(left.intersection(right).pop()) + 1
#part 1
print(s1)

s2 = 0
group = []
for r in rucksacks:
    group.append(r)
    if len(group) == 3:
        s2 += prio.index(set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()) + 1
        group = []
#part 2
print(s2)
