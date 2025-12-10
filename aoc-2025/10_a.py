from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=10).input_data
puzzle = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

data = []
for line in puzzle.splitlines():
    schematics = line.split(" ")
    lights = schematics[0].replace("[", "").replace("]", "")
    lights = [0 if x == "." else 1 for x in lights]
    buttons = [eval(x) for x in schematics[1:-1]]
    data.append((lights, buttons))

def press(curr, presses, buttons, target):
    if curr == target:
        return presses
    if presses >= 10:
        return float("inf")
    fewest = float("inf")

    for button in buttons:
        new = curr
        for i in range(len(curr)):
            if i in button:
                if new[i] == 0:
                    new[i] = 1
                else:
                    new[i] = 0
        print(new)
        exit()
        fewest = min(fewest, press(curr + button, presses + 1, buttons, target))
    return fewest

for d in data:
    state = [0 for _ in range(len(d[0]))]
    few = press(tuple(state), 0, d[1], d[0])