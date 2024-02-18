with open('input.txt') as f:
    layer_dict = {x: y for (x, y) in [tuple(map(int, x.strip().split(': '))) for x in f.readlines()]}

sev = 0
for depth in layer_dict.keys():
    rng = layer_dict[depth]
    period_length = 2*rng - 2
    if depth % period_length == 0:
        sev += depth * rng

print(sev)
