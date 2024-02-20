import heapq
import copy

def run(prog_instrs, input_vars):
    prog = copy.deepcopy(prog_instrs)
    
    input_data = input_vars
    eip = 0

    finished = False
    while not finished:
        instr = prog[eip]

        op_code = instr % 100
        
        mode_param_3 = instr // 10000
        mode_param_2 = (instr // 1000) % 10
        mode_param_1 = (instr // 100) % 10

        match op_code:
            case 1 | 2 | 7 | 8: # Add, multiply, less than, equals
                param_1, param_2, param_3 = prog[eip+1:eip+4]

                param_1 = param_1 if mode_param_1 == 1 else prog[param_1]
                param_2 = param_2 if mode_param_2 == 1 else prog[param_2]

                match op_code:
                    case 1:
                        prog[param_3] = param_1 + param_2
                    case 2:
                        prog[param_3] = param_1 * param_2
                    case 7:
                        prog[param_3] = 1 if param_1 < param_2 else 0
                    case 8:
                        prog[param_3] = 1 if param_1 == param_2 else 0
                
                eip += 4

            case 3 | 4: # Input or output
                param_1 = prog[eip+1]

                if op_code == 3:
                    next_val = heapq.heappop(input_data)
                    prog[param_1] = next_val
                else:
                    output = param_1 if mode_param_1 == 1 else prog[param_1]
                    print(output)

                eip += 2

            case 5 | 6: # Jump if (true|false)
                param_1, param_2 = prog[eip+1:eip+3]
                
                param_1 = param_1 if mode_param_1 == 1 else prog[param_1]
                param_2 = param_2 if mode_param_2 == 1 else prog[param_2]

                if (op_code == 5 and param_1 != 0) or (op_code == 6 and param_1 == 0):
                    eip = param_2
                else:
                    eip += 3

            case 99:
                finished = True

with open('input.txt') as f:
    prog = [int(x) for x in f.read().strip().split(',')]

run(prog, [5])
