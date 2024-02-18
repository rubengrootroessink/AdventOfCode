with open('input.txt') as f:
    box_ids = [x.strip() for x in f.readlines()]

for i, box_id in enumerate(box_ids):
    for s_box in box_ids[i+1:]:
        comparison = sum([1 if box_id[j] == s_box[j] else 0 for j in range(len(box_id))])
        if comparison == len(box_id) - 1:
            result = ''
            for j in range(len(box_id)):
                if box_id[j] == s_box[j]:
                    result += box_id[j]
            print(result)
