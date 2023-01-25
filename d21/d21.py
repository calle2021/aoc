infile = "input.txt"

data = {}
all_ingredients = []
for line in open(infile):
    line = line.strip()
    ingredients, allergens = line.split(" (contains ")
    allergens = allergens.replace(")", "")
    allergens = allergens.replace(",", "")
    allergens = allergens.split(" ")
    ingredients = set(ingredients.split(" "))
    for i in ingredients:
        all_ingredients.append(i)     
    for al in allergens:
        if al in data:
            data[al].append(ingredients)
        else:
            data[al] = []
            data[al].append(ingredients)
map = {}
for key in data:
    recipies = data[key]
    s = set.intersection(*recipies)
    map[key] = s

assigned = {}
while map:
    for k, v in map.items():
        if len(v) == 1:
            val, = v
            assigned[k] = val
            del map[k]
            for vals in map.values():
                vals.discard(val)
            break

#part 1
for m in assigned.values():
    if m in all_ingredients:
        all_ingredients = list(filter(lambda a: a != m, all_ingredients))
print(len(all_ingredients))

#part 2
res = ""
a = sorted(assigned.keys())
res = ','.join([assigned[i] for i in a])
print(res)

