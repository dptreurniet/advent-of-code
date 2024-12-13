import dataclasses

@dataclasses.dataclass
class GameState():
    boss_hp: int
    boss_damage: int
    hp: int = 50
    mana: int = 500
    armor: int = 0
    shield_timer: int = 0
    poison_timer: int = 0
    recharge_timer: int = 0
    players_turn: bool = True
    mana_spent: int = 0

spell_cost = {
    'magic_missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229
}

def tick(state: GameState, next_spell, history = [], hard_mode = False):
    if state.mana_spent > min_mana: return

    if hard_mode and state.players_turn:
        state.hp -= 1
        if state.hp <= 0:
            yield state, history + ['Player dead']
            return

    # Apply effects and reduce their timers
    if state.shield_timer > 0:
        state.armor = 7
        state.shield_timer -= 1
    else:
        state.armor = 0

    if state.poison_timer > 0:
        state.boss_hp -= 3
        state.poison_timer -= 1
        
    if state.recharge_timer > 0:
        state.mana += 101
        state.recharge_timer -= 1

    # Check if boss is dead
    if state.boss_hp <= 0:
        yield state, history + ['Boss dead']
        return

    # If players turn, cast spell
    if state.players_turn:
        # Check if next spell does not cast an effect that is active
        if next_spell == 'shield' and state.shield_timer > 0: return
        if next_spell == 'poison' and state.poison_timer > 0: return
        if next_spell == 'recharge' and state.recharge_timer > 0: return

        if state.mana < spell_cost[next_spell]: return
        state.mana -= spell_cost[next_spell]
        state.mana_spent += spell_cost[next_spell]
        if next_spell == 'magic_missile':
            state.boss_hp -= 4
        elif next_spell == 'drain':
            state.boss_hp -= 2
            state.hp += 2
        elif next_spell == 'shield':
            state.shield_timer = 6
            state.armor = 7
        elif next_spell == 'poison':
            state.poison_timer = 6
        elif next_spell == 'recharge':
            state.recharge_timer = 5
    
    # Else, boss attacks
    else:
        state.hp -= state.boss_damage - state.armor

    # Check if player or boss is dead
    if state.hp <= 0:
        yield state, history + ['Player dead']
        return
    if state.boss_hp <= 0:
        yield state, history + ['Boss dead']
        return

    # If this point is reached, next tick
    state.players_turn = not state.players_turn
    if not state.players_turn: yield from tick(dataclasses.replace(state), next_spell, history + [(state, 'boss turn')], hard_mode=hard_mode)
    else:
        for spell in spell_cost.keys():
            yield from tick(dataclasses.replace(state), spell, history + [(state, spell)], hard_mode=hard_mode)

def solve(data):
    
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]
    
    state = GameState(boss_hp=int(lines[0].split()[-1]),
                      boss_damage=int(lines[1].split()[-1]))

    global min_mana
    min_mana = 1000000
    for spell in spell_cost.keys():
        for last_state, history in tick(dataclasses.replace(state), spell, history=[(state, spell)]):
            if history[-1] == 'Boss dead':
                min_mana = min(min_mana, last_state.mana_spent)
    yield min_mana

    # Part 2

    min_mana = 1000000
    for spell in spell_cost.keys():
        for last_state, history in tick(dataclasses.replace(state), spell, history=[(state, spell)], hard_mode=True):
            if history[-1] == 'Boss dead':
                min_mana = min(min_mana, last_state.mana_spent)
    yield min_mana