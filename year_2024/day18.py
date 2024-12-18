import numpy as np
from scipy.sparse.csgraph import shortest_path

def print_maze(maze):
    print('')
    for row in maze:
        print(''.join(row))

def neighbors(maze, row, col):
    nbs = []
    for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
        try_r = row + dr
        try_c = col + dc
        if not (0 <= try_r < len(maze)): continue
        if not (0 <= try_c < len(maze[0])): continue
        if maze[try_r][try_c] == '#': continue
        nbs.append((try_r, try_c))
    return nbs

def run_maze(maze):
    n_rows, n_cols = len(maze), len(maze[0])

    # Gather nodes
    nodes = set()
    for row_i, row in enumerate(maze):
        for col_i, c in enumerate(row):
            if c == '.':
                nodes.add((row_i, col_i))

    conn = {}
    for node in nodes:
        conn[node] = set()
    
    for r, c, in nodes:
        for nb_r, nb_c in neighbors(maze, r, c):
            conn[(r, c)].add((nb_r, nb_c))

    # Create M matrix
    M = np.array([[0 for _ in range(n_cols * n_rows)] for __ in range(n_rows * n_cols)])
    for node, nbs in conn.items():
        i1 = node[0] * n_cols + node[1]
        for nb in nbs:
            i2 = nb[0] * n_cols + nb[1]
            M[i1][i2] = 1
            M[i2][i1] = 1

    return shortest_path(M, directed=True, indices = 0)[-1]

def maze_after_n_drops(b, n):
    n_rows = max([p[0] for p in b]) + 1
    n_cols = max([p[1] for p in b]) + 1

    maze = [['.' for _ in range(n_cols)] for __ in range(n_rows)]
    for c, r in b[:n]:
        maze[r][c] = '#'
    
    return maze

def solve(data):
    with open(data) as f:
        b = [list(map(int, line.strip().split(','))) for line in f.readlines()]
    
    maze = maze_after_n_drops(b, 1024)
    
    yield int(run_maze(maze))

    n_bytes = len(b)
    n = n_bytes // 2
    step = n_bytes // 4
    prev_OK = False
    while True:
        print(str(step) + '...        ', end='\r')
        maze = maze_after_n_drops(b, n)
        res = run_maze(maze)

        if np.isinf(res):
            if step == 1 and prev_OK:
                yield ','.join(list(map(str,b[n-1])))
                return
            n -= step
            prev_OK = False
        else:
            n += step
            prev_OK = True

        step = max(1, step // 2)
