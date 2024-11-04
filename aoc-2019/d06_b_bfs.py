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
#BFS
start = com["YOU"][0]
q = [start]
came_from = {}
came_from[start] = None
while q:
   curr = q.pop(0)
   for next in com[curr]:
      if next not in came_from:
         q.append(next)
         came_from[next] = curr

goal = com["SAN"][0]
curr = goal 
path = []
while curr != start: 
   path.append(curr)
   curr = came_from[curr]
print(len(path))