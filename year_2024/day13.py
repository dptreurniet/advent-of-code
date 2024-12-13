import sympy as sym

def cost(machines):
    cost = 0
    for machine in machines:
        nA, nB, xA, yA, xB, yB = sym.symbols('nA, nB, xA, yA, xB, yB')
        eq1 = xA - nA*machine[0][0]
        eq2 = yA - nA*machine[0][1]
        eq3 = xB - nB*machine[1][0]
        eq4 = yB - nB*machine[1][1]
        eq5 = xA + xB - machine[2][0]
        eq6 = yA + yB - machine[2][1]
        r = sym.linsolve([eq1, eq2, eq3, eq4, eq5, eq6], (nA, nB, xA, yA, xB, yB)).args[0]
        nA, nB = [int(x) if type(x) == sym.core.numbers.Integer else -1 for x in r.args[:2]]
        if nA >= 0 and nB >= 0: cost += nA*3 + nB
    return cost

def solve(data):
    with open(data) as f:
        lines = [line.strip() for line in f.readlines()]
    line_sets = [lines[i*4:i*4+3] for i in range((len(lines)+1)//4)]
    
    machines = []
    for line_set in line_sets:
        A = tuple(int(x) for x in line_set[0].replace('X','').replace('Y','').replace('+','').replace(',','').split()[-2:])
        B = tuple(int(x) for x in line_set[1].replace('X','').replace('Y','').replace('+','').replace(',','').split()[-2:])
        P = tuple(int(x) for x in line_set[2].replace('X=','').replace('Y=','').replace(',','').split()[-2:])
        machines.append((A, B, P))
        
    yield cost(machines)

    # Part 2

    new_machines = [(m[0], m[1], (m[2][0]+10000000000000, m[2][1]+10000000000000)) for m in machines]
    yield cost(new_machines)