import networkx as nwx
from math import prod
input = "input.txt"

graph = nwx.Graph()

data = [d for d in open(input).read().splitlines()]

for d in data:
    comp, con = d.split(": ")
    con = con.split(" ")
    for c in con:
        graph.add_edge(comp, c)

graph.remove_edges_from(nwx.minimum_edge_cut(graph))
size = []
for c in nwx.connected_components(graph):
    size.append(len(c))
print(prod(size))