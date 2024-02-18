import re
import hashlib

def find_consecs(salt, num):
    hash_str = hashlib.md5((salt + str(num)).encode()).hexdigest()

    for i in range(0, 2016):
        hash_str = hashlib.md5(hash_str.encode()).hexdigest()

    triplets = re.findall(r'([a-f0-9])\1\1', hash_str)
    if triplets:
        quintuplets = re.findall(r'([a-f0-9])\1\1\1\1', hash_str)
        if quintuplets:
            return {'three': triplets[0], 'five': quintuplets}
        else:
            return {'three': triplets[0]}

    return False

with open('input.txt') as f:
    salt = f.read().strip()

group_dict = {}
nr_otps = 0

for i in range(0, 1001):
    result = find_consecs(salt, i)
    if result:
        group_dict[i] = result

curr_index = 0
while nr_otps < 64:

    if curr_index in group_dict.keys():
        indices_in_range = [x for x in group_dict.keys() if x in range(curr_index + 1, curr_index + 1001)]
        curr_triplet = group_dict[curr_index]['three']
        
        matches = False
        for i in indices_in_range:
            quintuplets = group_dict[i]
            if 'five' in quintuplets.keys():
                if curr_triplet in quintuplets['five']:
                    matches = True
 
        if matches:
            nr_otps += 1
    
    result = find_consecs(salt, curr_index + 1001)
    if result:
        group_dict[curr_index + 1001] = result

    curr_index += 1

print(curr_index - 1)
