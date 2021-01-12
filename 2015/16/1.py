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
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    
    for sue, items in all_sue_dict.items():
        count = 0
        for key, value in items.items():
            if value_dict[key] == value:
                count += 1
        if count == len(items):
            print(sue)
