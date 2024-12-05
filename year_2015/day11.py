import re

def increment(password):
    ds = [ord(c)-97 for c in password]
    ds[-1] += 1
    for i in range(len(password)-1, 0, -1):
        ds[i-1] += ds[i] // 26
        ds[i] %= 26
    return ''.join([chr(i+97) for i in ds])

def get_dist_between_chars(password):
    return [ord(password[i]) - ord(password[i-1]) for i in range(1, len(password))]

def has_inc_straight(password):
    return '|1|1|' in '|'+'|'.join([str(d) for d in get_dist_between_chars(password)])+'|'

def has_two_pairs(password):
    r = re.findall(r'(.)\1', password)
    return len(r) > 1# and len(set(r)) > 1

def is_OK(password):
    if not has_inc_straight(password): return False
    if any([c in password for c in 'iol']): return False
    if not has_two_pairs(password): return False
    return True

def solve(data):
    
    with open(data) as f:
        password = f.readline().strip()
    
    for _ in range(2):
        while not is_OK(password):
            password = increment(password)
        yield password
        password = increment(password)

