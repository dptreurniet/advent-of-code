import json
import itertools

s = 0

def flatten(it, value_to_ignore = ''):
    if type(it) == list:
        l = []
        for x in it:
            try: l.extend(flatten(x, value_to_ignore))
            except TypeError: l.append(flatten(x, value_to_ignore))
        return l
    if type(it) == dict:
        l = []
        for x in it.values():
            if x == value_to_ignore: return 0
            try: l.extend(flatten(x, value_to_ignore))
            except TypeError: l.append(flatten(x, value_to_ignore))
        return l
    return it

def solve(data):
    with open(data) as f:
        d = json.load(f)

    f = flatten(d)
    yield sum([x for x in f if type(x) == int])

    f = flatten(d, 'red')
    yield sum([x for x in f if type(x) == int])
