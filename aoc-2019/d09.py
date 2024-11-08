from aocd.models import Puzzle
year = 2019
day = 9
puzzle = Puzzle(year=year, day=day)

ids = {
    1 : [1, 2, 3],
    2 : [1, 2, 3],
    3 : [1],
    4 : [1],
    5 : [1, 2],
    6 : [1, 2],
    7 : [1, 2, 3],
    8 : [1, 2 ,3],
    9 : [1]
}

def intcode(prog, i=0, input=[0]):
    ins = prog[i]

    base = 0
    if ins == 99:
        return input.pop(), i, True
    
    def interpret(ins):
        modes = [0] * 5
        digi = [int(x) for x in str(ins)]
        modes[-len(digi):] = digi
        opcode = modes[-1]
        
        modes = modes[:-2][::-1]
        params = []
        for x, y in zip(modes, [i + id for id in ids[opcode]]):
            match x:
                case 0:
                    p = prog[y]
                case 1:
                    p = y
                case 2:
                    p = base + prog[y]
                case __:
                    assert False
            params.append(p)

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
                input.append(prog[params[0]])
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
            case 9:
                base += prog[params[0]]
                i += 2
            case _:
                assert False
        ins = prog[i]
    print(input)
program = list(eval(puzzle.input_data))
program = program + [0] * 10000
intcode(program, i=0, input = [2])