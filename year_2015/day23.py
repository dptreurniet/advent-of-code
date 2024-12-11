
def solve(data):
    with open(data) as f:
        program = [tuple(line.replace(',', ' ').strip().split()) for line in f.readlines()]

    for a in range(2):
        b = 0
        i = 0
        try:
            while True:
                cmd = program[i]
                if cmd[0] == 'hlf':
                    if cmd[1] == 'a': a /= 2
                    else: b /= 2
                    i += 1
                    continue
                elif cmd[0] == 'tpl':
                    if cmd[1] == 'a': a *= 3
                    else: b *= 3
                    i += 1
                    continue
                elif cmd[0] == 'inc':
                    if cmd[1] == 'a': a += 1
                    else: b += 1
                    i += 1
                    continue
                elif cmd[0] == 'jmp':
                    if cmd[1][0] == '+': i += int(cmd[1][1:])
                    else: i -= int(cmd[1][1:])
                    continue
                elif cmd[0] == 'jie':
                    r = a if cmd[1] == 'a' else b
                    if r%2 == 0:
                        if cmd[2][0] == '+': i += int(cmd[2][1:])
                        else: i -= int(cmd[2][1:])
                    else:
                        i += 1
                    continue
                elif cmd[0] == 'jio':
                    r = a if cmd[1] == 'a' else b
                    if r == 1:
                        if cmd[2][0] == '+': i += int(cmd[2][1:])
                        else: i -= int(cmd[2][1:])
                    else:
                        i += 1
                    continue
        except IndexError:
            yield b
            