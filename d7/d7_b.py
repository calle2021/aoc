import re
from functools import cmp_to_key
input = "input.txt"

hands = [d.strip() for d in open(input).readlines()]

s = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def type_score(hand):
    unique = set(hand)
    counts = []
    js = 0
    if "J" in unique:
        unique.remove("J")
        js = hand.count("J")
    
    if js == 5: return 7

    for u in unique:
        counts.append(hand.count(u))

    # add js to highest count
    if js:
        counts = sorted(counts)
        counts[-1] += js

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
    if len(unique) == len(hand):
        return 1
    return None #sanity

def compare_hands(h1, h2):
    c1 = h1.split(" ")[0]
    c2 = h2.split(" ")[0]
    t1 = type_score(c1)
    t2 = type_score(c2)

    if t1 > t2:
        return 1
    elif t2 > t1:
        return -1

    for i in range(len(c1)):
        if c1[i] == c2[i]:
            continue
        if s.index(c1[i]) < s.index(c2[i]):
            return 1
        else:
            return -1
    else:
        return 0

hands.sort(key = cmp_to_key(compare_hands))
winnings = 0
for rank, hand in enumerate(hands):
    bid = int(hand.split(" ")[1])
    winnings += (rank + 1) * bid
#part 2
print(winnings)