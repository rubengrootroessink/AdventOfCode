with open('input.txt') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

card_dict = {}

for card in data:
    card_nr, vals = card.split(': ')
    card_nr = int(card_nr.split()[1])
    matching_nrs, own_nrs = vals.split(' | ')
    matching_nrs = [int(x) for x in matching_nrs.split()]
    own_nrs = [int(x) for x in own_nrs.split()]
    card_dict[card_nr] = {
        'match': matching_nrs,
        'own': own_nrs,
        'count': 1
    }

for i in range(1, len(card_dict)+1):
    nr_winning = len([1 for x in card_dict[i]['own'] if x in card_dict[i]['match']])
    for j in range(1, nr_winning+1):
        card_dict[i+j]['count'] += card_dict[i]['count']

print(sum([v['count'] for v in card_dict.values()]))
