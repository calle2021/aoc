from aocd.models import Puzzle
from scipy.optimize import LinearConstraint
from scipy.optimize import milp
import numpy as np
import re
puzzle = Puzzle(year=2025, day=10).input_data
manual = []
for instruction in puzzle.splitlines():
    instruction = instruction.split(" ")
    buttons = [[eval(x)] if isinstance(eval(x), int) else list(eval(x)) for x in instruction[1:-1]]
    joltage = [int(x) for x in re.findall(r"\d+", instruction[-1])]
    manual.append([buttons, joltage])

presses = 0
for buttons, joltage in manual:
    nrows = len(joltage)
    ncols = len(buttons)
    M = np.column_stack([np.array([1 if x in button else 0 for x in range(nrows)]) for button in buttons])
    c_lo = c_hi = np.array(joltage)
    cons = LinearConstraint(M, c_lo, c_hi)
    coeffs = np.ones(ncols)
    integrality = np.ones_like(coeffs)
    solution = milp(c = coeffs, constraints = cons, integrality = integrality)
    presses += sum([int(round(x)) for x in solution.x])
print(presses)