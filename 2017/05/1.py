with open('input.txt') as f:
    instrs = [int(x.split('\n')[0]) for x in f.readlines()]

ip = 0
counter = 0
while 0<=ip<len(instrs):
    jump = instrs[ip]
    instrs[ip] = instrs[ip] + 1
    ip = ip + jump
    counter += 1

print(counter)
