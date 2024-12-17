
def run(A, B, C, program, compare_output = []):
    output = []
    i = 0
    while i < len(program):

        if compare_output:
            if compare_output[:len(output)] != output:
                return output

        cmd = program[i]
        lit_op = program[i+1]
        comb_op = program[i+1]
        if comb_op == 4: comb_op = A
        elif comb_op == 5: comb_op = B
        elif comb_op == 6: comb_op = C

        if cmd == 0:
            A = A // (2**comb_op)
            i += 2
            continue
            
        if cmd == 1:
            B = B ^ lit_op
            i += 2
            continue

        if cmd == 2:
            B = comb_op % 8
            i += 2
            continue
    
        if cmd == 3:
            if A == 0:
                i += 2
                continue
            else:
                i = lit_op
                continue
    
        if cmd == 4:
            B = B ^ C
            i += 2
            continue

        if cmd == 5:
            output.append(comb_op%8)
            i += 2
            continue

        if cmd == 6:
            B = A // (2**comb_op)
            i += 2
            continue

        if cmd == 7:
            C = A // (2**comb_op)
            i += 2
            continue

    return output


def solve(data):
    with open(data) as f:
        A, B, C = [int(f.readline().strip().split()[-1]) for _ in range(3)]
        f.readline()
        ops = list(map(int, f.readline().strip().split()[-1].split(',')))

    yield ','.join(map(str, run(A, B, C, ops)))

    min_A = 0
    max_A = 0
    stepsize = 1
    count = 0
    last_lengths = set()
    while True:
        res = run(max_A, B, C, ops)
        if (L := len(res)) == len(ops) and min_A == 0: min_A = max_A - stepsize
        if (L := len(res)) > len(ops): break
        last_lengths.add(L)
        count += 1
        if count == 100:
            if len(last_lengths) == 1: stepsize *= 10
            last_lengths.clear()
            count = 0
            continue
        max_A += stepsize
    
    ranges = [(min_A, max_A)]
    checking_digits = 1
    min_found = max_A

    for _ in range(len(ops)):
        new_ranges = []
        for r in ranges:
            in_range = False
            stepsize = max((r[1] - r[0]) // 1000, 1)
            for A in range(r[0], r[1], stepsize):
                res = run(A, B, C, ops)
                if len(res) != len(ops): continue

                if res == ops:
                    min_found = min([min_found, A])
                    
                
                if res[-checking_digits:] == ops[-checking_digits:]:
                    if not in_range:
                        r_start = A - stepsize
                        in_range = True
                else:
                    if in_range:
                        in_range = False
                        new_ranges.append((r_start, A))
        ranges = new_ranges[:]
        checking_digits += 1
    yield min_found
                    
