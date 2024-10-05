file = "input.txt"
lines = [l.strip() for l in open(file).readlines()]

paths = {}

for i in lines:
    l, r = i.split("-")
    if l not in paths:
        paths[l] = [r]
    else:
        paths[l].append(r)

    if r not in paths:
        paths[r] = [l]
    else:
        paths[r].append(l)


q = ["start"]

unique = []

path_count = 0


def dfs(d, count, curr, visited):
    if curr == "end":
        return count + 1
    else:
        if curr.islower():
            visited.append(curr)
        for next in d[curr]:
            if next not in visited:
                count = dfs(d, count, next, visited.copy())
    return count


path_count = dfs(paths, 0, "start", ["start"])
# part 1
print(path_count)
