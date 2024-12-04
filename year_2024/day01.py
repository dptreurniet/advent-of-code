

def solve(data):

    with open(data) as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    
    A = sorted([line[0] for line in lines])
    B = sorted([line[1] for line in lines])
    C = [abs(A[i] - B[i]) for i in range(len(A))]
    yield sum(C)
    yield sum([a * B.count(a) for a in A])


