with open('input.txt') as f:
    instrs = [x.split('\n')[0] for x in f.readlines()]

board = set()

for instr in instrs:
    if instr.startswith('rect'):
        a,b = instr.split('x')
        a = a.split(' ')[1]
        a,b = int(a), int(b)

        for i in range(0, a):
            for j in range(0, b):
                board.add((i,j))
    
    elif instr.startswith('rotate'):
        val, shifts = instr.split(' by ')
        val = val.split('=')[1]
        val, shifts = int(val), int(shifts)

        col = 'column' in instr
        
        if col:
            matching_keys = [(x, y) for x, y in list(board) if x == val]

            for k in matching_keys:
                board.remove(k)

            for k in matching_keys:
                board.add((k[0], (k[1] + shifts) % 6))

        else:
            matching_keys = [(x, y) for x, y in list(board) if y == val]

            for k in matching_keys:
                board.remove(k)

            for k in matching_keys:
                board.add(((k[0] + shifts) % 50, k[1]))

print(len(board))
