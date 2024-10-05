input = "input.txt"

elves = set()
empty = set()
for y, line in enumerate(open(input).readlines()):
    for x, e in enumerate(line):
        if e == "#":
            elves.add(x + y * 1j)
        if e == ".":
            empty.add((x, y * 1j))

dirs  = [[-1j, 1 - 1j, -1 - 1j], [1j, 1 + 1j, -1 + 1j], [-1, -1 + 1j, -1 - 1j], [1, 1 - 1j, 1 + 1j]]
dest = [-1j, 1j, -1, 1]
adjacent = [1, -1, 1j, -1j, -1 - 1j, 1 - 1j, -1 + 1j, 1 + 1j]

i = 0
round = 1
while True:
    proposed = []
    previous = []
    stationary = set()
    for e in elves:
        if len({a + e for a in adjacent} & elves) == 0:
            stationary.add(e)
            continue
        for i_ in range(4):
            d = dirs[(i + i_) % 4]
            if len({d_ + e for d_ in d} & elves) == 0:
                proposed.append(e + dest[(i + i_) % 4])
                previous.append(e)             
                break
        else:
            stationary.add(e)
    new_positions = set()
    dont_move = set()
    while proposed:
        p = proposed.pop()
        prev = previous.pop()
        if p not in proposed and p not in dont_move:
            new_positions.add(p)
            continue
        stationary.add(prev)
        dont_move.add(p)
    if len(stationary) == len(elves):
        break
    elves = stationary | new_positions
    i = (i + 1) % 4
    round += 1
print(round)