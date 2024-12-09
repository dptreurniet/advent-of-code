from itertools import combinations

weapons = [
    ('dagger',      8,  4,  0),
    ('shortsword',  10, 5,  0),
    ('warhammer',   25, 6,  0),
    ('longsword',   40, 7,  0),
    ('greataxe',    74, 8,  0),]

armors = [
    ('leather',     13, 0, 1),
    ('chainmail',   31, 0, 2),
    ('splintmail',  53, 0, 3),
    ('bandedmail',  75, 0, 4),
    ('platemail',   102,0, 5)]

rings = [
    ('damage1', 25, 1, 0),
    ('damage2', 50, 2, 0),
    ('damage3', 100, 3, 0),
    ('defense1', 20, 0, 1),
    ('defense2', 40, 0, 2),
    ('defense3', 80, 0, 3)]

def player_wins(stats, boss_hp, boss_damage, boss_armor):
    bhp = boss_hp
    bd = boss_damage
    ba = boss_armor

    php = 100
    pd = stats[1]
    pa = stats[2]

    player_turn = True
    while php > 0 and bhp > 0:
        if player_turn:
            bhp -= (pd - ba)
        else:
            php -= (bd - pa)
        player_turn = not player_turn
    return bhp <= 0

def solve(data):

    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]

    bhp, bd, ba = 0, 0, 0
    for line in lines:
        stat, val = [l.strip() for l in line.split(':')]
        if stat == 'Hit Points': bhp = int(val)
        if stat == 'Damage': bd = int(val)
        if stat == 'Armor': ba = int(val)

    ring_combs = rings[:]
    ring_combs.extend(list(combinations(rings, 2)))

    loadouts = []
    for w in weapons:
        loadouts.append((w,))
        for r in ring_combs:
            if len(r) == 2: loadouts.append((w, *r))
            else: loadouts.append((w, r))
            for a in armors:
                if len(r) == 2: loadouts.append((w, *r, a))
                else: loadouts.append((w, r, a))
    
    stats = []
    for L in loadouts:
        cost = sum([i[1] for i in L])
        damage = sum([i[2] for i in L])
        armor = sum([i[3] for i in L])
        stats.append((cost, damage, armor))

    for stat in sorted(stats, key=lambda s: s[0]):
        if player_wins(stat, bhp, bd, ba):
            yield stat[0]
            break

    for stat in sorted(stats, key=lambda s: 1/s[0]):
        if not player_wins(stat, bhp, bd, ba):
            yield stat[0]
            break
