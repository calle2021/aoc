class colors:
    SUCCESS = '\033[92m'
    FAIL = '\033[91m'

def run_examples(solver, puzzle, part):
    status = True
    for i, example in enumerate(puzzle.examples):
        ans = solver(example.input_data)
        example_ans = example.answer_a if part == "a" else example.answer_b
        if ans == eval(example_ans):
            print(f"{colors.SUCCESS}example {i} succeeded\nexample answer {example.answer_a}\nyour answer {ans}\n") 
            continue
        status = False
        print(f"{colors.FAIL}example {i} failed\nexample answer {example.answer_a}\nyour answer {ans}\n")
    return status

"""
from aoc_utility import run_examples
from aocd.models import Puzzle

year = 2019
day = day
puzzle = Puzzle(day=day, year=year)

def solve_a(data):
    return a

def solve_b(data):
    return b
    
assert(run_examples(solver=solve_a, puzzle=puzzle, part="a"))
a = solve_a(puzzle.input_data)
puzzle.answer_a = a
assert(run_examples(solver=solve_b, puzzle=puzzle, part="b"))
b = solve_b(puzzle.input_data)
puzzle.answer_b = b


"""