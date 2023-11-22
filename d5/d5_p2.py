
import re
input = "input.txt"

with open(input) as f:
    st, seq = f.read().split("\n\n")

r = [1, 5, 9, 13, 17, 21, 25, 29, 33]
stack = [[] for s in range(9)]
for s in st.split("\n")[:-1]:
    for i, r_ in enumerate(r):
        letter = s[r_]
        if letter == " ": continue
        stack[i].append(letter)
PATTERN = r'\b\d+\b'
for s in seq.strip().split("\n"):
    amount, source, dest = list(map(int, list(re.findall(PATTERN, s))))
    stack[dest - 1] = stack[source - 1][:amount] + stack[dest - 1]
    del stack[source - 1][:amount]
    
STRING = ""
for s in stack:
    STRING += s[0]
#part 2
print(STRING)