
def is_valid(triangle):
    if (triangle[0] + triangle[1]) <= triangle[2]: return False
    if (triangle[0] + triangle[2]) <= triangle[1]: return False
    if (triangle[1] + triangle[2]) <= triangle[0]: return False
    return True

def solve(data):
    with open(data) as f:
        triangles = sorted([list(map(int, line.split())) for line in f.readlines()])
    yield list(map(is_valid, triangles)).count(True)

    # Part 2
    
    triangles = []
    with open(data) as f:
        lines = [list(map(int,line.split())) for line in f.readlines()]
    for i in range(0, len(lines), 3):
        for j in range(3):
            triangles.append((lines[i][j], lines[i+1][j], lines[i+2][j]))
    yield list(map(is_valid, triangles)).count(True)
    