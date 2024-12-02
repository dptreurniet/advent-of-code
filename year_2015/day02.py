
def solve(data):
    with open(data) as f:
        sizes = [list(map(int, line.strip().split('x'))) for line in f.readlines()]
    
    total = 0
    for s in sizes:
        A = s[0] * s[1]
        B = s[1] * s[2]
        C = s[0] * s[2]
        total += 2*A + 2*B + 2*C + min([A, B, C])
    yield total

    total = 0
    for s in sizes:
        A = 2*s[0] + 2*s[1]
        B = 2*s[1] + 2*s[2]
        C = 2*s[0] + 2*s[2]
        total += min([A, B, C]) + s[0] * s[1] * s[2]
    yield total