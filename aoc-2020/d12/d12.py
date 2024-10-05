infile = "input.txt"
instructions = []
for line in open(infile):
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])
    instructions.append((direction, distance))

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def update_heading(h, d, dist):
    if dist == 180:
        return (-h[0] , -h[1] )
    if d == "L":
        if dist == 90:
            h = (-h[1], h[0])
        elif dist == 270:
            h = (h[1], -h[0])
    elif d == "R":
        if dist == 90:
            h = (h[1], -h[0])
        elif dist == 270:
            h = (-h[1], h[0])
    return h

curr_p1 = (0, 0) #part 1
curr_p2 = (0, 0) #part 2
h = (1, 0)
w = (10, 1)
for ins in instructions:
    d = ins[0]
    dist = ins[1]
    match d:
        case "N":
            curr_p1 = (curr_p1[0], curr_p1[1] + dist)
            w = (w[0], w[1] + dist)
        case "S": 
            curr_p1 = (curr_p1[0],  curr_p1[1] - dist)
            w = (w[0],  w[1] - dist)
        case "E":
            curr_p1 = (curr_p1[0] + dist , curr_p1[1])
            w = (w[0] + dist , w[1])
        case "W":
            curr_p1 = ( curr_p1[0] - dist, curr_p1[1])
            w = ( w[0] - dist, w[1])
        case "L":
            h = update_heading(h, d, dist)
            w = update_heading(w, d, dist)
        case "R":
            h = update_heading(h, d, dist)
            w = update_heading(w, d, dist)
        case "F":
            curr_p1 = ( curr_p1[0] + h[0] * dist, curr_p1[1] + h[1] * dist)
            curr_p2 = ( curr_p2[0] + w[0] * dist, curr_p2[1] + w[1] * dist)        
print(manhattan_distance((0,0), curr_p1))
print(manhattan_distance((0,0), curr_p2))