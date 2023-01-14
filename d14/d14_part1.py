infile = "input.txt"
mask = {}
for line in open(infile):
    line = line.strip()
    if "mask" in line:
        mask[line.split("= ")[1]] = []
        curr = line.split("= ")[1]
    else:
        line = line.replace("mem[", "")
        line = line.replace("]", "")
        m, i = line.split(" = ")
        mask[curr].append((int(m) , int(i)))

memory = {}
for key in mask:
    for nbr in mask[key]:
        bit = '{0:036b}'.format(nbr[1])
        res = ""
        idxs = []
        for i, b in enumerate(bit):
            if key[i] == "X":
                res += b
            else:
                res += key[i]
        memory[nbr[0]] = int(res, 2)
s = 0
for k in memory:
    s += memory[k]
print(s)