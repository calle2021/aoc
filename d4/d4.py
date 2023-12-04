import re
input = "input.txt"

cards = [d.strip() for d in open(input).readlines()]

s = 0
count = []
cs = []
for i, c in enumerate(cards):
    win, mine = c.split(": ")[1].split(" | ")
    win = set(map(int, re.findall("\d+", win)))
    mine = set(map(int, re.findall("\d+", mine)))
    count.append(1)
    both = win & mine
    cs.append(len(both))
    if both: 
        s += 2 ** (len(both) - 1) 

#part 1
print(s)

i = 0
for i in range(len(cs)):
    for _ in range(count[i]):
        for j in range(cs[i]):
            count[i + j + 1] += 1
    i += 1
#part 2
print(sum(count))