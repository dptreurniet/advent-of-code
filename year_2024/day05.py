
def rule_applies(rule, update):
    A, B = map(int, rule.split('|'))
    return (A in update) and (B in update)

def rule_is_followed(rule, update):
    A, B = map(int, rule.split('|'))
    if not rule_applies(rule, update): return True
    return update.index(A) < update.index(B)

def swap_rule_pages(rule, update):
    A, B = map(int, rule.split('|'))
    update[update.index(A)] = B
    update[update.index(B)] = A
    return update


def fix_ordering(rules, update):
    for rule in rules:
        if not rule_is_followed(rule, update):
            return fix_ordering(rules, swap_rule_pages(rule, update))
    return update

def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]
    
    rules = [line for line in lines if '|' in line]
    updates = [list(map(int, line.split(','))) for line in lines if ',' in line]

    s = 0
    incorrect_updates = []
    for update in updates:
        if all([rule_is_followed(rule, update) for rule in rules]):
            s += update[len(update)//2]
        else: incorrect_updates.append(update)
    yield s

    # Part 2

    s = 0
    for update in incorrect_updates:
        rules_applying = [rule for rule in rules if rule_applies(rule, update)]
        update = fix_ordering(rules_applying, update)
        s += update[len(update)//2]
    yield s

