def run(player_prof, opp_prof):
    dead = False
    player_turn = True
    while not dead:
        if player_turn:
            opp_prof['hit_points'] -= max(1, player_prof['damage'])
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

with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.split('\n')[0] for line in lines]
    opp_hit_points = int(lines[0].split(': ')[1])
    opp_damage = int(lines[1].split(': ')[1])
    
    print(opp_hit_points, opp_damage)
    

