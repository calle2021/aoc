from aocd.models import Puzzle
from heapq import *
year = 2019
day = 15
puzzle = Puzzle(year=year, day=day)

def intcode(memory, address=0, base=0, input=[], interrupt = 0):
    running = True
    def modes(mem):
        modes = str(mem).zfill(6)
        modes = modes[:-2][::-1]
        return [int(m) for m in modes]
    
    def param(a):
        if mode[a - 1] == 0:
            return memory[address + a]
        if mode[a - 1] == 1:
            return address + a
        if mode[a - 1] == 2:
            return base + memory[address + a]
        assert False

    while True:
        op = memory[address] % 100
        mode = modes(memory[address])
        match op:
            case 1:
                memory[param(3)] = memory[param(1)] + memory[param(2)]
                address += 4
            case 2:
                memory[param(3)] = memory[param(1)] * memory[param(2)]
                address += 4
            case 3:
                memory[param(1)] = input.pop(0)
                address += 2
            case 4:
                input.append(memory[param(1)])
                address += 2
                if interrupt:
                    return input, address, base, running
            case 5:
                if memory[param(1)] != 0:
                    address = memory[param(2)]
                else:
                    address += 3
            case 6:
                if memory[param(1)] == 0:
                    address = memory[param(2)]
                else:
                    address += 3
            case 7:
                memory[param(3)] = 1 if memory[param(1)] < memory[param(2)] else 0
                address += 4
            case 8:
                memory[param(3)] = 1 if memory[param(1)] == memory[param(2)] else 0
                address += 4
            case 9:
                base += memory[param(1)]
                address += 2
            case 99:
                running = False
                break
            case _:
                assert False
    return input, address, base, running

memory = list(eval(puzzle.input_data)) + [0] * 10000

def simulate(mem, seq):
    address = base = 0
    for s in seq:
        o, address, base, running = intcode(mem, address, base, [s], 1)
    return o

dirs = {1 : (0, 1), 2 : (0, -1), 3 : (-1, 0), 4 : (1, 0)}

grid = {}
goal = (0, 0)
def explore(curr, o, seq):
    if o == 0 or curr in grid:
        return
    grid[curr] = o
    if o == 2:
        goal = curr
    for dir in [1, 2, 3, 4]:
        o = simulate(memory.copy(), seq + [dir])
        pos = (curr[0] + dirs[dir][0], curr[1] + dirs[dir][1])
        explore(pos, o.pop(), seq + [dir])

explore((0, 0), 1, [])
goal = next((k for k, v in grid.items() if v == 2), None)
assert goal

q = []
start = (0, 0)
heappush(q, (0, start))
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0
while q:
    curr = heappop(q)
    if curr == goal:
        break
    neighbours = []
    for dir in dirs.values():
        pos = (curr[1][0] + dir[0], curr[1][1] + dir[1])
        if pos not in grid: 
            continue
        neighbours.append(pos)
    for next in neighbours:
        new_cost = cost_so_far[curr[1]] + 1
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            heappush(q, (priority, next))
            came_from[next] = curr
print(cost_so_far[goal])

q = [goal]
distances = {goal: 0}
while q:
    curr = q.pop(0)
    neighbours = []
    for d in dirs.values():
        pos = (curr[0] + d[0], curr[1] + d[1])
        if pos not in grid: 
            continue
        neighbours.append(pos)
    for next in neighbours:
        if next not in distances:
            q.append(next)
            distances[next] = distances[curr] + 1
print(max(distances.values()))