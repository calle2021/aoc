infile = "input.txt"

with open(infile) as f:
    f = f.read()
    data = f.splitlines()

gamma = ""
epsilon = ""
for i in range(len(data[0])):
    count = {"1": 0, "0" : 0}
    for d in data:
        count[d[i]] += 1
    if count["1"] > count["0"]:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

#part 1
print(int(gamma, 2) * int(epsilon, 2))

def life_support(data, p1, p2):
    for i in range(len(data[0])):
        count = {"1": 0, "0" : 0}
        for d in data:
            count[d[i]] += 1
        p = ""
        if count["1"] > count["0"] or count["1"] == count["0"]:
            p = p1
        else:
            p = p2
        idx = 0
        while idx < len(data):
            if data[idx][i] == p:
                idx +=1
            else:
                data.pop(idx)
        if len(data) == 1:
            break
    return data[0]
oxygen = life_support(data.copy(), "1", "0")
co2 = life_support(data.copy(), "0", "1")
life_support_raiting = int(oxygen, 2) * int(co2, 2)

#part 2
print(life_support_raiting)
