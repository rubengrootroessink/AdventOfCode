def hasher(input_str):
    result = 0
    for c in input_str:
        result += ord(c)
        result *= 17
        result = result % 256
    return result

box_dict = {}

with open('input.txt') as f:
    data = f.read()[:-1].split(',')

for lens in data:

    if lens.endswith('-'):
        name = lens[:-1]
        curr_box = hasher(name)
        
        try:
            box_dict[curr_box].pop(name)
        except:
            pass

    elif '=' in lens:
        name, focal_str = lens.split('=')
        curr_box = hasher(name)
        if not curr_box in box_dict.keys():
            box_dict[curr_box] = {}
        box_dict[curr_box][name] = int(focal_str)

result = 0
for box_num, contents in box_dict.items():
    if not contents == {}:
        for i, (label, focal_str) in enumerate(contents.items()):
            result += (box_num+1)*(i+1)*focal_str

print(result)
