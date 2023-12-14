input = "ex0.txt"


round = []
square = []
stationary = []
my = 0
mx = 0
for y, row in enumerate( open(input).read().split("\n")):
    my = max(my, y)
    for x, v in enumerate(row):
        mx = max(mx, x)
        if v == "O":
            round.append(x + y * 1j) 
        elif v == "#":
            square.append(x + y * 1j)
            stationary.append(x + y * 1j)

def printer(s, r):
    for y in range(my):
        for x in range(mx):
            v = x + y * 1j
            if v in r:
                print("O", end="")
            elif v in s:
                print("#", end="")
            else:
                print(".", end="") 
        print("")
round = sorted(round, key=lambda x: x.imag)

dirs = {"N" : -1j, "W" : -1, "S" : 1j, "E" : 1}
cycle = 0
load = 0
seen = set()
for d in dirs:
    i = 0
    stat = stationary[:]
    while i != len(round):
        curr = round[i]
        while curr not in stat and curr.imag >= 0 and curr.real >= 0 and curr.imag <= my and curr.real <= mx:
            curr += dirs[d]
        curr += -1 * dirs[d]
        load += int(my - curr.imag + 1)
        stat.append(curr)
        i += 1
    #cycle += 1
    #key = (*stationary, d)
    #if key in stationary:
    #    load *= (1000000000 - cycle)
printer(stat, round)    
print(load)
