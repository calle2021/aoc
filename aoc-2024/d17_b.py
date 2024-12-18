def program(a):
    output = []
    while True:
        b = a % 8
        b = b ^ 2
        c = a >> b
        b = b ^ c
        b = b ^ 3
        out = b % 8
        output.append(out)
        a = a >> 3
        if a == 0:
            break
    return output

prog = [2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0]

prog.pop()
i = 1
tail = [0]
for curr in prog[::-1]:
    while True:
        a = i
        b = a % 8
        b = b ^ 2
        c = a >> b
        b = b ^ c
        b = b ^ 3
        out = b % 8
        a = a >> 3
        if out == curr and a != 0 and program(i) == [curr] + tail:
            o = program(i)
            tail.insert(0, curr)
            i = i << 3
            break
        i += 1
print(i >> 3)
