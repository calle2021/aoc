from aocd.models import Puzzle
puzzle = Puzzle(year=2025, day=2).input_data
invalid = 0
for line in puzzle.strip().split(","):
    x, y = line.split("-")
    x = int(x)
    y = int(y)
    for number in range(x, y + 1):
        s = str(number)
        div = len(s) // 2
        divs = []
        while div:
            if len(s) % div == 0:
                divs.append(div)
            div -= 1
        for i, div in enumerate(divs):
            rep = len(s) // div
            seq = [s[i*div:i*div + div] for i in range(rep)]
            if all([x == seq[0] for x in seq]):
                invalid += number
                break
print(invalid)
