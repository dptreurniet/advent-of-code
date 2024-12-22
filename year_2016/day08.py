
def print_screen(screen):
    for r in screen: print(''.join(['#' if c else ' ' for c in r]))

def solve(data):
    with open(data) as f:
        cmds = [line.strip() for line in f.readlines()]

    screen = [[False for _ in range(50)] for __ in range(6)]

    for cmd in cmds:
        #print_screen(screen)
        if cmd.startswith('rect'):
            A, B = list(map(int, cmd.split(' ')[1].split('x')))
            for r in range(B):
                for c in range(A):
                    screen[r][c] = True
            continue
        if cmd.startswith('rotate row'):
            A = int(cmd.split(' ')[2].split('=')[1])
            B = int(cmd.split(' ')[4])
            row = screen[A][:]
            screen[A][B:] = row[:-B]
            screen[A][:B] = row[-B:]
            continue
        if cmd.startswith('rotate column'):
            A = int(cmd.split(' ')[2].split('=')[1])
            B = int(cmd.split(' ')[4])
            col = [r[A] for r in screen]
            for i in range(len(screen)):
                screen[i][A] = col[(i - B + len(screen)) % len(screen)]
            continue
    

    yield sum([r.count(True) for r in screen])
    print_screen(screen)
    yield 'See output above'