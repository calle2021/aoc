from aocd import get_data

puzzle = get_data(day=19, year=2024)

towels, patterns = puzzle.split("\n\n")
towels = towels.split(", ")
patterns = patterns.split("\n")

def possible(pattern):
    if pattern == "":
        return True
    for towel in towels:
        if pattern[:len(towel)] == towel:
            if possible(pattern[len(towel):]):
                return True
    return False

count = 0
for pattern in patterns:
    if possible(pattern):
        count += 1
print(count)