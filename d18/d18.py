data = "input.txt"

sides = [
    (0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)
]
cs = [eval(c.strip())for c in open(data).readlines()]
cubes = [({(c[0] + s[0], c[1] + s[1], c[2] + s[2]) for s in sides}) for c in cs]

faces = set().union(*cubes)
surface_area = 2 * len(faces) - len(cubes) * 6

m = 2 #margin of bounding box
mx = min(cs, key=lambda t: t[0])[0] - m
my = min(cs, key=lambda t: t[1])[1] - m
mz = min(cs, key=lambda t: t[2])[2] - m

Mx = max(cs, key=lambda t: t[0])[0] + m
My = max(cs, key=lambda t: t[1])[1] + m
Mz = max(cs, key=lambda t: t[2])[2] + m

q = [(mx, my, mz)]
air = {(mx, my, mz)}
while q:
    x, y, z = q.pop(0)
    for dx, dy, dz in sides:
        nx, ny, nz = c = (x + 2*dx, y + 2*dy, z + 2*dz)
        if not (mx <= nx < Mx and my <= ny < My and mz <= nz < Mz):
            continue
        if c in air or c in cs:
            continue
        q.append(c)
        air.add(c)

free = {(a[0] + s[0], a[1] + s[1], a[2] + s[2]) for s in sides for a in air}
exterior = free & faces

#part 1
print(surface_area)
#part 2
print(len(exterior))