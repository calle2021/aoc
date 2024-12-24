from aocd import get_data
import re

puzzle = get_data(day=24, year=2024)
gates, wires = puzzle.split("\n\n")

gates =  {g[0] : int(g[1]) for g in re.findall(r"(\w+): (\d)", gates)}
zs = list(re.findall(r"z\d+", wires))

while zs:
    for wire in wires.split("\n"):
        left, op, right, dest = re.findall(r"(\w+) (AND|XOR|OR) (\w+) -> (\w+)", wire)[0]
        if left not in gates or right not in gates:
            continue
        if dest in zs:
            zs.remove(dest)
        match op:
            case "AND":
                gates[dest] = gates[left] & gates[right]
            case "XOR":
                gates[dest] = gates[left] ^ gates[right]
            case "OR":
                gates[dest] = gates[left] | gates[right]
            case _:
                assert False
z = int(''.join([str(gates[x]) for x in sorted([k for k in gates.keys() if "z" in k])][::-1]), 2)
print(z)