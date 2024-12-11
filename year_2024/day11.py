
def blink(stones):
    new_stones = []
    for i in range(len(stones)):
        if stones[i][0] == 0:
            new_stones.append((1, stones[i][1]))
        elif len(stone_str:=str(stones[i][0]))%2 == 0:
            new_stones.append((int(stone_str[len(stone_str)//2:]), stones[i][1]))
            new_stones.append((int(stone_str[:len(stone_str)//2]), stones[i][1]))
        else:
            new_stones.append((stones[i][0]*2024, stones[i][1]))
    
    values = set()
    for stone in new_stones: values.add(stone[0])
    return [(s, sum([n for v,n in new_stones if v == s])) for s in values]


def solve(data):
    with open(data) as f:
        stones = list(map(int, f.readline().split()))
    stones = list(set([(stone, stones.count(stone)) for stone in stones]))
    
    for i in range(75):
        stones = blink(stones)
        print('{:.0f}%'.format(100*(i+1)/75), end='\r')
        if i == 24: yield sum([n for v,n in stones])
    yield sum([n for v,n in stones])