import re
from typing import Match
infile = "input.txt"

PATTERN = re.compile(r'\(([^()]+)\)')
ADDITION = re.compile(r'(\d+) \+ (\d+)')

def add_sub(m):
    return str(int(m[1]) + int(m[2]))

def par_sub(m):
    return str(compute(m[1]))
    
def compute(line):
    while ADDITION.search(line):
        line = ADDITION.sub(add_sub, line)
    nbrs = line.split()
    val = int(nbrs[0])
    i = 1
    while i < len(nbrs):
        op = nbrs[i]
        n = nbrs[i+1]
        if op == "+":
            val += int(n)
        elif op == "*":
            val *= int(n)
        i += 2
    return val

data = []
for line in open(infile):
    line = line.strip()
    while PATTERN.search(line):
        line = PATTERN.sub(par_sub, line)
    line = compute(line)
    data.append(line)
s = 0
for d in data:
    s += int(d)
print(s)
