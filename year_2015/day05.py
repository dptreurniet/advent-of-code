import re

vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']

def is_nice_1(s):
    if len(s) < 2: return False
    if sum([s.count(v) for v in vowels]) < 3: return False
    if not any([s[i] == s[i-1] for i in range(1, len(s))]): return False
    if any([substr in s for substr in forbidden]): return False
    return True

def is_nice_2(s):
    if len(s) < 2: return False

    pairs = [s[i-1]+s[i] for i in range(1, len(s))]
    for pair in pairs:
        if pair in s.replace(pair, '', 1):
            print(s, pair)
            break
    else: return False

    print(re.findall(r'(.).(?=\1)', s))
    return len(re.findall(r'(.).(?=\1)', s)) > 0


def solve(data):
    with open(data) as f:
        strings = [line.strip() for line in f.readlines()]
    print(strings)
    
    yield len([s for s in strings if is_nice_1(s)])
    yield len([s for s in strings if is_nice_2(s)])
