
def words_in_all_dirs(grid, start):
    steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for step in steps:
        word = ''
        coords = []
        for i in range(4):
            x = start[0]+step[0]*i
            y = start[1]+step[1]*i
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid): continue
            coords.append((x, y))
            word += grid[y][x]
        if len(word) == 4:
            yield (word, coords)

def cross_pair(grid, start):
    if not (1 <= start[0] <= len(grid)-2): return []
    if not (1 <= start[1] <= len(grid)-2): return []
    x, y = start
    return [grid[y-1][x-1] + grid[y][x] + grid[y+1][x+1],
            grid[y-1][x+1] + grid[y][x] + grid[y+1][x-1]]

def solve(data):
    with open(data) as f:
        grid = [line.strip() for line in f.readlines()]
    
    hits = []
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            for word in words_in_all_dirs(grid, (x, y)):
                if word[0] ==  'XMAS': hits.append(word)

    yield len(hits)

    # Part 2
    s = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            words = cross_pair(grid, (x, y))
            if all([word in ['MAS', 'SAM'] for word in words]) and len(words) == 2:
                s += 1
    yield s




