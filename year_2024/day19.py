
def word_break(target, dictionary):
    n = len(target)
    dp = [1] + [0 for _ in range(n)]
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and target[j:i] in dictionary:
                dp[i] += dp[j]
    return dp[-1]

def solve(data):
    with open(data) as f:
        towels = set(f.readline().strip().split(', '))
        f.readline()
        patterns = [line.strip() for line in f.readlines()]

    combinations = [word_break(pattern, towels) for pattern in patterns]
    yield len(list(filter(lambda x: x > 0, combinations)))
    yield sum(combinations)
