from collections import defaultdict
import re

begin_patt = r'^Begin in state (\w+)\.$'
checksum_patt = r'^Perform a diagnostic checksum after (\d+) steps\.$'

name_patt = r'^In state (\w+)\:$'
cmp_patt = r'^If the current value is (\d+)\:$'
write_patt = r'^- Write the value (\d+)\.$'
move_patt = r'^- Move one slot to the (\w+)\.$'
n_state_patt = r'^- Continue with state (\w+)\.$'

def parse_state(state):
    s_state = [x.strip() for x in state.split('\n')]

    name = re.match(name_patt, s_state[0]).groups()[0]

    ret_val = []
    for i in [1, 5]:
        block = s_state[i:i+4]
        #cmp_val = int(re.match(cmp_patt, block[0]).groups()[0])
        write_val = int(re.match(write_patt, block[1]).groups()[0])
        move_val = re.match(move_patt, block[2]).groups()[0]
        n_state_val = re.match(n_state_patt, block[3]).groups()[0]

        ret_val.append((write_val, move_val, n_state_val))

    return (name, ret_val)

with open('input.txt') as f:
    data = f.read()[:-1].split('\n\n')

instrs, states = data[0], data[1:]

begin_state, diagnostic = instrs.split('\n')
begin_state = re.match(begin_patt, begin_state).groups()[0]
diagnostic = int(re.match(checksum_patt, diagnostic).groups()[0])

state_dict = {}
for state in states:
    name, ret_val = parse_state(state)
    state_dict[name] = ret_val

tape = defaultdict(int)

curr_state = begin_state
curr_index = 0

count = 0

for i in range(0, diagnostic):
    curr_val = tape[curr_index]
    state = state_dict[curr_state]

    write_val, move_val, n_state_val = state[curr_val]

    if curr_val == 0 and write_val == 1:
        count += 1
    elif curr_val == 1 and write_val == 0:
        count -= 1

    tape[curr_index] = write_val
    curr_index += 1 if move_val == 'right' else -1
    curr_state = n_state_val

print(count)
