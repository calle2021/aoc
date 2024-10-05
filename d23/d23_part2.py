ex = "389125467"
input = "123487596"

s = [int(i) for i in input]
for i in range(10, 1000001):
    s.append(i)

d = {}
for i in range(1, len(s)):
    d[s[i-1]] = s[i]
d[s[len(s)-1]] = s[0]

mx = 1000000
def move(curr):
    dest = curr - 1
    a = d[curr]
    b = d[a]
    c = d[b]
    while dest == a or dest == b or dest == c or dest == 0:
        if dest < 1:
            dest = mx
        else:
            dest -= 1
    d[curr] = d[c]

    d[c] = d[dest]
    d[b] = c
    d[dest] = a
    return d[curr]

curr = s[0]
moves = 10000000
for _ in range(moves):
    curr = move(curr)

c1 = d[1]
c2 = d[c1]
print(c1 * c2)

