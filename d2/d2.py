infile = "input.txt"

data = []
for line in open(infile):
    l = []
    line = line.strip()
    condition, password = line.split(": ")
    times, char = condition.split(" ")
    t1, t2 = times.split("-")
    l.append(password)
    l.append(char)
    l.append(eval(t1))
    l.append(eval(t2))
    data.append(l)


#part 1
valid = 0
for i in data:
    cnt = i[0].count(i[1])
    if i[2] <= cnt <= i[3]:
        valid += 1

print(valid)

#part 2
valid = 0
for i in data:
    s1 = i[0][i[2]-1]
    s2 = i[0][i[3]-1]
    if s1 == i[1] and s2 != i[1]:
        valid += 1
    elif s2 == i[1] and s1 != i[1]:
        valid +=1 
print(valid)