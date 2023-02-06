ex = "389125467"
input = "123487596"

s = [int(i) for i in ex]
for i in range(10, 101):
    s.append(i)
print(s)

d = {}

for i in range(1, len(s)):
    d[i-1] = s[i]
d[len(s)] = s[0]
print(d)

#1000000 and 10 000 000 iterations

curr = 0
def move(curr):
    a = d[curr]
    b = d[curr+1]
    c = d[curr+2]



for _ in range(1):
    prev = move(curr)


