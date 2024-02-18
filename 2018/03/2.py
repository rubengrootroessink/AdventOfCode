import re

with open('input.txt') as f:
    claims = [x.strip() for x in f.readlines()]

claim_dict = {}

claim_pattern = r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$'
for claim in claims:
    num, left_offset, top_offset, width, height = [int(x) for x in re.match(claim_pattern, claim).groups()]
    claim_dict[num] = {
        'hor': range(left_offset, left_offset + width + 1),
        'vert': range(top_offset, top_offset + height + 1)
    }

unique_vals = set()

keys = list(sorted(claim_dict.keys()))
for i, k1 in enumerate(keys):
    sliced = False
    for k2 in keys:

        hor_overlap = [x for x in claim_dict[k1]['hor'] if x in claim_dict[k2]['hor']]
        vert_overlap = [x for x in claim_dict[k1]['vert'] if x in claim_dict[k2]['vert']]
        
        if hor_overlap != [] and vert_overlap != [] and not k1 == k2:
            sliced = True

    if not sliced:
        print(k1)
