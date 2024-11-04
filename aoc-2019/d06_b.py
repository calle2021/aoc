from heapq import *
from aocd.models import Puzzle
year = 2019
day = 6
puzzle = Puzzle(year=year, day=day).input_data

com = {}
for node in puzzle.strip().split("\n"):
   x, y  = node.split(")")
   if x not in com:
      com[x] = [y]
   else:
      com[x].append(y)
   
   if y not in com:
      com[y] = [x]
   else:
      com[y].append(x)
      
#Djikstra
front = []
start = com["YOU"][0]
goal = com["SAN"][0]
heappush(front, (0, start))
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0
while front:
    curr = heappop(front)
    if curr == goal:
        break
    for next in com[curr[1]]:
        new_cost = cost_so_far[curr[1]] + 1
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            heappush(front, (priority, next))
            came_from[next] = curr
print(cost_so_far[goal])