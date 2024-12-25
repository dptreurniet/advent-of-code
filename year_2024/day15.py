
def find_robot(grid):
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == '@':
                return ri, ci

def push_line(line):
    for i, c in enumerate(line):
        if c == '.': return '@'+line[:i]+line[i+1:]
        if c == '#': return line
    return line

def get_line(grid, coords, dir):
    ri, ci = coords
    dirs = {'^': (-1, 0, ri, 0),
            '>': (0, 1, ci, len(grid[0])-1),
            'v': (1, 0, ri, len(grid)-1),
            '<': (0, -1, ci, 0)}
    line = ''
    steps = abs(dirs[dir][3] - dirs[dir][2])
    for i in range(1, steps+1):
        line += grid[ri+i*dirs[dir][0]][ci+i*dirs[dir][1]]
    return line

def insert_line(grid, coord, dir, line):
    dirs = {'^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0),
            '<': (0, -1)}
    for i, c in enumerate(line):
        grid[coord[0]+(i+1)*dirs[dir][0]][coord[1]+(i+1)*dirs[dir][1]] = c
    return grid

def GPS_score(grid):
    s = 0
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c in 'O[': s += 100*ri + ci
    return s

def step(grid, dir):
    line = get_line(grid, coord := find_robot(grid), dir)
    line = push_line(line)
    if '@' not in line: return grid
    grid[coord[0]][coord[1]] = '.'
    return insert_line(grid, coord, dir, line)

def step_expanded_down(grid):
    robot_r, robot_c = find_robot(grid)
    getting_pushed = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
    getting_pushed[robot_r][robot_c] = True

    for r_i, r in enumerate(grid):
        for c_i, c in enumerate(r):
            if not getting_pushed[r_i][c_i]: continue
            if grid[r_i + 1][c_i] == '#': return grid
            if grid[r_i + 1][c_i] in '[]':
                getting_pushed[r_i + 1][c_i] = True
                if grid[r_i + 1][c_i] == ']':
                    getting_pushed[r_i + 1][c_i - 1] = True
                else:
                    getting_pushed[r_i + 1][c_i + 1] = True
    
    for r_i in range(len(getting_pushed)-1, -1, -1):
        r = getting_pushed[r_i]
        for c_i, c in enumerate(r):
            if not getting_pushed[r_i][c_i]: continue
            grid[r_i+1][c_i] = grid[r_i][c_i]
            grid[r_i][c_i] = '.'

            #for rr in grid:
            #    print(''.join(rr))
            #input()
    
    return grid
                    
def solve(data):
    with open(data) as f:
        lines = [list(line.strip()) for line in f.readlines()]

    i = 0
    grid, cmds = [], []
    while True:
        if not lines[i]: break
        grid.append(lines[i])
        i += 1
    original_grid = [row[:] for row in grid]
    i += 1
    while True:
        try: cmds.append(''.join(lines[i]))
        except IndexError: break
        i += 1
    cmds = ''.join(cmds)

    for dir in cmds:
        grid = step(grid, dir)

    yield GPS_score(grid)

    # Part 2

    grid = []
    for row in original_grid:
        grid.append(list(''.join(row)
        .replace('#', '##')
        .replace('O', '[]')
        .replace('.', '..')
        .replace('@', '@.')))

    for dir_i, dir in enumerate(cmds):
        print('{:.1f}%'.format(100*(dir_i+1)/len(cmds)), end='\r')
        if dir in '<>':
            grid = step(grid, dir)
        elif dir == 'v':
            grid = step_expanded_down(grid)
        else:
            grid = step_expanded_down(grid[::-1])[::-1]

    yield GPS_score(grid)