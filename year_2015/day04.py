import hashlib

def solve(data):
    with open(data) as f: key = f.readline()

    i = 0
    while True:
        h = hashlib.md5(f'{key}{i}'.encode()).hexdigest()
        if h[:5] == '00000': break
        i += 1
    yield i

    # Part 2

    i = 0
    while True:
        h = hashlib.md5(f'{key}{i}'.encode()).hexdigest()
        if h[:6] == '000000': break
        i += 1
    yield i

