
def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]
    
    code_chars = len(''.join(lines))

    s = ''.join([line[1:-1] for line in lines])
    s = s.replace(r'\\', '_')
    s = s.replace(r'\"', '_')
    str_chars = len(s) - s.count(r'\x') * 3

    yield code_chars - str_chars

    # Part 2

    s = ''.join(line for line in lines)
    str_chars = len(s) + 2 * len(lines)
    str_chars += s.count('"')
    str_chars += s.count('\\')

    yield str_chars - code_chars