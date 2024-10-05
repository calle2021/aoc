ex = "389125467"
input = "123487596"

s = [int(i) for i in input]

d = {}
for i in range(1, len(s)):
    d[s[i-1]] = s[i]
d[s[len(s)-1]] = s[0]

def move(curr):
    dest = curr - 1
    a = d[curr]
    b = d[a]
    c = d[b]
    while dest == a or dest == b or dest == c or dest == 0:
        if dest < 1:
            dest = 9
        else:
            dest -= 1
    d[curr] = d[c]
    d[c] = d[dest]
    d[b] = c
    d[dest] = a
    return d[curr]

curr = s[0]
moves = 100
for _ in range(moves):
    curr = move(curr)

curr = d[1]
output = ""
for i in range(len(d)-1):
    output += str(curr)
    curr = d[curr]
print(output)
