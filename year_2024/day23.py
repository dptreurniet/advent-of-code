import networkx as nx
import matplotlib.pyplot as plt

def solve(data):
    with open(data) as f:
        conns = [line.strip() for line in f.readlines()]

    G = nx.Graph()
    for conn in conns:
        A, B = conn.split('-')
        G.add_node(A)
        G.add_node(B)
        G.add_edge(A, B)

    groups = set()
    for A in G.nodes():
        for B in G[A]:
            for C in G[B]:
                if A in G[C]:
                    groups.add(tuple(sorted([A, B, C])))
    
    t = 0
    for group in groups:
        if any([g[0] == 't' for g in group]): t += 1
    yield t

    # Part 2

    cliques = nx.algorithms.clique.find_cliques(G)
    yield ','.join(sorted(max(cliques, key=len)))
