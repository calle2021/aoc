from aocd.models import Puzzle
year = 2019
day = 7
puzzle = Puzzle(year=year, day=day)

ids = {
    1 : [1, 2, 3],
    2 : [1, 2, 3],
    3 : [1],
    4 : [1],
    5 : [1, 2],
    6 : [1, 2],
    7 : [1, 2, 3],
    8 : [1, 2 ,3 ]
}

def intcode(prog, i, input):
    ins = prog[i]
    if ins == 99:
        return input.pop(), i, True
    
    def interpret(ins):
        modes = [0] * 5
        digi = [int(x) for x in str(ins)]
        modes[-len(digi):] = digi
        opcode = modes[-1]
        func = lambda x, y: y if x == 1 else prog[y]
        modes = modes[:-2][::-1]
        params = [func(x, y) for x, y in zip(modes, [i + id for id in ids[opcode]])]
        return opcode, params
    
    while ins != 99:
        opcode, params = interpret(ins)
        match opcode:
            case 1:
                prog[params[2]] = prog[params[0]] + prog[params[1]]
                i += 4
            case 2:
                prog[params[2]] = prog[params[0]] * prog[params[1]]
                i += 4
            case 3:
                prog[params[0]] = input.pop(0)
                i += 2
            case 4:
                i += 2
                return prog[params[0]], i, False
            case 5:
                if prog[params[0]] != 0:
                    i = prog[params[1]]
                else:
                    i += 3
            case 6:
                if prog[params[0]] == 0:
                    i = prog[params[1]]
                else:
                    i += 3
            case 7:
                prog[params[2]] = 1 if prog[params[0]] < prog[params[1]] else 0
                i += 4
            case 8:
                prog[params[2]] = 1 if prog[params[0]] == prog[params[1]] else 0
                i += 4
            case _:
                assert False
        ins = prog[i]

program = list(eval(puzzle.input_data))
phase_settings = [[i, j, k, l, m] for i in range(5,10) for j in range(5,10) for k in range(5,10) for l in range(5,10) for m in range(5,10)]
phase_settings = [x for x in phase_settings if len(set(x)) == 5]

signal = [] 
while phase_settings:
    ps = phase_settings.pop()
    programs = [program] * 5
    idx = [0] * 5
    amp = 0
    j = 0
    for _ in range(5):
        amp, i, done = intcode(programs[j % 5], idx[j % 5], [ps[j % 5], amp])
        idx[j % 5] = i
        j += 1
    while not done:
        amp, i, done = intcode(programs[j % 5], idx[j % 5], [amp])
        idx[j % 5] = i
        j += 1
    signal.append(amp)
print(max(signal))
