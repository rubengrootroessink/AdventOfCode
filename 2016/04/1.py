from functools import reduce

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [x.split(']\n')[0].split('[') for x in lines]
    
    sum_matching = 0
    for line in lines:
        string, sec_id = line[0].rsplit('-', 1)
        checksum = line[1]
        sec_id = int(sec_id)
        string = string.replace('-', '')
        string = reduce(lambda x, y: x + y, sorted(string))
        
        result = {}
        for c in string:
            if c in result.keys():
                result[c] += 1
            else:
                result[c] = 1

        sorted_list = sorted(result.items(), key=lambda x: (-x[1], x[0]))
        stringified = "".join([y[0] for y in sorted_list])
        if stringified[:len(checksum)] == checksum:
            sum_matching += sec_id

    print(sum_matching)
