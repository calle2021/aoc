from aocd.models import Puzzle
from functools import cache
puzzle = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


#puzzle = Puzzle(year=2025, day=10).input_data

data = []
for line in puzzle.splitlines():
    schematics = line.split(" ")
    lights = schematics[0].replace("[", "").replace("]", "")
    lights = tuple([0 if x == "." else 1 for x in lights])
    buttons = tuple([eval(x) for x in schematics[1:-1]])
    joltage = tuple(eval(schematics[-1].replace("{", "[").replace("}", "]")))
    data.append((joltage, buttons))

@cache
def press(curr, presses, target):
    if curr == target:
        return presses
    if any([x > y for x, y in zip(curr, target)]):
        return float("inf")
    fewest = float("inf")
    for button in buttons:
        new = list(curr)
        if isinstance(button, int):
            new[button] += 1
        else:
            for i in range(len(curr)):
                if i in button:
                    new[i] += 1
        fewest = min(fewest, press(tuple(new), presses + 1, target))
    return fewest

ans = 0
for d in data:
    state = [0 for _ in range(len(d[0]))]
    print(tuple(state), 0, d[1], d[0])
    buttons = d[1]
    few = press(tuple(state), 0, d[0])
    ans += few
    print(few)
print(ans)
