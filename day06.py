import networkx as nx

with open("input.txt") as f:
    pairs = [l.strip().split(")") for l in f.readlines()]

g = nx.DiGraph([(b, a) for a, b in pairs])
print(sum(len(nx.shortest_path(g, n, "COM")) - 1 for n in g.nodes()))
print(len(nx.shortest_path(nx.Graph(g), "YOU", "SAN")) - 3)
