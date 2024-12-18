# Took inspiration from others
import re

with open('input.txt') as f:
    registers, instrs = f.read().strip().split('\n\n')

instrs = [int(x) for x in instrs.split(': ')[1].split(',')]

def calc(a):
    while True:
        b = (a % 8) ^ 7
        c = a // (2**b)
        yield (b ^ c ^ 4) % 8
        a = a // 8
        if a == 0:
            break

def eval_input(prog, prev=0):
    if prog == []:
        yield prev # TODO
        return # TODO

    for i in range(8):
        if next(calc(8*prev+i)) == prog[-1]:
            yield from eval_input(prog[:-1], 8*prev+i)

n = min(eval_input(instrs))
print(n)
