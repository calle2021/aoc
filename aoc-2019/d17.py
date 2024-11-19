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
facings = {ord("^") : -1j, ord("v") : 1j, ord("<") : -1, ord(">") : 1}
scaffolds = set()
empty = set()
o, _, _, _ = intcode(memory.copy())
x = y = 0
for i, v in enumerate(o):
    match v:
        case 10:
            x = 0
            y += 1
            continue
        case 35:
            scaffolds.add(x + y * 1j)
        case 46:
            empty.add(x + y * 1j)
        case _:
            robot = x + y * 1j
            facing = facings[v]
    x += 1
dirs = [1, -1, -1j, 1j]
align = 0
for s in scaffolds:
    if all([s + d in scaffolds for d in dirs]):
        align += s.real * s.imag
print(int(align))

mem = memory.copy()
mem[0] = 2

ymax = max(scaffolds, key=lambda x: x.imag).imag
xmax = max(scaffolds, key=lambda x: x.real).real

rows = []
for y in range(0, int(ymax+1)):
    row = []
    for x in range(0, int(xmax+1)):
        c = x + y * 1j
        if c in scaffolds:
            row.append("#")
        elif c in empty:
            row.append(".")
        elif c == robot:
            print(facing)
            row.append("^")
    rows.append(row)
#rows = rows[::-1]
for r in rows:
    print(''.join(r))

def get_facings(x, f):
    facings = []
    for d in dirs:
        if d == -f:
            continue
        if x + d not in scaffolds: 
            continue
        facings.append(d)
    return facings

seq = []
count = 0
while True:
    count += 1
    facings = get_facings(robot, facing)
    if not facings:
        seq.append(count)
        break
    if facing in facings:
        robot += facing
        continue
    assert len(facings) == 1
    f = facings.pop()
    c = "R" if facing * -1j == f else "L"
    seq.append(count)
    seq.append(c)
    count = 0
    facing = f
    robot += facing

seq.pop(0)
movement = {}
movement["A"] = ["L",4,"L",12,"L",10,"R",12]
movement["B"] = ["R",12,"L",4,"L",12]
movement["C"]  = ["R",12,"R",8,"L",10]
main_routine = ["A","B","B","C","C","A","B","B","C","A"]
que = "L,4,L,12,L,10,R,12,R,12,L,4,L,12,R,12,L,4,L,12,R,12,R,8,L,10,R,12,R,8,L,10,L,4,L,12,L,10,R,12,R,12,L,4,L,12,R,12,L,4,L,12,R,12,R,8,L,10,L,4,L,12,L,10,R,12"
routine = [ord(x) for x in ','.join(main_routine)] + [ord("\n")]

print("here", routine)
for c in "ABC":
    print("lol",[ord(x) for x in ','.join(list(map(str,movement[c])))] + [ord("\n")])
    routine += [ord(x) for x in ','.join(list(map(str,movement[c])))] + [ord("\n")]
routine += [ord("n")]
print(routine)
mem = memory.copy()
mem[0] = 2
o, _, _, _ = intcode(mem, 0, 0, routine, 0)
print(o)