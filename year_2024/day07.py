import itertools

def can_be_made_true(eq, with_concat = False):
    operators = '+*'
    if with_concat: operators += '|'

    s = eq.split()
    result = int(s[0][:-1])
    parts = [int(d) for d in s[1:]]

    for operator_set in itertools.product(operators, repeat=len(parts)-1):
        t = parts[0]
        for i, operator in enumerate(operator_set):
            if operator == '+': t += parts[1+i]
            if operator == '*': t *= parts[1+i]
            if operator == '|': t = int(str(t) + str(parts[1+i]))
        if t == result:
            return result
    return 0

def solve(data):
    with open(data) as f:
        eqs = [line.strip() for line in f.readlines()]

    yield sum([can_be_made_true(eq) for eq in eqs])

    yield sum([can_be_made_true(eq, with_concat=True) for eq in eqs])