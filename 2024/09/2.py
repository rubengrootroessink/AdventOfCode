import sys

with open('input.txt') as f: 
    data = [(int(x), i%2==0) for i, x in enumerate(f.read().strip())]

location_dict = {}
id_num = 0
empty_num = sys.maxsize
for i, (length, filled) in enumerate(data):
    if filled:
        location_dict[id_num] = {'length': length, 'prev': empty_num, 'next': empty_num-1}
        empty_num -= 1
        id_num += 1
    else:
        location_dict[empty_num] = {'length': length, 'prev': id_num-1, 'next': id_num}

location_dict[0]['prev'] = None
location_dict[id_num-1]['next'] = None

for i in range(id_num-1, 0, -1):
    block = location_dict[i]
    found = False
    index = 0

    while not found:
        loc = location_dict[index]

        if index == i:
            found = True
        elif index < 10000:
            index = loc['next']
        else:
            if loc['length'] >= block['length']:

                found = True
                if index == i:
                    continue

                if loc['length'] == block['length'] and block['prev'] == index and loc['next'] == i:
                    lp, ln = loc['prev'], loc['next']
                    bp, bn = block['prev'], block['next']
                    location_dict[index]['prev'] = i
                    location_dict[index]['next'] = bn
                    location_dict[lp]['next'] = i
                    location_dict[i]['prev'] = lp
                    location_dict[i]['next'] = index
                    location_dict[bn]['prev'] = index
                    continue
                
                old_prev, old_next = block['prev'], block['next']
                
                new_length = block['length']                
                if old_prev > 10000:
                    new_length += location_dict[old_prev]['length']
                    old_prev = location_dict[old_prev]['prev']
                if old_prev != None:
                    location_dict[old_prev]['next'] = empty_num

                if old_next == None:
                    pass
                elif old_next > 10000:
                    new_length += location_dict[old_next]['length']
                    old_next = location_dict[old_next]['next']
                if old_next != None:
                    location_dict[old_next]['prev'] = empty_num

                if loc['length'] == block['length']:
                    new_prev, new_next = loc['prev'], loc['next']             

                    location_dict[empty_num] = {'length': new_length, 'prev': old_prev, 'next': old_next}
                    location_dict[old_prev] 
                    empty_num -= 1

                    location_dict[new_prev]['next'] = i
                    location_dict[i] = {'length': block['length'], 'prev': new_prev, 'next': new_next}
                    location_dict[new_next]['prev'] = i

                elif loc['length'] > block['length']:
                    location_dict[empty_num] = {'length': new_length, 'prev': old_prev, 'next': old_next}
                    empty_num -= 1

                    location_dict[loc['prev']]['next'] = i
                    location_dict[i] = {'length': block['length'], 'prev': loc['prev'], 'next': index}
                    location_dict[index]['length'] -= block['length']
                    location_dict[index]['prev'] = i
            else:
                index = loc['next']

            if index == None:
                break

checksum = 0
index = 0
counter = 0
while index != None:
    loc = location_dict[index]
    if index < 10000:
        for i in range(loc['length']):
            checksum += (counter+i)*index
    counter += loc['length']
    index = loc['next']

print(checksum)
