# Inspired by others

def solve(nr_steps):
    prev_reachable = set([start_node])
    
    for i in range(nr_steps):
        reachable = set()
        for pr in prev_reachable:
            neighbours = [
                (pr[0]-1, pr[1]), (pr[0]+1, pr[1]), 
                (pr[0], pr[1]-1), (pr[0], pr[1]+1)
            ]
            for n in neighbours:
                if not (n[0]%max_x, n[1]%max_y) in rocks:
                    reachable.add(n)

        prev_reachable = reachable
    return len(prev_reachable)

with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

max_x = len(data[0])
max_y = len(data)

start_node = None
rocks = set()
for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column == '#':
            rocks.add((x, y))
        elif column == 'S':
            start_node = (x, y)

steps = 26501365
remainder = steps % max_x

f_n = solve(remainder) # f(n)
f_n_x = solve(remainder + max_x) # f(n+X)
f_n_2x = solve(remainder + 2*max_x) # f(n+2x)

a = (f_n - 2 * f_n_x + f_n_2x) / 2
b = (-3 * f_n + 4 * f_n_x - f_n_2x) / 2
c = f_n
n = steps // max_x

print(int(a*(n**2) + b*n + c))
