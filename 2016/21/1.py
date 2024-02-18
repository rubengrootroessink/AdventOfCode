import re

with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]

password = 'abcdefgh'
password = list(password)

swap_pos_patt = r'^swap position (\d+) with position (\d+)$'
swap_let_patt = r'^swap letter (\w) with letter (\w)$'
rot_steps_patt = r'^rotate (left|right) (\d+) steps?$'
rot_pos_let_patt = r'^rotate based on position of letter (\w)$'
rev_pos_patt = r'^reverse positions (\d+) through (\d+)$'
mov_pos_patt = r'^move position (\d+) to position (\d+)$'

for instr in instrs:

    # Swap positions
    matcher = re.match(swap_pos_patt, instr)
    if matcher:
        pos_a, pos_b = [int(x) for x in matcher.groups()]
        a, b = password[pos_a], password[pos_b]
        password[pos_a] = b
        password[pos_b] = a
        continue

    # Swap letters
    matcher = re.match(swap_let_patt, instr)
    if matcher:
        let_a, let_b = matcher.groups()
        pos_a = password.index(let_a)
        pos_b = password.index(let_b)
        password[pos_a] = let_b
        password[pos_b] = let_a
        continue

    # Rotate X steps
    matcher = re.match(rot_steps_patt, instr)
    if matcher:
        direction, nr_rots = matcher.groups()
        nr_rots = int(nr_rots)

        if direction == 'left' and nr_rots != 0:
            password = password[nr_rots:] + password[:nr_rots]
        elif direction == 'right' and nr_rots != 0:
            password = password[-nr_rots:] + password[:len(password)-nr_rots]
        continue
    
    # Rotate based on position of letter
    matcher = re.match(rot_pos_let_patt, instr)
    if matcher:
        let = matcher.groups()[0]
        nr_rots = password.index(let)
        nr_rots = nr_rots + 1 if nr_rots >= 4 else nr_rots
        nr_rots += 1
        nr_rots = nr_rots % len(password)
        if nr_rots != 0:
            password = password[-nr_rots:] + password[:len(password)-nr_rots]
        continue
    
    # Reverse sublist
    matcher = re.match(rev_pos_patt, instr)
    if matcher:
        pos_a, pos_b = [int(x) for x in matcher.groups()]
        password = password[:pos_a] + password[pos_a:pos_b+1][::-1] + password[pos_b+1:]
        continue

    # Move element
    matcher = re.match(mov_pos_patt, instr)
    if matcher:
        pos_a, pos_b = [int(x) for x in matcher.groups()]
        let_a = password[pos_a]
        password = password[:pos_a] + password[pos_a+1:]
        password = password[:pos_b] + [let_a] + password[pos_b:]
        continue

print(''.join(password))
