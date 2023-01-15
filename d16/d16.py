from collections import deque

infile = "input.txt"

found_my_ticket = False
found_nearby_ticket = False
valid_nbrs = set()
fields = {}
my_ticket = []
nearby_tickets = []

for line in open(infile):
    if "your ticket" in line:
        found_my_ticket = True
    elif "nearby tickets" in line:
        found_nearby_ticket = True
    elif not found_my_ticket and not found_nearby_ticket and line != "\n":
        field, line = line.split(": ")
        field = field.replace(" ", "")
        fields[field] = []
        l, r = line.split(" or ")
        l = l.split("-")
        r = r.split("-")
        for n in range(int(l[0]), int(l[1]) + 1):
            valid_nbrs.add(n) 
            fields[field].append(n)
        for n in range(int(r[0]), int(r[1]) + 1):
            valid_nbrs.add(n) 
            fields[field].append(n)
    elif found_my_ticket and not found_nearby_ticket and line != "\n":
        my_ticket  = list(eval(line))
    elif found_nearby_ticket and line != "\n":
        nearby_tickets.append(list(eval(line)))
s1 = 0
nearby = []
for ticket in nearby_tickets:
    valid = True
    for n in ticket:
        if n not in valid_nbrs:
            s1 += n
            valid = False
    if valid:
        nearby.append(ticket)
print(s1) # part 1

def get_index(lst, n):
    return [itm[n] for itm in lst]

d ={}
q = deque([])
idx = deque([])
for i in range(0, len(nearby[0])):
    q.append(tuple(get_index(nearby, i)))
    idx.append(i)

while q:
    curr = q.popleft()
    i = idx.popleft()
    keys = []
    for key in fields:
        if all( item in fields[key] for item in curr):
            keys.append(key)
    if len(keys) == 1:
        d[keys[0]] = i
        del fields[keys[0]]
    else:
        q.append(curr)
        idx.append(i)

s2 = 1
for key in d:
    if "departure" in key:
        i = d[key]
        s2 *= my_ticket[i]
print(s2)