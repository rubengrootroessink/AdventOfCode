with open('input.txt', 'r') as f:
    all_sue_dict = {}
    for line in f.readlines():
        data = line.split('\n')[0].split(': ', 1)
        nr = int(data[0].split(' ')[1])        
        sue_dict = {}
        items = data[1].split(', ')
        for item in items:
            name, value = item.split(': ')
            sue_dict[name] = int(value)
        all_sue_dict[nr] = sue_dict
        
    value_dict = {
        'children': 3,
        'cats': ('larger', 7),
        'samoyeds': 2,
        'pomeranians': ('smaller', 3),
        'akitas': 0,
        'vizslas': 0,
        'goldfish': ('smaller', 5),
        'trees': ('larger', 3),
        'cars': 2,
        'perfumes': 1
    }
    
    for sue, items in all_sue_dict.items():
        count = 0
        for key, value in items.items():
            
            temp_val = value_dict[key]
            if type(temp_val) == tuple:
                if temp_val[0] == 'larger':
                    count = count + 1 if value > temp_val[1] else count
                else:
                    count = count + 1 if value < temp_val[1] else count
            elif temp_val == value:
                count += 1
        if count == len(items):
            print(sue)
