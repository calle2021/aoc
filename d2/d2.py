input = "input.txt"

rounds = [r.strip() for r in open(input).readlines()]
score_map = {"X" : 1, "Y": 2, "Z" : 3}
strategy = {"A" : {"X" : 3, "Y" : 6, "Z" : 0},
    "B" : {"X" : 0, "Y" : 3, "Z" : 6},
    "C" : {"X" : 6, "Y" : 0, "Z" : 3}}
score = 0
for r in rounds:
    op, me = r.split(" ")
    score += strategy[op][me] + score_map[me]
#part 1
print(score)

points = {"X" : 0 , "Y" : 3, "Z" : 6}
instructions = {"X" : {"A" : "Z", "B" : "X", "C" : "Y"},
    "Y" : {"A" : "X", "B" : "Y", "C" : "Z"},
    "Z" : {"A" : "Y", "B" : "Z", "C" : "X"}}

score = 0
for r in rounds:
    op, me = r.split(" ")
    score += points[me] + score_map[instructions[me][op]] 
#part 2
print(score)

