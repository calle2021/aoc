infile = "input.txt"

active = set()
a = set()
for i, line in enumerate(open(infile)):
        line = line.strip()
        for j, c in enumerate(line):
            if c == "#":
                active.add((j, i, 0))
            a.add((j, i, 0))

dirs = [] 
for i in range(-1, 2):
    for j in range(-1, 2):
        for k in range(-1, 2):
            if i == 0 and j == 0 and k == 0:
                continue
            dirs.append((i,j,k))

def get_neighbours(a):
    a_ = set()
    for s in a:
        a_.add(s)
        for d in dirs:
            cube = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
            a_.add(cube)
    return a_

def get_actives(a, ac):
    active_ = set()
    for s in a:
        active_count = 0
        inacitve_count = 0 
        for d in dirs:
            cube = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
            if cube in ac:
                active_count += 1
            else:
                inacitve_count += 1
        if s in ac:
            if active_count == 2 or active_count == 3:
                active_.add(s)   
        else:
            if active_count == 3:
                active_.add(s)
    return active_

for i in range(6):
    a = get_neighbours(a)
    active = get_actives(a, active)

print(len(active))
