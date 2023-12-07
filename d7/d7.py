import re
from functools import cmp_to_key
input = "input.txt"

hands = [d.strip() for d in open(input).readlines()]

strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def hand_type(h):
    u = set(h)
    counts = []
    for u_ in u:
        counts.append(h.count(u_))

    if 5 in counts:
        return 7
    if 4 in counts:
        return 6
    if 3 in counts and 2 in counts:
        return 5
    if 3 in counts:
        return 4
    if counts.count(2) == 2:
        return 3
    if 2 in counts:
        return 2
    
    if len(u) == len(h):
        return 1
    
    print("SHOULD NOT BE HERE")
    return 0





def compare_hands(h1, h2):
    c1 = h1.split(" ")[0]
    c2 = h2.split(" ")[0]
    t1 = hand_type(c1)
    t2 = hand_type(c2)

    if t1 > t2:
        return 1
    elif t2 > t1:
        return -1
    # are equal if reach here

    for i in range(len(c1)):
        if h1[i] == h2[i]:
            continue
        # we have found best
        if strength.index(h1[i]) < strength.index(h2[i]):
            return 1
        else:
            return -1
    else:
        # if not distinction return 0
        return 0

hands.sort(key = cmp_to_key(compare_hands))
#print(hands)
s = 0
for i, h in enumerate(hands):
    x = int(h.split(" ")[1])
    s += (i + 1) * x

print(s)