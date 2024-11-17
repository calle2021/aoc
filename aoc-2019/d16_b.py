from aocd.models import Puzzle
year = 2019
day = 16
puzzle = Puzzle(year=year, day=day)
signal = puzzle.input_data

offset = int(signal[:7])
signal = [int(x) for x in signal]
signal *= 10000
signal = signal[offset:]
phases = 100
for x in range(phases):
    base_sum = sum(signal)
    part_sum = 0
    for i in range(len(signal)):
        s = base_sum - part_sum
        part_sum += signal[i]
        signal[i] = abs(s) % 10
print(signal[:8])