from aocd.models import Puzzle
from functools import cache
import re
from heapq import *
puzzle = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


puzzle = Puzzle(year=2025, day=10).input_data

manual = []
for instruction in puzzle.splitlines():
    instruction = instruction.split(" ")
    buttons = [eval(x) for x in instruction[1:-1]]
    joltage = tuple(map(int, re.findall(r"\d+", instruction[-1])))
    manual.append([buttons, joltage])

def heuristic(next, goal):
    return sum([abs(x - y) for x, y in zip(next, goal)])

def astar(buttons, goal):
    q = []
    start = tuple([0 for _ in joltage])
    heappush(q, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while q:
        cost, curr = heappop(q)
        if curr == goal:
            break
        neighbours = []
        for button in buttons:
            n = list(curr)
            if isinstance(button, int):
                n[button] += 1
            else:
                for b in button:
                    n[b] += 1
            neighbours.append(tuple(n))
        for next in neighbours:
            new_cost = cost_so_far[curr] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                heappush(q, (priority, next))
                came_from[next] = curr
    return cost_so_far[curr]

fewest = 0
for buttons, joltage in manual:
    few = astar(buttons, joltage)
    fewest += few
    print(few)

print(fewest)
