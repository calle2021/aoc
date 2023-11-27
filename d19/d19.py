import re
import numpy as np
input = "input.txt"
input = "ex0.txt"

pattern = "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
robots = [list(map(int, [r[1], r[2], r[3], r[4], r[5], r[6]])) for r in re.findall(pattern, open(input).read())]

robot = robots[0]
print(robot)
# active : ore, clay, obsidian, geode
# blueprint costs: ore, ore, ore, clay, ore, obsidian
# material, ore, clay, obisian, geode
def dfs(blueprint, active_robots, material, time):
    if time == 0:
        return material[3]

    maxgeodes = material[3] + active_robots[3] * time
    for i, in bp in blueprint:
        wait = 0
        

    return maxgeodes

geods = dfs(robot, np.array([1, 0, 0, 0]), np.array([0, 0, 0, 0]), 24)




