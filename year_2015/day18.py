
def neighbors(grid, r, c):
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == dc == 0: continue
            rr = r + dr
            cc = c + dc
            if not (0 <= rr < len(grid)): continue
            if not (0 <= cc < len(grid[0])): continue
            yield grid[rr][cc]


def step(grid, keep_corners_on = False):
    next_grid = [row[:] for row in grid]
    for ri, row in enumerate(grid):
        for ci, char in enumerate(row):
            lights_on = list(neighbors(grid, ri, ci)).count('#')
            if char == '#':
                if lights_on not in [2,3]: next_grid[ri][ci] = '.'
            else:
                if lights_on == 3: next_grid[ri][ci] = '#'
    if keep_corners_on:
        next_grid[0][0] = '#'
        next_grid[0][-1] = '#'
        next_grid[-1][0] = '#'
        next_grid[-1][-1] = '#'

    return next_grid
            


def solve(data):
    with open(data) as f:
        grid = [list(line.strip()) for line in f.readlines()]

    starting_grid = [row[:] for row in grid]

    n_steps = 100
    for i in range(n_steps):
        print(f'\t{i}/{n_steps}',end='\r')
        grid = step(grid)

    yield sum(row.count('#') for row in grid)

    grid = [row[:] for row in starting_grid]
    grid[0][0] = '#'
    grid[0][-1] = '#'
    grid[-1][0] = '#'
    grid[-1][-1] = '#'
    
    for i in range(n_steps):
        print(f'\t{i}/{n_steps}',end='\r')
        grid = step(grid, True)

    yield sum(row.count('#') for row in grid)