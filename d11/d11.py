infile = "input.txt"
data = []
for line in open(infile):
    line = line.strip()
    data.append(line)

empty = set()
max_x = 0
max_y = 0
for r, row in enumerate(data):
    for c, col in enumerate(row):
        if col == "L":
            empty.add((c,r))
            max_x = max(max_x, c)
            max_y = max(max_y, r)

dirs = [ (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1) ] 

def adj(seat, occ, dirs, max_x, max_y):
    count = 0
    for d in dirs:
        x = seat[0] + d[0]
        y = seat[1] + d[1]
        if x < 0 or y < 0:
            continue
        if x > max_x or y > max_y:
            continue
        if (x, y)  in occ:
            count += 1
    return count

occupied = set()
while True:
    to_be_filled = set()    
    for seat in empty:
        if adj(seat, occupied, dirs, max_x, max_y) == 0:
            to_be_filled.add(seat)

    for s in to_be_filled:
        empty.remove(s)
        occupied.add(s)

    to_be_empty = set()
    for seat in occupied:
        if adj(seat, occupied, dirs, max_x, max_y) >= 4:
            to_be_empty.add(seat)

    if len(to_be_empty) == 0:
        print(len(occupied))
        break
    
    for s in to_be_empty:
        occupied.remove(s)
        empty.add(s)