from aocd import get_data

puzzle = get_data(day=19, year=2024)

towels, patterns = puzzle.split("\n\n")
towels = towels.split(", ")
patterns = patterns.split("\n")

def possible(pattern):
    if pattern in cache:
        return cache[pattern]
    if pattern == "":
        return 1
    count = 0
    for towel in towels:
        if pattern[:len(towel)] == towel:
            count += possible(pattern[len(towel):])
    cache[pattern] = count
    return count

count = 0
for x, pattern in enumerate(patterns):
    cache = {}
    count += possible(pattern)
print(count)