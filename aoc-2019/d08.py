import numpy as np
file = "input.txt"
data = open(file).read().strip()
w = 25
h = 6
d = len(data) // (w * h)
i = 0
layers = np.zeros((h, w, d))
z = 0
while i != len(data):
    x = i % w
    y = (i // w) % h
    z = i // (w * h) 
    layers[y, x, z] = int(data[i])
    i+=1

digits = []
for i in range(layers.shape[2]):
    layer = layers[:,:, i]
    digits.append((np.count_nonzero(layer==0),np.count_nonzero(layer==1), np.count_nonzero(layer==2)))
digits.sort(key=lambda x: x[0])
print(digits[0][1] * digits[0][2])

m = {1 :"#", 0 : " "}
image = []
for y in range(h):
    row = ""
    for x in range(w):
        pixel = [ i for i in layers[y, x, :] if i != 2][0]
        assert pixel != 2
        row = row + str(m[int(pixel)])
    print(row)