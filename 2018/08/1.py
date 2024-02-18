# Inspired by others
import re

def recurse(rest):
    nr_childs, nr_meta = rest[:2]
    rest = rest[2:]
    sum_meta = 0

    for i in range(nr_childs):
        child_meta, rest = recurse(rest)
        sum_meta += child_meta

    metadata = rest[:nr_meta]
    sum_meta += sum(metadata)

    if nr_childs == 0:
        return (sum_meta, rest[nr_meta:])
    else:
        return (sum_meta, rest[nr_meta:])
        
with open('input.txt') as f:
    integers = [int(x) for x in f.read().strip().split(' ')]

result, remaining = recurse(integers)
print(result)
