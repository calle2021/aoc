input = "input.txt"

sides = [
    (0.5, 0, 0.5), (0.5, 0.5, 0), (1, 0.5, 0.5), (0.5, 1, 0.5), (0.5, 0.5, 1), (0, 0.5, 0.5)
]
cs = [eval(c.strip())for c in open(input).readlines()]
cubes = [({(c[0] + s[0], c[1] + s[1], c[2] + s[2]) for s in sides}) for c in cs]

unique = len(set().union(*cubes))
surface_area = 2 * unique - len(cubes) * 6
print(surface_area)
