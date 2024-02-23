with open('input.txt') as f:
    sif = f.read().strip()

width = 25 
height = 6
layer_size = width*height

layers = [sif[x:x+layer_size] for x in range(0, len(sif), layer_size)]

result = ''
for i in range(layer_size):
    for j in range(len(layers)):
        if layers[j][i] in ['0', '1']:
            result += layers[j][i]
            break
        else:
            continue

for i in range(0, layer_size, width):
    print(''.join(['.' if x == '0' else '#' for x in result[i:i+width]]))
