input = "input.txt"

data = [d.strip() for d in open(input).readlines()]
idx = {"red" : 0, "green" : 1, "blue" : 2}
games = []
for i, d in enumerate(data):
    d = d.split(": ")[1]
    subset = d.split("; ")
    colors = []
    for sub in subset:
        color = [0, 0, 0]
        s = sub.split(", ")
        for set in s:
            val, col = set.split(" ")
            color[idx[col]] += int(val)
        colors.append(color)
    games.append(colors)

possible = 0
CONDITIONS = [12, 13, 14]
for i, subset in enumerate(games):
    for s in subset:
        if s[0] > CONDITIONS[0] or s[1] > CONDITIONS[1] or s[2] > CONDITIONS[2]:
            break
    else:
        possible += (i + 1)
#part 1
print(possible)
powers = 0
for i, subset in enumerate(games):
    r = -float("inf")
    g = -float("inf")
    b = -float("inf")
    for s in subset:
        r = max(r, s[0])
        g = max(g, s[1])
        b = max(b, s[2])
    powers += (r * g * b)
#part 2
print(powers)
