
class OutOfBounds(Exception): pass
class LoopDetected(Exception): pass

def move_guard_to_next(guard, obs):
    dir, gr, gc, _ = guard
    if dir in '^v': obs = sorted([obs[0][i] for i in range(len(obs[0])) if obs[1][i] == gc])
    if dir in '<>': obs = sorted([obs[1][i] for i in range(len(obs[0])) if obs[0][i] == gr])
    if dir in '^<': obs = obs[::-1]
    for o in obs:
        if dir == '^':
            if o<gr: return '>', o+1, gc, abs((o+1)-gr)
        if dir == 'v':
            if o>gr: return '<', o-1, gc, abs((o-1)-gr)
        if dir == '<':
            if o<gc: return '^', gr, o+1, abs((o+1)-gc)
        if dir == '>':
            if o>gc: return 'v', gr, o-1, abs((o-1)-gc)
    raise OutOfBounds

def get_guard_turns(guard, obs, grid_size):
    # Create a list of coordinates where the guard runs into a obstacle and turns
    path = [(guard[1], guard[2]), ]
    steps = 0
    try:
        while True:
            guard = move_guard_to_next(guard, obs)
            path.append((guard[1], guard[2]))
            steps += guard[3]

            # Detect a loop by seeing if the number of steps goes above the number of cells in the grid.
            if steps > grid_size[0]*grid_size[1]: raise LoopDetected

    # When the guard goes out of bounds, add the last coordinate before he steps out of the map to the path
    except OutOfBounds:
        if guard[0] == 'v': path.append((grid_size[0], guard[2]))
        if guard[0] == '^': path.append((0, guard[2]))
        if guard[0] == '>': path.append((guard[1], grid_size[1]))
        if guard[0] == '<': path.append((guard[1], 0))
        steps += (abs(path[-1][0] - abs(path[-2][0]))) + (abs(path[-1][1] - abs(path[-2][1])))

    return path

def get_obstacles_and_guard(grid):
    # Create a nested list with all obstacle coordinates [[rows], [cols]]
    obs = [[], []]
    for row_i, row in enumerate(grid):
        for col_i, col in enumerate(row):
            if col in '#O':
                obs[0].append(row_i)
                obs[1].append(col_i)
            if col in '^>v<':
                guard = (col, row_i, col_i, 0)
    return obs, guard

def solve(data):
    with open(data) as f:
        grid = [list(line.strip()) for line in f.readlines()]

    obs, guard = get_obstacles_and_guard(grid)
    path = get_guard_turns(guard, obs, (len(grid), len(grid[0])))

    # Connect the dots in a 2D list of booleans to keep track which coords are visited by the guard
    visited = set()
    for i in range(1, len(path)):
        S = path[i-1]
        F = path[i]
        dr = F[0] - S[0]
        dc = F[1] - S[1]

        for i in range(abs(dr+dc)):
            visited.add(((S[0]+i*(min(max(dr, -1), 1))) , (S[1]+i*(min(max(dc, -1), 1)))))

    yield len(visited)

    # Part 2

    # Go through the walked path and try putting an obstacle on every coord.
    loops = 0
    for i, (r, c) in enumerate(visited):
        print('\t{:.2f}%'.format(100*(i+1)/len(visited)), end='\r')
        try_grid = [row[:] for row in grid]
        if try_grid[r][c] in '^>v<': continue
        try_grid[r][c] = 'O'

        obs, guard = get_obstacles_and_guard(try_grid)
        try:
            path = get_guard_turns(guard, obs, (len(try_grid), len(try_grid[0])))
        except LoopDetected:
            loops += 1
            continue
    yield loops

    

