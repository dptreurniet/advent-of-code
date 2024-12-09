

def solve(data):
    with open(data) as f:
        seq = f.readline().strip()

    memory = []
    space = False
    i = 0
    for c in seq:
        if space:
            memory.extend(['.' for _ in range(int(c))])
        else:
            memory.extend([i for _ in range(int(c))])
            i += 1
        space = not space
    original_memory = memory[:]

    with open('test.txt', 'w') as f:
        f.write(''.join([str(m) for m in original_memory]))
    
    in_space = False
    space_size = 0
    for i in range(len(memory)):
        m = memory[i]
        if m == '.':
            in_space = True
            space_size += 1
        else:
            if in_space:
                n_shifted = 0
                j = len(memory) - 1
                while n_shifted != space_size:
                    if memory[j] != '.':
                        memory[i - space_size + n_shifted] = memory[j]
                        memory[j] = '.'
                        n_shifted += 1
                    j -= 1
                i -= 1

            in_space = False
            space_size = 0

    yield sum([i*int(m) for i,m in enumerate(memory) if m != '.'])

    # Part 2
    
    moved_files = set()
    memory = original_memory[:]
    last_file = memory[-1]
    file_start = len(memory)-1
    stop = False
    for i in range(len(memory)-1, -1, -1):
        if stop: break
        file_id = memory[i]
        if file_id != last_file:
            file_size = file_start - i
            if last_file != '.':
                gap = ('._' * file_size)[:-1]
                mem_str = '_'.join([str(m) for m in memory])
                gap_i = mem_str.find(gap)
                gap_i = mem_str[:gap_i].count('_')
                if (gap_i < 0 or gap_i > file_start) and file_size == 1: stop = True
                if gap_i >= 0 and gap_i < file_start and last_file not in moved_files:
                    moved_files.add(last_file)
                    print(f'--> moving file {last_file} of size {file_size} to index {gap_i}')
                    A = memory[:gap_i]
                    B = [last_file for _ in range(file_size)]
                    C = memory[gap_i + file_size:file_start-file_size+1]
                    D = ['.' for _ in range(file_size)]
                    E = memory[file_start+1:]
                    memory = [*A, *B, *C, *D, *E]

            last_file = file_id
            file_start = i
            
    yield sum([i*int(m) for i,m in enumerate(memory) if m != '.'])

