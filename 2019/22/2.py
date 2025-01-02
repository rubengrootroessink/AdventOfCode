# Inspired by others
nr_cards = 119315717514047
nr_shuffles = 101741582076661

def deal(i):
    return nr_cards-1-i

def cut(i, amount):
    return (i+amount+nr_cards)

def inc(i, increment):
    return pow(increment, -1, nr_cards) * i

def rev_function(instrs, i):
    loc = i
    for instr in instrs[::-1]:
        if instr.startswith('deal into new stack'):
            loc = deal(loc)
        elif instr.startswith('cut'):
            amount = int(instr.split(' ')[-1])
            loc = cut(loc, amount)
        elif instr.startswith('deal with increment'):
            increment = int(instr.split(' ')[-1])
            loc = inc(loc, increment)
    return loc

with open('input.txt') as f:
    instrs = [x.strip() for x in f.readlines()]

# Linear equations, so we need two equations:
# - e.g. a*x+b=y and a*y+b=z
x = 2020
y = rev_function(instrs, x)
z = rev_function(instrs, y)

# Simplify equations to:
# - a*(x-y)=y-z --> a = (x-z)/(x-y) (substracting equation 1 from 2)
# - b=y-a*x
a = (y-z) * pow(x-y, -1, nr_cards)
b = (y-a*x) % nr_cards

print((pow(a, nr_shuffles, nr_cards)*x + (pow(a, nr_shuffles, nr_cards)-1) * pow(a-1, -1, nr_cards) * b) % nr_cards)
