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
    for k2 in keys[i+1:]:

        hor_overlap = [x for x in claim_dict[k1]['hor'] if x in claim_dict[k2]['hor']]
        vert_overlap = [x for x in claim_dict[k1]['vert'] if x in claim_dict[k2]['vert']]
        
        if hor_overlap != [] and vert_overlap != []:
            hor_overlap = range(hor_overlap[0], hor_overlap[-1])
            vert_overlap = range(vert_overlap[0], vert_overlap[-1])

            for i in hor_overlap:
                for j in vert_overlap:
                    unique_vals.add((i, j))

print(len(unique_vals))
