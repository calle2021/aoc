input = "input.txt"

seq = [s.strip() for s in open(input).readlines()]

data_structure = {"/" : 0}
PATH = []
for s in seq:
    if "$ ls" in s:
        continue
    elif "$ cd" in s:
        if ".." in s:
            PATH.pop(-1)
        else:
            PATH.append(s.split(" ")[-1])
    elif "dir " in s:
        p = ','.join(PATH) + "," + s.split(" ")[-1]
        if p not in data_structure:
            data_structure[p] = 0
    else:
        size, name = s.split(" ")
        path = []
        for p in PATH:
            path.append(p)
            data_structure[','.join(path)] += int(size)
#part 1
print(sum([s for s in data_structure.values() if s <= 100000]))
file_size = 30000000 - (70000000 - data_structure["/"])
file_candidates = []
for v in data_structure.values():
    if v >= file_size:
        file_candidates.append(v)
#part 2
print(min(file_candidates))