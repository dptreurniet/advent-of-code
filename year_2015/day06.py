
def solve(data):
    with open(data) as f:
        cmds = [line.strip() for line in f.readlines()]

    lights = [[False for _ in range(1000)] for __ in range(1000)]

    for cmd in cmds:
        cmd_split = cmd.split(' ')
        x1, y1 = map(int, cmd_split[-3].split(','))
        x2, y2 = map(int, cmd_split[-1].split(','))
       
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if cmd[:7] == 'turn on': lights[y][x] = True
                elif cmd[:8] == 'turn off': lights[y][x] = False
                else: lights[y][x] = not lights[y][x]

    yield sum([row.count(True) for row in lights])

    # Part 2
    lights = [[0 for _ in range(1000)] for __ in range(1000)]

    for cmd in cmds:
        cmd_split = cmd.split(' ')
        x1, y1 = map(int, cmd_split[-3].split(','))
        x2, y2 = map(int, cmd_split[-1].split(','))
       
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if cmd[:7] == 'turn on': lights[y][x] += 1
                elif cmd[:8] == 'turn off': lights[y][x] = max(lights[y][x] - 1, 0)
                else: lights[y][x] += 2

    yield sum([sum(row) for row in lights])