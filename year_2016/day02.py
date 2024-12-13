
steps = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1)
    }

def code(keypad, lines):
    code= ''
    curr = [len(keypad)//2, len(keypad[0])//2]
    for line in lines:
        for c in line:
            try_row = curr[0] + steps[c][0]
            try_col = curr[1] + steps[c][1]
            if 0 <= try_row < len(keypad) and 0 <= try_col < len(keypad[0]):
                if keypad[try_row][try_col] != '_': curr = [try_row, try_col]
        code += keypad[curr[0]][curr[1]]
    return code

def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]

    keypad = ['123', '456', '789']
    yield code(keypad, lines)

    keypad = ['__1__', '_234_', '56789', '_ABC_', '__D__']
    yield code(keypad, lines)