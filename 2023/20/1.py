import heapq

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

module_dict = {}
state_dict = {}

flipflops = [x[1:].split(' -> ') for x in data if x.startswith('%')]
for f in flipflops:
    dsts = f[1].split(', ')
    module_dict[f[0]] = {'dsts': dsts, 'type': 'ff'}
    state_dict[f[0]] = False

conjunctions = [x[1:].split(' -> ') for x in data if x.startswith('&')]
for c in conjunctions:
    dsts = c[1].split(', ')
    module_dict[c[0]] = {'dsts': dsts, 'type': 'cj'}
    state_dict[c[0]] = {}

broadcaster = [x for x in data if x.startswith('broadcaster')][0].split('-> ')[1].split(', ')
module_dict['broadcaster'] = {'dsts': broadcaster, 'type': 'bc'}

for k1, v1 in module_dict.items():
    if v1['type'] == 'cj':
        for k2, v2 in module_dict.items():
            if k1 in v2['dsts']:
                state_dict[k1][k2] = 'low'

high_p, low_p = 0, 0
for i in range(1000):

    heap = [('button', 'broadcaster', 'low')]

    while heap:
        inpt, mod, pulse_val = heapq.heappop(heap)

        if pulse_val == 'high':
            high_p += 1
        else:
            low_p += 1

        if not mod in module_dict.keys():
            continue

        mod_type = module_dict[mod]['type']
        mod_dsts = module_dict[mod]['dsts']
        
        if mod_type == 'bc':
            for dst in mod_dsts:
                heapq.heappush(heap, ('broadcaster', dst, pulse_val))
        elif mod_type == 'ff':
            if pulse_val == 'high':
                pass
            elif pulse_val == 'low':
                off = state_dict[mod]
                state_dict[mod] = not off
                new_pulse_val = 'high' if not off else 'low' 
                for dst in mod_dsts:
                    heapq.heappush(heap, (mod, dst, new_pulse_val))
        elif mod_type == 'cj':
            state_dict[mod][inpt] = pulse_val
            new_pulse_val = 'high'
            if all([v == 'high' for k, v in state_dict[mod].items()]):
                new_pulse_val = 'low'
            
            for dst in mod_dsts:
                heapq.heappush(heap, (mod, dst, new_pulse_val))
            
print(high_p*low_p)
