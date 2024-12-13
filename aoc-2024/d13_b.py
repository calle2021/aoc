from aocd import get_data
import re

puzzle = get_data(day=13, year=2024)

machines = []
for line in puzzle.split("\n\n"):
    row = line.split("\n")
    a = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", row[0])[0]
    b = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", row[1])[0]
    p = re.findall(r"Prize: X=(\d+), Y=(\d+)", row[2])[0]
    machines.append([tuple(map(int, a)), tuple(map(int, b)), tuple(map(int, p))])

spend = 0
for machine in machines:
    a, b, p = machine
    a1, a2 = a
    b1, b2 = b
    p1, p2 = p
    p1 += 10000000000000
    p2 += 10000000000000
    x = (p1 * b2 - p2 * b1) / (a1 * b2 - a2 * b1)
    y = (p1 * a2 - p2 * a1) / (b1 * a2 - b2 * a1)
    if x != int(x) or y != int(y):
        continue
    spend += 3 * int(x) + int(y)
print(spend)
