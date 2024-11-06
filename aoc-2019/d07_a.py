from aocd.models import Puzzle
year = 2019
day = 7
puzzle = Puzzle(year=year, day=day)

def intcode(prog, input):
    i = 0
    output = []
    ins = prog[i]
    def interpret(ins):
        modes = [0] * 5
        digi = [int(x) for x in str(ins)]
        modes[-len(digi):] = digi
        opcode = modes[-1]
        func = lambda x, y: y if x == 1 else prog[y]
        modes = modes[:-2][::-1]
        params = [func(x, y) for x, y in zip(modes, [i+1, i+2, i+3])]
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
                output.append(prog[params[0]])
                i += 2
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
    return output[0]

program = list(eval(puzzle.input_data))
phase_settings = [[i, j, k, l, m] for i in range(5) for j in range(5) for k in range(5) for l in range(5) for m in range(5)]
phase_settings = [x for x in phase_settings if len(set(x)) == 5]
signal = []
for phase in phase_settings:
    amp = intcode(program[:], [phase[0], 0])
    amp = intcode(program[:], [phase[1], amp])
    amp = intcode(program[:], [phase[2], amp])
    amp = intcode(program[:], [phase[3], amp])
    amp = intcode(program[:], [phase[4], amp])
    signal.append(amp)
print(max(signal))
