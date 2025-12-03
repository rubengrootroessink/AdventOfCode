dp_dict = {}

def recurse(bank, depth):
    if (len(bank), depth) in dp_dict:
        return dp_dict[(len(bank), depth)]
    elif depth == 0:
        res = max(bank)
        dp_dict[(len(bank), depth)] = res
        return res
    else:
        max_val = 0
        for i, d in enumerate(bank[:-depth]):
            res = recurse(bank[i+1:], depth-1)
            dp_dict[(len(bank[i+1:]), depth-1)] = res
            max_val = max(max_val, int(str(d) + str(res)))
        
        dp_dict[(len(bank), depth)] = max_val
        return max_val

with open('input.txt') as f:
    banks = [[int(y) for y in x.strip()] for x in f.readlines()]

num_batteries = 2
final_res = 0
for bank in banks:
    dp_dict = {}
    final_res += recurse(bank, num_batteries - 1)
print(final_res)
