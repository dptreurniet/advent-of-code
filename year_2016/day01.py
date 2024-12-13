
def solve(data):
    with open(data) as f:
        cmds = [cmd.replace(',', '') for cmd in f.readline().strip().split()]
    
    dir_steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    facing = 0
    pos = [0, 0]
    visited = set(tuple(pos),)
    first_pos_visited_twice = None

    for cmd in cmds:
        turn = cmd[0]
        steps = int(cmd[1:])

        facing += 1 if turn == 'R' else -1
        if facing == -1: facing == 3
        facing %= 4

        for i in range(1, steps + 1):
            p = (pos[0] + i * dir_steps[facing][0], pos[1] + i * dir_steps[facing][1])
            if p in visited and not first_pos_visited_twice: first_pos_visited_twice = p
            visited.add(p)
        pos[0] += steps * dir_steps[facing][0]
        pos[1] += steps * dir_steps[facing][1]

    yield sum([abs(p) for p in pos])
    yield sum([abs(p) for p in first_pos_visited_twice])

