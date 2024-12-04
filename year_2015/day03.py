
def solve(data):

    with open(data) as f:
        cmds = f.readline()

    x, y = 0, 0
    visited = [(x, y)]

    steps = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}

    for cmd in cmds:
        x += steps[cmd][0]
        y += steps[cmd][1]
        visited.append((x, y))
    
    yield len(set(visited))

    x1, y1, x2, y2 = 0, 0, 0, 0
    visited = [(x1, x2)]

    # Part 2

    for i, cmd in enumerate(cmds):
        if i%2:
            x1 += steps[cmd][0]
            y1 += steps[cmd][1]
            visited.append((x1, y1))
        else:
            x2 += steps[cmd][0]
            y2 += steps[cmd][1]
            visited.append((x2, y2))
    
    yield len(set(visited))



