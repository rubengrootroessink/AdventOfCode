import itertools

def run(player_prof, opp_prof):
    dead = False
    player_turn = True
    while not dead:
        if player_turn:
            opp_prof['hit_points'] -= max(1, player_prof['damage'] - opp_prof['armor'])
            if opp_prof['hit_points'] <= 0:
                dead = True
            else:
                player_turn = False
        else:
            player_prof['hit_points'] -= max(1, opp_prof['damage'] - player_prof['armor'])
            if player_prof['hit_points'] <= 0:
                dead = True
            else:
                player_turn = True
    return player_turn

inventory = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

inventory = inventory.split('\n\n')
daggers = inventory[0].split('\n')
armor = inventory[1].split('\n')
rings = inventory[2].split('\n')

daggers = [list(filter(None, x.split(' '))) for x in daggers][1:]
armor = [list(filter(None, x.split(' '))) for x in armor][1:] + [['None', 0, 0, 0]]
rings = [list(filter(None, x.split(' '))) for x in rings][1:] + [['None', '+0', 0, 0, 0]] + [['None', '+0', 0, 0, 0]]

with open('input.txt', 'r') as f:
    lines = f.readlines()
    opp_hit_points = int(lines[0].split(': ')[1])
    opp_damage = int(lines[1].split(': ')[1])
    opp_armor = int(lines[2].split(': ')[1])

    least_cost = 10000000000000000000000000
    for sword in daggers:
        for item in armor:
            for ring in list(itertools.permutations(rings, 2)):
                total_cost = int(sword[1]) + int(item[1]) + int(ring[0][2]) + int(ring[1][2])
                total_damage = int(sword[2]) + int(item[2]) + int(ring[0][3]) + int(ring[1][3])
                total_armor = int(sword[3]) + int(item[3]) + int(ring[0][4]) + int(ring[1][4])

                opp_prof = {'hit_points': opp_hit_points, 'damage': opp_damage, 'armor': opp_armor}
                play_prof = {'hit_points': 100, 'damage': total_damage, 'armor': total_armor}
    
                if run(play_prof, opp_prof):
                    if total_cost < least_cost:
                        least_cost = total_cost
    print(least_cost)
