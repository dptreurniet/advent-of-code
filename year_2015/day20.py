from functools import reduce
from math import sqrt

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
        step = 2 if n%2 else 1
        return set.union(*[set([i, n//i]) for i in range(1, int(sqrt(n))+1, step) if not n % i])

def factors_with_limit(n, limit):
    step = 2 if n%2 else 1
    f = [set([i, n//i]) for i in range(1, int(sqrt(n))+1, step) if not n % i]
    if not f: return None
    f = set.union(*f)
    return [x for x in f if n / x < limit]

def solve(data):
    target = 34000000
    house = 1

    while True:
        p = 10 * sum(factors(house))
        if p >= target: break
        house += 1
    yield house

    # Part 2
    while True:
        p = 11 * sum(factors_with_limit(house, 50))
        if p >= target: break
        house += 1
    yield house
