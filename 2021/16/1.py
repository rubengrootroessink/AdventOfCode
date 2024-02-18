def read_packet(string):
    total_version = 0
    version = int(string[0:3], 2)
    total_version += version
    iden = int(string[3:6], 2)
    
    packet = {
        'version': version,
        'id': iden,
    }

    return_string = ''

    curr_length = 6
    if iden != 4:
        length_id = string[6]
        curr_length = 7
        if length_id == '0':
            length = int(string[7:22], 2)
            curr_length += 15
            parse_string = string[22:22+length]
            
            sub_packets = []

            while len(parse_string) != 0:
                sub_pack, parse_string = read_packet(parse_string)
                sub_packets.append(sub_pack)

            packet['sub_packets'] = sub_packets
            return_string = string[22+length:]

        elif iden != '100' and length_id == '1':
            num_subpackets = int(string[7:18], 2)

            sub_packets = []

            parse_string = string[18:]
            while len(sub_packets) != num_subpackets:
                sub_pack, parse_string = read_packet(parse_string)
                sub_packets.append(sub_pack)

            packet['sub_packets'] = sub_packets
            return_string = parse_string

    elif iden == 4:
        total_num = ''
        start_int = 6

        found = False
        while not found:
            if string[start_int] == '0':
                found = True
            total_num += string[start_int:start_int + 5][1:]
            start_int += 5
        
        return_string = string[start_int:]
        literal_value = int(total_num, 2)
        packet['literal_value'] = literal_value
    
    return packet, return_string

def count_dict(input_dict):
    count = 0
    count += input_dict['version']
    if 'sub_packets' in input_dict.keys():
        for item in input_dict['sub_packets']:
            count += count_dict(item)
    return count

binary = ''
with open('input.txt') as f:
    data = f.read().split('\n')[0]
    for hex_char in data:
        bin_char = str(bin(int(hex_char, base=16)))[2:]
        binary += '0'*(4-len(bin_char)) + bin_char

packets = []

result = read_packet(binary)[0]
print(count_dict(result))
