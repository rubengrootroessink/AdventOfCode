import math
import copy
import heapq

def walkthrough(input_dict, watch, final_mod):
    cycles = {val: [] for val in watch}

    s_dict = copy.deepcopy(input_dict)

    i = -1
    while True:
        i += 1

        heap = [('button', 'broadcaster', False)]

        while heap:

            inpt, mod, pulse_val = heapq.heappop(heap)
    
            if not mod in module_dict.keys():
                continue

            mod_type = module_dict[mod]['type']
            mod_dsts = module_dict[mod]['dsts']
            
            if mod in watch and pulse_val == False:
                if (mod_type == 'cj' and all([value == True for value in list(s_dict[mod].values())])) or (mod_type == 'ff' and s_dict[mod]):
                    cycles[mod].append(i)
                    if all([len(v) >= 2 for k, v in cycles.items()]):
                        return cycles
        
            if mod_type == 'bc':
                for dst in mod_dsts:
                    heapq.heappush(heap, ('broadcaster', dst, pulse_val))

            elif mod_type == 'ff':

                if not pulse_val: # Low pulse
                    off = s_dict[mod]
                    s_dict[mod] = not off
                    new_pulse_val = True if not off else False 
                    for dst in mod_dsts:
                        heap.append((mod, dst, new_pulse_val))

            elif mod_type == 'cj':
                s_dict[mod][inpt] = pulse_val
                new_pulse_val = True
                if all([v == True for k, v in s_dict[mod].items()]):
                    new_pulse_val = False

                for dst in mod_dsts:
                    heap.append((mod, dst, new_pulse_val))

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

output_mod = 'rx'
final_cj_mod = None

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
    if output_mod in v1['dsts']:
        final_cj_mod = k1
    if v1['type'] == 'cj':
        for k2, v2 in module_dict.items():
            if k1 in v2['dsts']:
                state_dict[k1][k2] = False

final_input_mods = list(state_dict[final_cj_mod].keys())

result = [v[1]-v[0] for k, v in walkthrough(state_dict, final_input_mods, final_cj_mod).items()]

lcm = result[0]
for val in result[1:]:
    lcm = lcm*val // math.gcd(lcm, val)

print(lcm)
