from aocd import get_data

puzzle = """029A"""
#puzzle = get_data(day=21, year=2024)

numpad = {7 : (0, 0), 8 : (1, 0), 9 : (2, 0), 4 : (0, 1), 5 : (1, 1), 6 : (2, 1), 1 : (0, 2), 2 : (1, 2), 3 : (2, 2), 0 : (1, 3), "A" : (2, 3)}
numgrid = {v : k for k, v in numpad.items()}

dirpad = {(1, 0) : (2, 1), (-1, 0) : (0, 1), (0, -1) : (1, 0), (0, 1) : (1, 1), "A" : (2, 0)}
dirgrid = {v : k for k, v in dirpad.items()}



codes = puzzle.split("\n")



dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


for code in puzzle.split("\n"):
    code = [int(x) if x.isdigit() else x for x in code]
    start = numpad["A"]
    break