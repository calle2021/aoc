file = "input.txt"

map = {}
pair_counter = {}
char_counter = {}
default = {}
with open(file) as f:
    f = f.read()
    start, maps = f.split("\n\n")
    for m in maps.split("\n"):
        l, r = m.split(" -> ")
        map[l] = r
        pair_counter[l] = 0
        char_counter[r] = 0
        default[l] = 0

for i in range(len(start) - 1):
    s = start[i] + start[i + 1]
    pair_counter[s] += 1
for c in start:
    char_counter[c] += 1


def pair_insertion(default, pair_counter, char_counter, steps):
    for _ in range(steps):
        t = default.copy()

        for x in pair_counter:
            if x in t:
                t[x[0] + map[x]] += pair_counter[x]
                t[map[x] + x[1]] += pair_counter[x]
                char_counter[map[x]] += pair_counter[x]
            else:
                t[x[0] + map[x]] = pair_counter[x]
                t[map[x] + x[1]] = pair_counter[x]
                char_counter[map[x]] += pair_counter[x]
        for key in pair_counter:
            if key in t:
                pair_counter[key] = t[key]
            else:
                pair_counter[key] = 0

    min_count = float("inf")
    max_count = 0
    for c in char_counter:
        min_count = min(min_count, char_counter[c])
        max_count = max(max_count, char_counter[c])
    return max_count - min_count


# part 1
print(pair_insertion(default.copy(), pair_counter.copy(), char_counter.copy(), 10))
# part 2
print(pair_insertion(default.copy(), pair_counter.copy(), char_counter.copy(), 40))
