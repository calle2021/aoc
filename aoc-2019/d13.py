from aocd.models import Puzzle
import time
year = 2019
day = 13
puzzle = Puzzle(year=year, day=day)

def intcode(memory, address=0, base=0, input=[], interrupt = 0):
    running = True
    def modes(mem):
        modes = str(mem).zfill(6)
        modes = modes[:-2][::-1]
        return [int(m) for m in modes]
    
    def param(a):
        if mode[a - 1] == 0:
            return memory[address + a]
        if mode[a - 1] == 1:
            return address + a
        if mode[a - 1] == 2:
            return base + memory[address + a]
        assert False

    while True:
        op = memory[address] % 100
        mode = modes(memory[address])
        match op:
            case 1:
                memory[param(3)] = memory[param(1)] + memory[param(2)]
                address += 4
            case 2:
                memory[param(3)] = memory[param(1)] * memory[param(2)]
                address += 4
            case 3:
                memory[param(1)] = input.pop(0)
                address += 2
            case 4:
                input.append(memory[param(1)])
                address += 2
                if interrupt:
                    return input, address, base, running
            case 5:
                if memory[param(1)] != 0:
                    address = memory[param(2)]
                else:
                    address += 3
            case 6:
                if memory[param(1)] == 0:
                    address = memory[param(2)]
                else:
                    address += 3
            case 7:
                memory[param(3)] = 1 if memory[param(1)] < memory[param(2)] else 0
                address += 4
            case 8:
                memory[param(3)] = 1 if memory[param(1)] == memory[param(2)] else 0
                address += 4
            case 9:
                base += memory[param(1)]
                address += 2
            case 99:
                running = False
                break
            case _:
                assert False
    return input, address, base, running

memory = list(eval(puzzle.input_data)) + [0] * 10000
mem = memory.copy()
o, _, _, _ = intcode(mem)
print(o[2::3].count(2))

mem = memory.copy()
mem[0] = 2
score = address = base =  0
ball = (0, 0)
paddle = (0, 0)
inp = [0]
while True:
    for _ in range(3):
        o, address, base, running = intcode(mem, address, base, inp, 1)
    if not running: break
    x, y, z = o[-3:]
    if x == -1 and y == 0:
        score = z
    if z == 3:
        paddle = (x, y)
    if z == 4:
        ball = (x, y)
    joystick = 0
    if ball[0] > paddle[0]:
        joystick = 1
    if ball[0] < paddle[0]:
        joystick = -1
    inp = [joystick]
print(score)
