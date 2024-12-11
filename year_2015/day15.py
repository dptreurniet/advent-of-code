from functools import reduce
from operator import mul

def get_score(ingredients, spoons):
    score = [0 for _ in range(len(ingredients[0]))]
    for spoon_i, spoons in enumerate(spoons):
        ing_score = [i * spoons for i in ingredients[spoon_i][:-1]]
        score = [sum(x) for x in zip(ing_score, score)]
    return reduce(mul, score)

def calories(ingredients, spoons):
    return sum([s*ingredients[s_i][-1] for s_i, s in enumerate(spoons)])

def solve(data):
    with open(data) as f:
        ingredients = [[int(v.replace(',',''))
                for i, v in enumerate(line.strip().split()) if i in [2,4,6,8,10]]
                for line in f.readlines()]
    
        total = 100
       
        # Start with equal parts
        spoons = [100 // len(ingredients) for _ in range(len(ingredients))]
        spoons[-1] += total - sum(spoons)

        while True:
            # Try changing 1 spoon from one ingredient to another.
            # If the score improves, repeat. If the score does not increase, optimum reached.
            score_increased = False
            current_score = get_score(ingredients, spoons)
            for i in range(len(spoons)):
                for j in range(len(spoons)):
                    if i == j: continue
                    if spoons[i] == 0: continue
                    try_spoons =  spoons[:]
                    try_spoons[i] -= 1
                    try_spoons[j] += 1
                    if get_score(ingredients, try_spoons) > current_score:
                        spoons = try_spoons[:]
                        score_increased = True
                        break
                if score_increased: break
            if not score_increased: break

    yield current_score

    # Part 2
    
    options = [(i,j,k,100-i-j-k)
                      for i in range(101)
                      for j in range(101-i)
                      for k in range(101-i-j)
                      if calories(ingredients, (i,j,k,100-i-j-k)) == 500]

    high_score = (0,)
    for spoons in options:
        if (score := get_score(ingredients, spoons)) > high_score[0]:
            high_score = (score, spoons)
    yield high_score[0]



