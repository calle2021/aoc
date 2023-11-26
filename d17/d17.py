input = "input.txt"
jets = [1 if j == ">" else -1 for j in open(input).read()]

rocks = [
    [ 0, 1, 2, 3 ],
    [ 1j, 1, 1 + 1j, 1 + 2j, 2 + 1j],
    [ 0, 1, 2, 2 + 1j, 2 + 2j],
    [ 0, 1j, 2j, 3j],
    [ 0, 1, 1j, 1 + 1j]
]

solid = {x for x in range(8)}
h = 0
idx = 0
rock = {x + 3 + (h + 4) * 1j for x in rocks[idx]}

def printer(rock, h):
    
    for y in range(int(h) + 7, -2, -1):
        for x in range(9):
            if x == 0 or x == 8 :
                print("|", end="")
            elif x + y*1j in solid:
                print("#", end="")
            elif x + y*1j in rock:
                print("@", end="")
            else:
                print("." , end = "")
        print("")
    print("")
rc = 0      

c = 0
while rc < 2022:
    print("The first rock begins falling:")
    printer(rock, h)
    while True:
        jet = jets.pop(0)
        jets.append(jet)
        pushed = {r + jet for r in rock}
        if all(0 < p.real < 8 for p in pushed) and not (pushed & solid):
            print("Jet of gas pushes")
            printer(pushed, h)
            rock = pushed
        else:
            print("Jet of gas pushes but nothing happens")
            printer(rock, h)


        down = {r - 1j for r in rock}
        if down & solid:
            solid |= rock
            rc += 1
            idx = (idx + 1) % 5
            print("Rock falls 1 unit, causing it to come to rest:")
            printer(rock, h)
            h = max(r.imag for r in solid)
            if rc >= 2022:
                break 
            print("height is ", h)
            rock = {x + 3 + (h + 4) * 1j for x in rocks[idx]}
            c += 1
            break
        else:
            print("rock falls 1 unit")
            printer(down, h)
            rock = down

    if c == 2:
        printer(rock, h)
        print(h)
        break
print(h)