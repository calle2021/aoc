from aocd.models import Puzzle

year = 2019
day = 1

puzzle = Puzzle(day=day, year=year)
modules = puzzle.input_data

a = sum([eval(x) // 3 - 2 for x in modules.splitlines()])

def fuel_req(x):
    x = x // 3 - 2
    if x <= 0:
        return 0
    return x + fuel_req(x)

b = sum([fuel_req(eval(x)) for x in modules.splitlines()])

puzzle.answer_a = a
puzzle.answer_b = b
