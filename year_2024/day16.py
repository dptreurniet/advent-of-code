import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def neighbors(grid, row, col):
    for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
        try_r = row + dr
        try_c = col + dc
        if not (0 <= try_r < len(grid)): continue
        if not (0 <= try_c < len(grid[0])): continue
        if grid[try_r][try_c] == '#': continue
        yield try_r, try_c

def find_char(maze, x):
    for row_i, row in enumerate(maze):
            for col_i, c in enumerate(row):
                if c == x: return row_i, col_i

def get_start(maze): return find_char(maze, 'S')
def get_end(maze): return find_char(maze, 'E')

def get_score(path):
    s = 0
    last_heading = 'E'
    for i in range(1, len(path)):
        if i == 0: continue
        
        dr, dc = path[i][0] - path[i-1][0], path[i][1]- path[i-1][1]
        if dr == -1: heading = 'N'
        if dr == 1: heading = 'S'
        if dc == -1: heading = 'W'
        if dc == 1: heading = 'E'
        
        if heading != last_heading: s += 1000
        else: s += 1
        
        last_heading = heading

    return s+1

def print_maze(grid, path = None):
    if not path: path = []
    for row_i, row in enumerate(grid):
        print('')
        for col_i, c in enumerate(row):
            if (row_i, col_i) in path: print('.', end='', flush=True)
            else: print('#' if c != '.' else ' ', end='', flush=True)
    print('')

def get_paths(maze, max_score, path = None):
    if not path:
        start = get_start(maze)
        path = [start,]
    
    curr_r, curr_c = path[-1]

    # Base case: found Exit
    if maze[curr_r][curr_c] == 'E':
        yield path
        return

    # If  current score goes above max, abort
    if get_score(path) > max_score: return

    nbs = list(neighbors(maze, curr_r, curr_c))
    for nb_r, nb_c in nbs:
        if (nb_r, nb_c) not in path:
            yield from get_paths(maze, max_score, path + [(nb_r, nb_c),])

    return

def solve(data):
    with open(data) as f:
        maze = [line.strip() for line in f.readlines()]

    G = nx.Graph()

    # Create set of nodes
    nodes_without_dir = set()
    for row_i, row in enumerate(maze):
        for col_i, c in enumerate(row):
            if c in '.SE':
                nodes_without_dir.add(f'{row_i}_{col_i}')
                G.add_node(f'{row_i}_{col_i}_NS')
                G.add_node(f'{row_i}_{col_i}_EW')

    # Create connections between cell directions
    for node in nodes_without_dir:
        G.add_edge(f'{node}_NS', f'{node}_EW', weight=1000)

    # Create connections between cells
    for row_i, row in enumerate(maze):
        for col_i, c in enumerate(row):
            if c == '#': continue
            for nb_r, nb_c in neighbors(maze, row_i, col_i):
                if nb_r - row_i != 0:
                    G.add_edge(f'{row_i}_{col_i}_NS', f'{nb_r}_{nb_c}_NS', weight = 1)
                else:
                    G.add_edge(f'{row_i}_{col_i}_EW', f'{nb_r}_{nb_c}_EW', weight = 1)

    # Add start and end nodes
    G.add_node('S')
    r, c = get_start(maze)
    G.add_edge('S', f'{r}_{c}_EW', weight = 1)
    
    G.add_node('E')
    r, c = get_end(maze)
    G.add_edge('E', f'{r}_{c}_NS', weight = 1)
    G.add_edge('E', f'{r}_{c}_EW', weight = 1)

    # Find path
    path = nx.shortest_path(G, source='S', target='E', weight='weight')
    path = [tuple(map(int, p.split('_')[:2])) for p in path[1:-1]]

    yield get_score(path)

    # Part 2

    paths = nx.all_shortest_paths(G, source='S', target='E', weight='weight')
    tiles = set()
    for path in paths:
        path = [tuple(map(int, p.split('_')[:2])) for p in path[1:-1]]
        for tile in path: tiles.add(tile)

    yield len(tiles)

