
def step(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^(n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return n

def solve(data):
    with open(data) as f:
        ns = [int(line.strip()) for line in f.readlines()]
    
    t = 0
    for i, n in enumerate(ns):
        for _ in range(2000):
            n = step(n)
        t +=  n  
    yield t

    # Part 2

    prices = [[n,] for n in ns]
    changes = [[] for _ in range(len(prices))]
    for i in range(len(prices)):
        for _ in range(2000):
            prices[i].append(step(prices[i][-1]))
            changes[i].append(prices[i][-1]%10 - prices[i][-2]%10)
    
    X = []
    for price, change in zip(prices, changes):
        X.append({})
        for i in range(3, len(change)):
            key = ','.join(map(str, change[i-3:i+1]))
            if key not in X[-1]:
                X[-1][key] = price[i+1]%10

    keys = set([key for x in X for key in x.keys()])

    max_t =  0
    for p_i, p in enumerate(keys):
        print('{:.1f}%'.format(100*(p_i+1)/len(keys)), end='\r')
        t = 0
        for xx in X:
            try: t += xx[p]
            except KeyError: pass
        max_t = max(max_t, t)
    yield max_t