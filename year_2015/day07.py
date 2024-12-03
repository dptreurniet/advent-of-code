ops = ['NOT', 'AND', 'OR', 'RSHIFT', 'LSHIFT']

def str_to_val(vars, s):
    if s.isnumeric(): return int(s)
    return vars[s]

def solve_circuit(vars, circuit):
    while not all([type(v) == int for v in vars.values()]):
        for line in circuit:
            lhs, rhs = line.split(' -> ')
        
            if lhs.isnumeric():
                vars[rhs] = int(lhs)
                continue
        
            lhs_elems = lhs.split()
            try:
                op = [op for op in lhs_elems if op in ops][0]
                ins = [str_to_val(vars, elem) for elem in lhs_elems if elem != op]
                if all([type(v) == int for v in ins]):
                    if op == 'NOT': vars[rhs] = ~ins[0]
                    if op == 'AND': vars[rhs] = ins[0] & ins[1]
                    if op == 'OR': vars[rhs] = ins[0] | ins[1]
                    if op == 'RSHIFT': vars[rhs] = ins[0] >> ins[1]
                    if op == 'LSHIFT': vars[rhs] = ins[0] << ins[1]
            except IndexError:
                if type(vars[lhs]) == int: vars[rhs] = vars[lhs]
    return convert_signed_to_unsigned(vars)

def convert_signed_to_unsigned(vars):
    return {k: v+2**16 if v < 0 else v for k, v in vars.items()}

def solve(data):
    with open(data) as f:
        circuit = [line.strip() for line in f.readlines()]

    vars = {}
    for line in circuit:
        words = line.split()
        for word in words:
            if word.islower() and word not in vars.keys():
                vars[word] = '?'
    
    vars = solve_circuit(vars, circuit)
    result = vars['a']
    
    yield result

    # Part 2

    vars = {k: '?' for k in vars.keys()}
    vars['b'] = result
    circuit = [line for line in circuit if line[-4:] != '-> b']

    yield solve_circuit(vars, circuit)['a']


    