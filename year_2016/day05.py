import hashlib

def solve(data):
    with open(data) as f:
        ID = f.readline().strip()
    
    code = ''
    i = 0
    print('\t'+'_'*8, end='\r')
    while len(code) < 8:
        if (hash := hashlib.md5((ID+str(i)).encode()).hexdigest())[:5] == '00000':
            code += hash[5]
            print(f'\t{code}{'_'*(8-len(code))}', end='\r')
        i += 1
    yield code

    code = ['_' for _ in range(8)]
    i = 0
    print('\t'+'_'*8, end='\r')
    while '_' in code:
        if (hash := hashlib.md5((ID+str(i)).encode()).hexdigest())[:5] == '00000':
            if hash[5] in '01234567':
                if code[int(hash[5])] == '_':
                    code[int(hash[5])] = hash[6]
                    print(f'\t{''.join(code)}', end='\r')
        i += 1
    yield ''.join(code)
