from itertools import combinations

def min_QE(P, w):
    min_size = [sum(P[:i])>=w for i in range(1, len(P))].index(True)+1
    max_size = len(P) - 2 * min_size

    G1 = []
    for size in range(min_size, max_size + 1):
        G1.extend(filter(lambda x: sum(x) == w, combinations(P, size)))
        if len(G1) > 0: break
    
    QEs = []
    for g in G1:
        QE = 1
        for p in g: QE *= p
        QEs.append(QE)

    return min(QEs)

def solve(data):
    with open(data) as f:
        P = sorted([int(line.strip()) for line in f.readlines()], reverse=True)
    
    total_w = sum(P)
    yield min_QE(P, total_w / 3)
    yield min_QE(P, total_w / 4)

