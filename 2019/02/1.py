import copy

def run(prog_instrs, noun, verb):
    prog = copy.deepcopy(prog_instrs)
    prog[1] = noun
    prog[2] = verb

    eip = 0

    finished = False
    while not finished:
        op_code = prog[eip]

        match op_code:
            case 1:
                input_1, input_2, output = prog[eip+1:eip+4]
                prog[output] = prog[input_1] + prog[input_2]
                eip += 4

            case 2:
                input_1, input_2, output = prog[eip+1:eip+4]
                prog[output] = prog[input_1] * prog[input_2]
                eip += 4

            case 99:
                finished = True

    print(prog[0])

with open('input.txt') as f:
    prog = [int(x) for x in f.read().strip().split(',')]

run(prog, 12, 2)
