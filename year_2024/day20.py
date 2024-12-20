
from itertools import combinations

def get_neighbors(track, coord):
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dr, dc in deltas:
        try_r, try_c = coord[0] + dr, coord[1] + dc
        if not (0 <= try_r < len(track)): continue
        if not (0 <= try_c < len(track[0])): continue
        if track[try_r][try_c] != '#': yield (try_r, try_c)

def get_path(track):
    S = [(r_i, c_i) for r_i, r in enumerate(track) for c_i, c in enumerate(r) if c == 'S'][0]
    prev = S[:]
    path = [S[:],]
    while track[path[-1][0]][path[-1][1]] != 'E':
        nbs = [nb for nb in get_neighbors(track, path[-1]) if nb != prev]
        prev = path[-1]
        path.append(nbs[0])
    return path

def get_cheatable_walls(track):
    return [(r_i, c_i)
            for r_i, r in enumerate(track) 
            for c_i, c in enumerate(r) 
            if c == '#' and 
            len(list(get_neighbors(track, (r_i, c_i)))) >= 2]

def dist(A, B): return abs(B[0] - A[0]) + abs(B[1] - A[1])

def solve(data):
    with open(data) as f:
        track = [line.strip() for line in f.readlines()]
    
    path = get_path(track)

    cheatable_walls = get_cheatable_walls(track)
    
    cheats = []
    for wall in cheatable_walls:
        nbs = list(get_neighbors(track, wall))
        nb_ix = [path.index(nb) for nb in nbs]
        for A, B in combinations(nb_ix, 2):
            cheats.append(abs(A-B)-2)

    yield len([t for t in cheats if t >= 100])

    # Part 2
    
    cheats = []
    for i, A in enumerate(path):
        print('{:.0f}%'.format(100*(i+1)/len(path)), end='\r')
        for j, B in enumerate(path[i+1:]):
            D = dist(A, B)
            if D > 20: continue
            if D == 1: continue
            walking_D = j + 1
            if D == walking_D: continue
            savings = walking_D - D
            if savings < 50: continue
            cheats.append(savings)

    yield len([t for t in cheats if t >= 100])
