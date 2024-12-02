

def solve(data):

    with open(data) as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    
    A = sorted([line[0] for line in lines])
    B = sorted([line[1] for line in lines])
    C = [abs(A[i] - B[i]) for i in range(len(A))]
    print(f'Answer part 1: {sum(C)}')
    print(f'Answer part 2: {sum([a * B.count(a) for a in A])}')


