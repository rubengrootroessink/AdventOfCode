from collections import defaultdict
import heapq
import copy

l_mode_dict = {
    0: lambda a, b, c: a,
    1: lambda a, b, c: a,
    2: lambda a, b, c: a+b
}

i_mode_dict = {
    0: lambda a, b, c: c[a],
    1: lambda a, b, c: a,
    2: lambda a, b, c: c[a+b]
}

def param_mode(mode, param, rel_base, prog, literal=False):
    if literal:
        return l_mode_dict[mode](param, rel_base, prog)
    else:
        return i_mode_dict[mode](param, rel_base, prog)

def run(prog_instrs, input_vars):
    prog = copy.deepcopy(prog_instrs)
    
    input_data = input_vars
    eip = 0
    rel_base = 0

    finished = False
    while not finished:
        instr = prog[eip]

        op_code = instr % 100
        
        num_params = 0
        param_mask = []

        match op_code:
            case 1 | 2 | 7 | 8: # Add, multiply, less than, equals
                num_params = 3
                param_mask = [False, False, True]
            
            case 3 | 4 | 9: # Input, output, changing relative base
                num_params = 1
                param_mask = [True] if op_code == 3 else [False]
            
            case 5 | 6: # Jump if (true|false)
                num_params = 2
                param_mask = [False, False]

            case 99: # Program end
                num_params = 0
                param_mask = []

        param_modes = [(instr // (100*10**i)) % 10 for i in range(num_params)]
        params = [prog[x] for x in range(eip+1, eip+1+num_params)]

        parameters = [param_mode(param_modes[i], params[i], rel_base, prog, literal=param_mask[i]) for i in range(num_params)]

        match op_code:
            case 1 | 2 | 7 | 8: # Add, multiply, less than, equals
                
                match op_code:
                    case 1:
                        prog[parameters[2]] = parameters[0] + parameters[1]
                    case 2:
                        prog[parameters[2]] = parameters[0] * parameters[1]
                    case 7:
                        prog[parameters[2]] = 1 if parameters[0] < parameters[1] else 0
                    case 8:
                        prog[parameters[2]] = 1 if parameters[0] == parameters[1] else 0
                
                eip += 4

            case 3 | 4: # Input or output
                if op_code == 3:
                    next_val = heapq.heappop(input_data)
                    prog[parameters[0]] = next_val
                else:
                    print(parameters[0])

                eip += 2

            case 5 | 6: # Jump if (true|false)
                if (op_code == 5 and parameters[0] != 0) or (op_code == 6 and parameters[0] == 0):
                    eip = parameters[1]
                else:
                    eip += 3

            case 9: # Change relative base
                rel_base += parameters[0]
                eip += 2

            case 99: # Exit program
                finished = True

with open('input.txt') as f:
    prog = [int(x) for x in f.read().strip().split(',')]

    prog_dict = defaultdict(int)
    for i, instr in enumerate(prog):
        prog_dict[i] = instr

run(prog_dict, [2])
