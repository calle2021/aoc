from aocd.models import Puzzle
import operator

year = 2019
day = 2

puzzle = Puzzle(day=day, year=year)
data = puzzle.input_data
opcode = list(eval(data))

def operate(code, noun, verb):
    code[1] = noun
    code[2] = verb
    op = {1: operator.add, 2 : operator.mul}
    i = 0
    while True:
        curr = code[i]
        if curr == 99: break
        val = op[curr](code[code[i+1]], code[code[i+2]])
        pos = code[i+3]
        code[pos] = val
        i += 4
    return code[0]

a = operate(opcode, 12, 2)
puzzle.answer_a = a

inputs = [(x, y) for x in range(100) for y in range(100)]
for noun, verb in inputs:
    opcode = list(eval(data))
    output = operate(opcode, noun, verb)
    if output == 19690720:
        b = 100 * noun + verb
        break
puzzle.answer_b = b

