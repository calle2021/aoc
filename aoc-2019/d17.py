from aocd.models import Puzzle
from collections import defaultdict
year = 2019
day = 17
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


scaffolds = set()
empty = set()
o, _, _, _ = intcode(memory)
curr = (0, 0)
x = y = 0
for i, v in enumerate(o):
    curr = (x, y)
    match v:
        case 10:
            y += 1
            x = 0
            continue
        case 35:
            scaffolds.add(curr)
        case 46:
            empty.add(curr)
        case _:
            robot = curr
            facing = chr(v)
    x += 1
top_left = sorted(scaffolds, key=lambda x: (-x[1], x[0]))[0]
intersections = []
for s in scaffolds:
    if (s[0] + 1, s[1]) in scaffolds and (s[0] + -1, s[1]) in scaffolds and (s[0], s[1] + 1) in scaffolds and (s[0], s[1] - 1) in scaffolds:
        intersections.append(s)
alignment_sum = 0
for i in intersections:
    alignment_sum += i[0] * i[1]

print(alignment_sum)
exit()
ymax = max(scaffolds, key=lambda x: x[1])[1]
xmax = max(scaffolds, key=lambda x: x[0])[0]

for y in range(0, ymax+1):
    for x in range(0, xmax+1):
        c = (x, y)
        if c == top_left:
            print("X", end="")
            continue
        elif c in intersections:
            print("O", end="")
            continue
        elif c in scaffolds:
            print("#", end="")
        elif c in empty:
            print(".", end="")
        elif c == robot:
            print(facing, end="")
    print("")
