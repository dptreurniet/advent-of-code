
def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]

    gift = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
    }

    sues = [{} for _ in range(len(lines))]
    for sue_i, sue in enumerate(lines):
        s = sue.split()[2:]
        for i in range(0, len(s), 2):
            k = s[i][:-1]
            v = int(s[i+1].replace(',',''))
            sues[sue_i][k] = v

    for sue_i, sue in enumerate(sues):
        for k, v in sue.items():
            if v != gift[k]: break
        else:
            yield sue_i + 1
            break
    
    # Part 2
    for sue_i, sue in enumerate(sues):
        for k, v in sue.items():
            if k in ['cats', 'trees']:
                if gift[k] >= v: break
            elif k in ['pomeranians', 'goldfish']:
                if gift[k] <= v: break
            else:
                if v != gift[k]: break
        else:
            yield sue_i + 1
            break
            
