input = "ex.txt"


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
    for y in range(my +1):
        for x in range(mx +1 ):
            v = x + y * 1j
            if v in r:
                print("O", end="")
            elif v in s:
                print("#", end="")
            else:
                print(".", end="") 
        print("")

dirs = {"N" : -1j, "W" : -1, "S" : 1j, "E" : 1}
s = {
    "N" : lambda x: x.imag,
    "S" : lambda x: -x.imag,
    "W" : lambda x: x.real,
    "E" : lambda x: -x.real
}


cycle = 0
target = 100000000
t = [round]
cache = {tuple(round)}
while True:
    cycle += 1
    print(cycle)
    for d in dirs:
        i = 0
        stat = stationary[:]
        round = sorted(round, key=s[d])
        while i != len(round):
            while round[i] not in stat and round[i].imag >= 0 and round[i].real >= 0 and round[i].imag <= my and round[i].real <= mx:
                round[i] += dirs[d]
            round[i] += -1 * dirs[d]
            stat.append(round[i])
            i += 1

    key = tuple(round)

    if key in cache:
        break
        
    cache.add(key)
    t.append(round[:])


f = t.index(round[:])
r = t[(target - f) % (cycle - f) + f]

load = int(sum(my - l.imag + 1 for l in r))
print("load", load)