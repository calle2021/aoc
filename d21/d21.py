infile = "input.txt"

data = {}
all_ingredients = []
for line in open(infile):
    line = line.strip()
    ingredients, allergens = line.split(" (contains ")
    allergens = allergens.strip(")").split(", ")
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
l = 0
for m in assigned.values():
    l += all_ingredients.count(m)
print(len(all_ingredients) - l)

#part 2
res = ""
a = sorted(assigned.keys())
res = ','.join([assigned[i] for i in a])
print(res)

