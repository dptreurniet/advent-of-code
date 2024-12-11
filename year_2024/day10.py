

def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            for j in flatten(i):
                yield j
        else:
            yield i

def possible_steps(grid, coord):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = coord
    for dr, dc in zip(dr, dc):
        try_r = r + dr
        try_c = c + dc
        if not (0 <= try_r < len(grid)): continue
        if not (0 <= try_c < len(grid[0])): continue
        yield (try_r, try_c)

def next_steps(grid, coord):
    #print(coord)
    curr_h = grid[coord[0]][coord[1]]
    if curr_h == 9:
        return coord

    options = []
    for step_r, step_c in possible_steps(grid, coord):
        if grid[step_r][step_c] == curr_h + 1:
            options.append((step_r, step_c))
    
    return [next_steps(grid, c) for c in options]

def solve(data):
    with open(data) as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    trailheads = []
    for r_i, r in enumerate(grid):
        for c_i, c in enumerate(r):
            try:
                grid[r_i][c_i] = int(c)
                if grid[r_i][c_i] == 0: trailheads.append((r_i, c_i))
            except ValueError: pass

    score = 0
    for trailhead in trailheads:
        peaks = list(flatten(next_steps(grid, trailhead)))
        score += len(set(peaks))

    yield score

    # Part 2

    score = 0
    for trailhead in trailheads:
        peaks = list(flatten(next_steps(grid, trailhead)))
        score += len(peaks)

    yield score
