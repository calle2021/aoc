from aocd.models import Puzzle
year = 2019
day = 5
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
                prog[params[0]] = input
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
    print(output)

program = list(eval(puzzle.input_data))
intcode(program[:], 1)
intcode(program[:], 5)
