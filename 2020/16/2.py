def clean(assigned, possibilities):
    result = possibilities.copy()
    for key, value in possibilities.items():
        if len(value) == 1:
            assigned[key] = value[0]
            result.pop(key)

    for field_name, field_value in fields.items():
        possible_mappings = []
        for key, value in result.items():
            if field_name in value:
                possible_mappings.append(key)
        if len(possible_mappings) == 1:
            result.pop(possible_mappings[0])
            assigned[possible_mappings[0]] = field_name

    return assigned, result

def get_range(str_range):
    temp = [int(x) for x in str_range.split('-')]
    return range(temp[0], temp[1] + 1)

with open('input.txt', 'r') as file:
    fields = {}
    data = file.read().split('\n\n')
    for field in data[0].split('\n'):
        temp = field.split(': ')
        field_name = temp[0]
        field_val = temp[1].split(' or ')
        range_1 = get_range(field_val[0])
        range_2 = get_range(field_val[1])
        fields[field_name] = (range_1, range_2)

    possible_values = []
    for key, value in fields.items():
        possible_values = possible_values + (list(value[0]))
        possible_values = possible_values + (list(value[1]))
    possible_values = list(sorted(set(possible_values)))
    
    nearby_tickets = data[2].split(':\n')[1].split('\n')[:-1]
    
    valid_tickets = []
    for ticket in nearby_tickets:
        splitted_ticket = [int(y) for y in ticket.split(',')]
        if len([1 for x in splitted_ticket if x in possible_values]) == len(ticket.split(',')):
            valid_tickets.append(splitted_ticket)
    
    t_matrix = zip(*valid_tickets)
    
    possibilities = {}
    for i, row in enumerate(t_matrix):
        for key, value in fields.items():
            result = all([True if x in value[0] or x in value[1] else False for x in list(row)])
            if result:
                if i in possibilities.keys():
                    possibilities[i].append(key)
                else:
                    possibilities[i] = [key]

    assigned = {}
    while len(assigned) != len(fields):
        assigned, possibilities = clean(assigned, possibilities)
    
    your_ticket = [int(x) for x in data[1].split(':\n')[1].split(',')]

    result = 0
    for item in sorted(assigned.items()):
        if item[1].startswith('departure'):
            if result == 0:
                result = your_ticket[item[0]]
            else:
                result *= your_ticket[item[0]]

    print(result)
