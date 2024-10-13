from aoc_utility import run_examples
from aocd.models import Puzzle

year = 2019
day = 3
puzzle = Puzzle(day=day, year=year)

d = {"R" : (1, 0), "L" : (-1, 0), "U" : (0, 1), "D" : (0, -1)}

def walk(path, curr):
    p = []
    visited = {}
    step_count = 0
    for dest in path.split(","):
        h = d[dest[0]]
        steps = eval(dest[1:])
        for _ in range(steps):
            loc = (curr[0] + h[0], curr[1] + h[1])
            step_count += 1
            if loc not in visited:
                visited[loc] = step_count
            p.append(loc)
            curr = loc
    return p, visited

def solve_a(data):
    path_a, path_b = data.split("\n")
    p_a, _ = walk(path_a, (0, 0))
    p_b, _ = walk(path_b, (0, 0))
    intersections = set(p_a) & set(p_b)
    a = min([abs(x) + abs(y) for x, y in intersections])
    return a

def solve_b(data):
    path_a, path_b = data.split("\n")
    p_a, v_a = walk(path_a, (0, 0))
    p_b, v_b  = walk(path_b, (0, 0))
    intersections = set(p_a) & set(p_b)
    b = min([v_a[i] + v_b[i] for i in intersections])
    return b

assert(run_examples(solver=solve_a, puzzle=puzzle, part="a"))
a = solve_a(puzzle.input_data)
puzzle.answer_a = a

assert(run_examples(solver=solve_b, puzzle=puzzle, part="b"))
b = solve_b(puzzle.input_data)
puzzle.answer_b = b

