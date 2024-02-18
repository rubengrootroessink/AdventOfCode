with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

start_node = None
rocks = set()
for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column == '#':
            rocks.add((x, y))
        elif column == 'S':
            start_node = (x, y)

prev_reachable = set([start_node])

nr_steps = 64
for i in range(nr_steps):
    reachable = set()
    for pr in prev_reachable:
        neighbours = [
            (pr[0]-1, pr[1]), (pr[0]+1, pr[1]), 
            (pr[0], pr[1]-1), (pr[0], pr[1]+1)
        ]
        for n in neighbours:
            if not n in rocks:
                reachable.add(n)

    prev_reachable = reachable

print(len(prev_reachable))
