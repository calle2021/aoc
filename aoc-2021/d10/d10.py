file = "input.txt"

lines = [l.strip() for l in open(file).readlines()]

open = {")": "(", "]": "[", "}": "{", ">": "<"}
close = {"(": ")", "[": "]", "{": "}", "<": ">"}
point_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
bracket_points = {")": 1, "]": 2, "}": 3, ">": 4}


syntax_error_score = 0
scores = []
for i, l in enumerate(lines):
    stack = []
    corrupt = False
    for c in l:
        if c in open.values():
            stack.append(c)
        else:
            if len(stack) == 0:
                syntax_error_score += point_table[c]
                corrupt = True
                break
            if stack.pop() != open[c]:
                syntax_error_score += point_table[c]
                corrupt = True
                break
    complete_line = []
    if not corrupt:
        for s in stack:
            complete_line.insert(0, close[s])
        s = 0
        for c in complete_line:
            s = s * 5 + bracket_points[c]
        scores.append(s)


# part 1
print(syntax_error_score)

scores.sort()
# part 2
print(scores[int((len(scores) - 1) / 2)])
