from aocd import get_data

puzzle = get_data(day=22, year=2024)

numbers = list(map(int, puzzle.split("\n")))
for _ in range(2000):
    for i, n in enumerate(numbers):
        numbers[i] = ((numbers[i] ^ numbers[i] * 64)) % 16777216
        numbers[i] = ((numbers[i] ^ numbers[i] // 32)) % 16777216
        numbers[i] = ((numbers[i] ^ numbers[i] * 2048)) % 16777216
print(sum(numbers))