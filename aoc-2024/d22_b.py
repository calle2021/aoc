from aocd import get_data
from collections import defaultdict

puzzle = get_data(day=22, year=2024)

numbers = list(map(int, puzzle.split("\n")))
sequances = [{} for _ in range(len(numbers)) ]
window = [[] for _ in range(len(numbers)) ]
for j in range(2000):
    for i, n in enumerate(numbers):
        numbers[i] = (numbers[i] ^ (numbers[i] * 64)) % 16777216
        numbers[i] = (numbers[i] ^ (numbers[i] // 32)) % 16777216
        numbers[i] = (numbers[i] ^ (numbers[i] * 2048)) % 16777216
        digit = numbers[i] % 10
        change = digit - n % 10
        window[i].append(change)
        if len(window[i]) < 4:
            continue
        if len(window[i]) == 5:
            window[i].pop(0)
        w = tuple(window[i])
        if w in sequances[i]:
            continue
        sequances[i][w] = digit

combined = defaultdict(int)
for seq in sequances:
    for k, v in seq.items():
        combined[k] += v
print(max(combined.values()))