from collections import Counter

with open('input.txt') as f:
    sif = f.read().strip()

width = 25
height = 6
layer_size = width*height

layers = [sif[x:x+layer_size] for x in range(0, len(sif), layer_size)]

layer_analysis = []
for layer in layers:
    digit_count = Counter(layer)
    layer_analysis.append((digit_count['0'], digit_count['1'] * digit_count['2']))

print(sorted(layer_analysis, key=lambda x: x[0])[0][1])
