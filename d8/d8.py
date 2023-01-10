infile = "input.txt"
ins = []
for line in open(infile):
    line = line.strip()
    action, amt = line.split()
    if "-" in amt:
        amt = -1 * int(amt[1:])
    else:
        amt = int(amt[1:])
    ins.append((action, amt))

def calc(ins):
    acc = 0
    visited = set()
    curr = 0
    found = False
    while True:
        if curr >= len(ins):
            found = True
            break
        i, idx = ins[curr]
        if curr in visited:
            break
        visited.add(curr)
        if i == "nop":
            curr += 1
        elif i == "acc":
            acc += idx
            curr += 1
        elif i == "jmp":
            curr += idx
    return acc, found

# part 1
acc, _ = calc(ins)
print(acc)
    
# part 2
ins2 = ins.copy()
converter = {"jmp" : "nop", "nop" : "jmp"}

for n in range(0, len(ins)):
    if ins[n][0] == "acc":
        continue
    ins2[n] = (converter[ins2[n][0]], ins2[n][1])
    acc, found = calc(ins2)
    if found:
        print(acc)
        break
    ins2[n] = (converter[ins2[n][0]], ins2[n][1])
    