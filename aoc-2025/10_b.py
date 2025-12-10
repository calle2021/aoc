from aocd.models import Puzzle
from functools import cache
import re
puzzle = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


#puzzle = Puzzle(year=2025, day=10).input_data

manual = []
for instruction in puzzle.splitlines():
    instruction = instruction.split(" ")
    buttons = [eval(x) for x in instruction[1:-1]]
    joltage = tuple(map(int, re.findall(r"\d+", instruction[-1])))
    manual.append([buttons, joltage])

@cache
def press(curr, presses):
    if curr == joltage:
        return presses
    if any([x > y for x, y in zip(curr, joltage)]):
        return float("inf")
    fewest = float("inf")
    for button in buttons:
        next = list(curr)
        if isinstance(button, int):
            next[button] += 1
        else:
            for b in button:
                next[b] += 1
        fewest = min(fewest, press(tuple(next), presses + 1))
    return fewest

fewest = 0
for buttons, joltage in manual:
    curr = tuple([0 for _ in joltage])
    few = press(curr, 0)
    fewest += few
    print(few)

print(fewest)
