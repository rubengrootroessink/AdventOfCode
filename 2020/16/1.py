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

    result_list = []
    for key, value in fields.items():
        result_list = result_list + (list(value[0]))
        result_list = result_list + (list(value[1]))
    result_list = list(sorted(set(result_list)))
    
    nearby_tickets = data[2].split(':\n')[1].split('\n')[:-1] # Necessary?
    
    result = 0
    for ticket in nearby_tickets:
        for val in ticket.split(','):
            temp_val = int(val)
            if not temp_val in result_list:
                result += temp_val
    print(result)
