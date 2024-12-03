import re

def mul(a, b): return a*b

def solve(data):
    with open(data) as f:
        line = ''.join([line.strip() for line in f.readlines()])

    yield sum([eval(hit) for hit in re.findall('mul\(\d{1,3},\d{1,3}\)', line)])

    t = 0
    enabled = True
    for hit in re.findall('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line):
        if hit == 'don\'t()': enabled = False
        elif hit == 'do()': enabled = True
        elif enabled: t += eval(hit)
    yield t



