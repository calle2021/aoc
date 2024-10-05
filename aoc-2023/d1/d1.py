import re
input = "input.txt"

data = [d.strip() for d in open(input).readlines()]
s  = 0
for d in data:
    numbers = list(re.findall(r"\d", d))
    n = numbers[0] + numbers[-1]
    s += int(n)
#part 1
print(s)

s = 0
pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
m = {"one": "1", "two" : "2", "three": "3" , "four" : "4", "five": "5", "six" : "6", "seven": "7", "eight" : "8", "nine": "9"}
for d in data:
    numbers = list(re.findall(pattern, d))
    a = numbers[0]
    b = numbers[-1]
    if not a.isdigit():
        a = m[a]
    if not b.isdigit():
        b = m[b]

    s += int(a + b)
#part 2
print(s)

