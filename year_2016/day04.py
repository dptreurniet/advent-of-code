
def get_top_5_letters(name):
    return ''.join([x[0] for x in sorted([(k, name.count(k)) for k in set(name.replace('-',''))], 
                                         key=lambda x: x[1]*'a'+'b'+x[0])[:5]])

def solve(data):
    with open(data) as f:
        room_lines = [line.strip() for line in f.readlines()]
    
    rooms = []
    for line in room_lines:
        parts = line.split('-')
        name = '-'.join(parts[:-1])
        id = int(parts[-1].split('[')[0])
        checksum = parts[-1].split('[')[-1][:-1]
        rooms.append((name, id, checksum))
    
    yield sum([room[1] if get_top_5_letters(room[0]) == room[2] else 0 for room in rooms])

    for name, id, _ in rooms:
        if 'north' in ''.join([chr((ord(n) - 97 + id)%26 + 97) if n != '-' else ' ' for n in name]): yield id