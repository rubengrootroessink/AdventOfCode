# Chinese Remainder theorem from:
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n,a):
        p = prod // n_i # Modified to return an int
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
    
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0,1
    if b == 1: return 1
    while a > 1 :
        q = a // b
        a, b= b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0 : x1 += b0
    return x1

with open('input.txt', 'r') as file:
    timestamp = int(file.readline())
    busses = [int(bus) if bus != 'x' else bus for bus in file.readline().split(',')]
    
    # x mod 7 = 0 ==> 7
    # x mod 13 = -1 ==> 12
    # x mod 'x' = X
    # x mod 'x'= X
    # x mod 59 = -4 ==> 55
    # x mod 'x' = X
    # x mod 31 = -6 ==> 25
    # x mod 19 = -7 ==> 12
    
    mods = []
    remainders = []
    for i, bus in enumerate(busses):
        if bus != 'x':
            mods.append(bus)
            remainders.append(-i + bus)
            
    print(chinese_remainder(mods, remainders))
    


