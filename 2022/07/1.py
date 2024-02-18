with open('input.txt', 'r') as f:
    data = [x[:-1] for x in f.read().split('$ ')[1:]]

file_struct = {}

curr_dir = 'root'
for command in data:
    if command == 'cd ..':
        curr_dir = '/'.join(curr_dir.split('/')[:-1])
    elif command.startswith('cd '):
        curr_dir += '/' + command.split(' ')[1]
    elif command.startswith('ls'):
        contents = command.split('\n')[1:]
        files = [(x.split(' ')) for x in contents if not x.startswith('dir')]
        file_struct[curr_dir] = files

sizes = {}
for key, value in file_struct.items():
    total = 0
    keys = [k for k in file_struct.keys() if k.startswith(key)]
    for k in keys:
        [total := total + int(x[0]) for x in file_struct[k]]
    sizes[key] = total

print(sum([value for key, value in sizes.items() if value <= 100000]))
