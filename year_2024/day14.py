
def map_size(robots):
    pos = [r[0] for r in robots]
    return max([p[0] for p in pos]) + 1, max([p[1] for p in pos]) + 1 

def print_map(robots, size=None, file=None):
    rows, cols = map_size(robots) if not map else size
    grid = [[0 for _ in range(cols)] for __ in range(rows)]
    for r in robots: grid[r[0][0]][r[0][1]] += 1
    if not file: print('')
    for r in grid: print(''.join(['#' if x > 0 else ' ' for x in r]), file=file)

def step(robots, map_size):
    new_robots = []
    for p, v in robots:
        new_p = [0,0]
        for i in range(2):
            new_p[i] = (p[i] + v[i]) % map_size[i]
        new_robots.append((tuple(new_p), v))
    return new_robots

def quadrant_counts(robots, size):
    r_mid = size[0] // 2
    c_mid = size[1] // 2
    ranges = [((0, r_mid),          (0, c_mid)),
              ((r_mid+1,size[0]),   (0, c_mid)),
              ((r_mid+1,size[0]),   (c_mid+1,size[1])),
              ((0, r_mid),          (c_mid+1,size[1]))]
    for r in ranges:
        yield [r[0][0] <= p[0] < r[0][1] and r[1][0] <= p[1] < r[1][1] for p,_ in robots].count(True)


def solve(data):
    robots = []
    with open(data) as f:
        for line in f.readlines():
            robots.append(tuple([tuple(int(v) for v in x[2:].split(',')[::-1]) for x in line.split()]))
    size = map_size(robots)

    start_robots = tuple(robots)

    for i in range(100): robots = step(robots, size)
    counts = list(quadrant_counts(robots, size))
    
    safety_factor = 1
    for c in counts: safety_factor *= c

    yield safety_factor
    

    with open('year_2024/output/day14.txt', 'w') as f:
            i = 100
            while True:
                # If the robots go back to their initial position, we can stop stepping
                if tuple(robots) == start_robots: break

                # By looking at the output, a pattern was found that repeats every 101 steps, starting at step 88.
                # An assumption was made that the christmas tree will be in that pattern
                if (i-88)%101 == 0:
                    print(f'{i} seconds passed', end='', file=f)
                    print_map(robots, size, file=f)
                robots = step(robots, size)
                i += 1

                # The answer to part 2 was found by drawing the maps of each step in the pattern to a file.
                # Then the file was zoomed out to allow quick scrolling while looking for the christmas tree manually.

