import numpy as np
from aocd import get_data, submit

year = 2019
day = 1

def parse_data(data):
    return data

def solve_a(data):
    return sum([eval(x) // 3 - 2 for x in data.splitlines()])

def solve_b(data):
    def fuel_req(x):
        x = x // 3 - 2
        if x <= 0:
            return 0
        return x + fuel_req(x)
    return sum([fuel_req(eval(x)) for x in data.splitlines()])

data = parse_data(get_data(day=day, year=year))

ans_a = solve_a(data)
ans_b = solve_b(data)
submit(ans_a, part="a", day=day, year=year)
submit(ans_b, part="b", day=day, year=year)