import re
infile = "input.txt"

matches = {}
with open(infile) as f:
    mat, mes = f.read().split("\n\n")
    for line in mat.splitlines():
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
reg_exp = reg_constructor("0")
reg_ = re.compile(reg_exp)

s = 0
for m in messages:
    if reg_.fullmatch(m):
        s += 1
print(s)




