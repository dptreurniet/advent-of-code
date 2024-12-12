
def get_matching_neighbors(grid, coord):
    r, c  = coord
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    for dr, dc in zip(drs, dcs):
        if not (0 <= r+dr < len(grid)): continue
        if not (0 <= c+dc < len(grid[0])): continue
        if grid[r+dr][c+dc] == grid[r][c]:
            yield (r+dr, c+dc)
        
def get_perimeter(region):
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]
    P = 0
    for r, c in region:
        p = 4
        for dr, dc in zip(drs, dcs):
            if (r+dr, c+dc) in region: p -= 1
        P += p
    return P

def get_region(grid, coord):
    region = [coord,]
    to_check = [coord,]
    while to_check:
        for coord in to_check:
            to_check.remove(coord)
            nbs = list(get_matching_neighbors(grid, coord))
            for nb in nbs:
                if nb not in region:
                    region.append(nb)
                    to_check.append(nb)
    return list(set(region))

def get_exposed_sides(region, coord):
    r, c = coord
    S = ''
    if (r+1, c) not in region: S += 'D'
    if (r-1, c) not in region: S += 'U'
    if (r, c+1) not in region: S += 'R'
    if (r, c-1) not in region: S += 'L'
    return S

def get_sides(region):
    X = {
        'U': [  ([(0,1), (-1,1)],   1, 'L'),
                ([(0,1)],           0, 'U'),
                ([],                1, 'R')],
        'R': [  ([(1,0), (1,1)],    1, 'U'),
                ([(1,0)],           0, 'R'),
                ([],                1, 'D')],
        'D': [  ([(0,-1), (1,-1)],  1, 'R'),
                ([(0,-1)],          0, 'D'),
                ([],                1, 'L')],
        'L': [  ([(-1,0), (-1,-1)], 1, 'D'),
                ([(-1,0)],          0, 'L'),
                ([],                1, 'U')]}
    
    exposed_sides = [(coord, get_exposed_sides(region, coord)) for coord in region]
    all_edges = []
    for coord, S in exposed_sides:
        for s in S:
            all_edges.append((coord, s))

    corners = 0
    while all_edges:
        coord = [x for x in all_edges if x[1] == 'U'][0][0]
        edge = 'U'
        start_coord = coord[:]
        start_edge = edge[:]
        while True:
            x = X[edge]
            for option in x:
                req_nbs = [(coord[0]+dr, coord[1]+dc) for dr, dc in option[0]]
                if all([nb in region for nb in req_nbs]):
                    all_edges.remove((coord, edge))
                    corners += option[1]
                    edge = option[2]
                    if option[0]: coord = (coord[0]+option[0][-1][0], coord[1]+option[0][-1][1])
                    break
            
            if edge == start_edge and coord == start_coord: break
    return corners

def solve(data):
    with open(data) as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    for cost_fn in [get_perimeter, get_sides]:
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        cost = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visited[r][c]:
                    region = get_region(grid, (r, c))
                    area = len(region)
                    X = cost_fn(region)
                    cost += area * X
                    for rr, cc in region:
                        visited[rr][cc] = True
        yield cost
