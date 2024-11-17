from aocd.models import Puzzle
from math import ceil
year = 2019
day = 16
puzzle = Puzzle(year=year, day=day)

input_signal = puzzle.input_data

signal = [int(x) for x in input_signal]

patterns = []
base = [0, 1, 0, -1]
curr = [0, 1, 0, -1]
for depth in range(len(signal)):
    new = []
    for c in base:
        new += [c] * (depth + 1)
    curr = new
    patterns.append(curr)

phases = 100
for _ in range(phases):
    new_signal = []
    for depth in range(len(signal)):
        pattern = patterns[depth]
        pattern = pattern * ceil((len(signal) + 1) / len(pattern))
        pattern = pattern[1:len(signal) + 1]
        s = abs(sum([x * y for x, y in zip(signal, pattern)])) % 10
        new_signal.append(s)
    signal = new_signal
print(''.join(map(str, signal[:8])))
