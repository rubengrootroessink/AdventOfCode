# Inspired by others
import re

def recurse(rest):
    nr_childs, nr_meta = rest[:2]
    rest = rest[2:]
    values = []

    for i in range(nr_childs):
        child_value, rest = recurse(rest)
        values.append(child_value)

    metadata = rest[:nr_meta]
    
    if nr_childs == 0:
        sum_meta = sum(metadata)
        return (sum_meta, rest[nr_meta:])

    else:
        ret_value = 0
        for i in metadata:
            if i in range(1, len(values)+1):
                ret_value += values[i-1]
        return (ret_value, rest[nr_meta:])
        
with open('input.txt') as f:
    integers = [int(x) for x in f.read().strip().split(' ')]

result, remaining = recurse(integers)
print(result)
