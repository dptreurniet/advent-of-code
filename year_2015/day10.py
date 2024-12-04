
def look_and_say(n):

    l = 1
    last_d = n[0]
    res = ''
    for d in n[1:]:
        if d == last_d:
            l += 1
        else:
            res += f'{l}{last_d}'
            last_d = d
            l = 1
    res += f'{l}{last_d}'
            
    return res

def solve(data):
    
    with open(data) as f:
        start = f.readline().strip()
    
    n = start
    n_cycles = 40
    for _ in range(n_cycles):
        n = look_and_say(n)
    
    yield len(n)

    # Part 2

    n = start
    n_cycles = 50
    for _ in range(n_cycles):
        n = look_and_say(n)
    
    yield len(n)


