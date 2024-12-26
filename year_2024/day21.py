
class Pad:
    def __init__(self, *lines: str):
        self.lines = lines

    def coord(self, char: str):
        r = [char in line for line in self.lines].index(True)
        c = self.lines[r].index(char)
        return r, c
    
    def gap(self): return self.coord(' ')

numpad = Pad('789', '456', '123', ' 0A')
dirpad = Pad(' ^A', '<v>')

def shortest_path(key1: str, key2: str, pad: Pad):
    r1, c1 = pad.coord(key1)
    r2, c2 = pad.coord(key2)

    ver = '^'*(r1 - r2) if r1 > r2 else 'v'*(r2 - r1)
    hor = '<'*(c1 - c2) if c1 > c2 else '>'*(c2 - c1)
    
    if c2 > c1 and (r2, c1) != pad.gap(): return ver+hor+'A'
    if (r1, c2) != pad.gap(): return hor+ver+'A'
    return ver+hor+'A'

def get_route(code, pad):
    keys = []
    prev_key = 'A'
    for key in code:
        keys.append(shortest_path(prev_key, key, pad))
        prev_key = key
    return keys

def complexity(codes, n_robots):

    def seq_counts(seq):
        f_map = {}
        for s in get_route(seq, dirpad):
            try: f_map[s] += 1
            except KeyError: f_map[s] = 1
        return f_map
    
    f_tables = [
        {''.join(get_route(code, numpad)): 1} for code in codes
    ]

    for _ in range(n_robots):
        new_f_tables = []
        for f_table in f_tables:
            sub_f_table = {}
            for seq, freq in f_table.items():
                for sub_seq, sub_freq in seq_counts(seq).items():
                    try: sub_f_table[sub_seq] += sub_freq * freq
                    except KeyError: sub_f_table[sub_seq] = sub_freq * freq
            new_f_tables.append(sub_f_table)
        f_tables = new_f_tables

    def cmplx(seq):
        return sum(len(key) * freq for key, freq in seq.items())
        
    return sum(cmplx(f_table) * int(codes[i][:-1]) for i, f_table in enumerate(f_tables))

def solve(data):

    with open(data) as f:
        codes = [line.strip() for line in f.readlines()]
    
    yield complexity(codes, 2)
    yield complexity(codes, 25)
