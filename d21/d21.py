from collections import deque
infile = "input.txt"

data = {}
all_ingredients = []
for line in open(infile):
    line = line.strip()
    ingredients, allergens = line.split(" (contains ")
    allergens = allergens.replace(")", "")
    allergens = allergens.replace(",", "")
    allergens = allergens.split(" ")
    ingredients = ingredients.split(" ")
    for i in ingredients:
        all_ingredients.append(i)     
    for al in allergens:
        if al in data:
            data[al].append(ingredients)
        else:
            data[al] = []
            data[al].append(ingredients)

#part 1        
map = {}
for d in data:
    count = {}
    dishes = data[d]
    for i in dishes:
        for j in i:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
    for c in count:
        if count[c] ==  len(dishes):
            map[c] = d
    for k in data:
        for l in data[k]:
            for m in map:
                if m in l:
                    l.remove(m)

for m in map:
    if m in all_ingredients:
        all_ingredients = list(filter(lambda a: a != m, all_ingredients))
print(len(all_ingredients))
