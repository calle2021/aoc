from aocd import get_data
import re
puzzle = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
puzzle = get_data(day=17, year=2024)
prog = list(map(int, re.findall(r"(\d+)", puzzle)))
a = prog.pop(0)
b = prog.pop(0)
c = prog.pop(0)

def combo(x, a, b, c):
    if x in [0, 1, 2, 3]:
        return x
    if x == 4:
        return a
    if x == 5:
        return b
    if x == 6:
        return c
    if x == 7:
        assert False
initial = (b, c, tuple(prog))
i = 0
while True:
    if i % 100000 == 0:
        print(i)
    a = i
    b = initial[0]
    c = initial[1]
    prog = list(initial[2])
    pointer = 0
    output = []
    unique = set()
    while pointer < len(prog):
        opcode = prog[pointer]
        operand = prog[pointer + 1]
        if opcode in [0, 2, 5, 6, 7]:
            operand = combo(operand, a, b, c)
        unique.add(opcode)
        match (opcode):
            case 0:
                a = int(a / 2 ** operand)
                pointer += 2
            case 1:
                b = b ^ operand
                pointer += 2
            case 2:
                b = operand % 8
                pointer += 2
            case 3:
                if a == 0:
                    pointer += 2
                else:
                    pointer = operand
            case 4:
                b = b ^ c
                pointer += 2
            case 5:
                output.append(operand % 8)
                pointer += 2
            case 6:
                b = int(a / 2 ** operand)
                pointer += 2
            case 7:
                c = int(a / 2 ** operand)
                pointer += 2
    state = (b, c, tuple(output))
    if state == initial:
        print(i)
        break
    i += 1