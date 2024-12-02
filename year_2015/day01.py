
def solve(data):
    with open(data) as f:
        line = f.readline()
    yield line.count('(') - line.count(')')

    floor = 0
    for i, c in enumerate(line):
        floor += [-1, 1][c=='(']
        if floor < 0:
            yield i+1
            return