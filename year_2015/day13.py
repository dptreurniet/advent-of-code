import itertools

def happiness_score(ordering, scores):
    t = 0
    for i, p1 in enumerate(ordering):
        p2 = ordering[(i+1)%len(ordering)]
        t += scores[p1][p2]
        p3 = ordering[(i-1)%len(ordering)]
        t += scores[p1][p3]
    return t


def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]

    scores = {}
    people = set()
    for line in lines:
        line_split = line.split()
        p1 = line_split[0]
        people.add(p1)
        multiplier = -1 if line_split[2] == 'lose' else 1
        h = multiplier * int(line_split[3])
        p2 = line_split[-1][:-1]

        try:
            scores[p1][p2] = h
        except KeyError:
            scores[p1] = {p2: h}    
    people = list(people)

    yield max([happiness_score(ordering, scores) for ordering in itertools.permutations(people)])

    # Part 2

    for p in people: scores[p]['me'] = 0
    scores['me'] = {p: 0 for p in people}
    people.append('me')
    yield max([happiness_score(ordering, scores) for ordering in itertools.permutations(people)])
