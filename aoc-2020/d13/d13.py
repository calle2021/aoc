infile = "input.txt"

wait = 0
busses = []
for i, line in enumerate(open(infile)):
    line = line.strip()
    if i == 0:
        wait = int(line)
    else:
        busses = line.split(",")
        busses = [(i, int(b)) for i, b in enumerate(line.split(",")) if b != "x"]

#part 1
min_wait = float("inf")
buss_id = 0
for _, b in busses:
    wait_time = b - wait % b
    if wait_time < min_wait:
        min_wait = wait_time
        buss_id = b
print(min_wait * buss_id)

#part 2
step_size = 1
idx = 0
for offset, b in busses:
    while True:
        idx += step_size
        if (idx + offset) % b == 0:
            step_size = step_size * b
            break
print(idx)