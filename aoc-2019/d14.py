from aocd.models import Puzzle
year = 2019
day = 14
puzzle = Puzzle(year=year, day=day).examples[0].input_data
#puzzle = Puzzle(year=year, day=day).input_data
RECIPES = {}
MATERIAL = {}
for r in puzzle.strip().splitlines():
    material, chemical = r.split("=>")
    chemical = chemical.split(" ")[-2:]
    material = material.strip().replace(" ", "-").replace(",", "").split("-")
    RECIPES[chemical[1]] = material[1::2]
    MATERIAL[chemical[1]] = [int(chemical[0])] + [int(m) for m in material[::2]]
print(RECIPES)
print(MATERIAL)

print(MATERIAL["A"])

def rec(c):
    if "ORE" in RECIPES[c]:
        return MATERIAL[c][1]