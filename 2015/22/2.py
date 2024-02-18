import sys
import heapq

def magic_missile(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r):
    if own_mana >= 53:
        return (opp_hp-4, own_hp, own_armor, own_mana-53, mana_spend+53, s, p, r)
    else:
        return False

def drain(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r):
    if own_mana >= 73:
        return (opp_hp-2, own_hp+2, own_armor, own_mana-73, mana_spend+73, s, p, r)
    else:
        return False

def shield(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r):
    if own_mana >= 113 and s == 0:
        return (opp_hp, own_hp, own_armor, own_mana-113, mana_spend+113, 6, p, r)
    else:
        return False

def poison(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r):
    if own_mana >= 173 and p == 0:
        return (opp_hp, own_hp, own_armor, own_mana-173, mana_spend+173, s, 6, r)
    else:
        return False

def recharge(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r):
    if own_mana >= 229 and r == 0:
        return (opp_hp, own_hp, own_armor, own_mana-229, mana_spend+229, s, p, 5)
    else:
        return False

with open('input.txt') as f:
    opp_hp, opp_damage = [int(x.strip().split(': ')[1]) for x in f.readlines()]
    own_hp, own_mana, own_armor = 50, 500, 0

your_turn = True
mana_spend = 0
s, p, r = 0, 0, 0

state = (your_turn, opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r)
heap = [state]

prev_states = []
lowest = sys.maxsize

while heap:
    your_turn, opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r = heapq.heappop(heap)

    if your_turn:
        own_hp -= 1
    
    if s > 0:
        own_armor = 7
        s -= 1
    elif s == 0:
        own_armor = 0
    if p > 0:
        opp_hp -= 3
        p -= 1
        if opp_hp <= 0:
            lowest = min(lowest, mana_spend)
            continue
    if r > 0:
        own_mana += 101
        r -= 1

    if your_turn:
        mm = magic_missile(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r)
        dr = drain(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r)
        sh = shield(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r)
        po = poison(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r)
        re = recharge(opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r)

        n_states = [mm, dr, sh, po, re]
        n_states = [x for x in n_states if x != False and not x in prev_states]

        for n_state in n_states:
            heapq.heappush(heap, (not your_turn,) + n_state)
            prev_states.append((not your_turn,) + n_state)
        
    elif not your_turn:
        own_hp = own_hp - max(opp_damage - own_armor, 1)
        n_state = (not your_turn, opp_hp, own_hp, own_armor, own_mana, mana_spend, s, p, r)
        if own_hp >= 1 and not n_state in prev_states:
            heapq.heappush(heap, n_state)
            prev_states.append(n_state)

print(lowest)
