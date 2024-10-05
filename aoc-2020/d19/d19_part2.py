import re
infile = "input.txt"

matches = {}
with open(infile) as f:
    mat, mes = f.read().split("\n\n")
    for line in mat.splitlines():
        print(line)
        rule, m = line.split(": ")
        matches[rule] = m 
    messages = mes.splitlines()

def reg_constructor(key):
    match_ = matches[key]
    if match_[0] == '"':
        return match_[1]
    conditions = match_.split()
    inner_condition = ""  
    for i in conditions:
        if "|" in i:
            inner_condition += "|"
            continue    
        inner_condition += reg_constructor(i)
    return f'({inner_condition})'


reg_exp_1 = reg_constructor("42")
reg_1 = re.compile(reg_exp_1)
reg_exp_2 = reg_constructor("31")
reg_2 = re.compile(reg_exp_2)

s = 0
for m in messages:
    pos = 0
    count_1 = 0
    match = reg_1.match(m, pos)
    while match:
        count_1 += 1
        pos = match.end()
        match = reg_1.match(m, pos)
    
    count_2 = 0
    match = reg_2.match(m, pos)
    while match:
        count_2 += 1
        pos = match.end()
        match = reg_2.match(m, pos)

    if pos == len(m) and 0 < count_2 < count_1:
        s += 1
print(s)




