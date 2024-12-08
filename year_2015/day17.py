from itertools import combinations

def get_options(containers, target):
    for i in range(1, len(containers)):
        for combination in combinations(containers, i):
            if sum(combination) == target: yield combination

def solve(data):
    with open(data) as f:
        containers = [int(line.strip()) for line in f.readlines()]
    
    target = 150

    options = list(get_options(containers, target))
    yield len(options)

    min_length = min([len(option) for option in options])
    yield len([option for option in options if len(option) == min_length])





