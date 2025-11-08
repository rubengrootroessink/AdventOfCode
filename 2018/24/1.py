import math
import re

pattern = r'^(\d+) units each with (\d+) hit points (.*?)?with an attack that does (\d+) (\w+) damage at initiative (\d+)$'

class Group:
    def __init__(self, identifier, n, hp, attack_strength, attack_type, initiative, weaknesses, immunities, side):
        self.id = identifier
        self.n = n
        self.hp = hp
        self.attack_strength = attack_strength
        self.attack_type = attack_type
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.side = side

    def power(self):
        return self.n * self.attack_strength

    def select_target(self, effective_power, attack_type):
        damage = effective_power
        if attack_type in self.immunities:
            damage = 0
        elif attack_type in self.weaknesses:
            damage = 2*effective_power
        return damage, self.power(), self.initiative

    def attacked(self, effective_power, attack_type):
        damage = effective_power
        if attack_type in self.immunities:
            damage = 0
        elif attack_type in self.weaknesses:
            damage = 2*effective_power

        units_killed = math.floor(damage / self.hp)
        self.n = max(0, self.n - units_killed)

    def __str__(self):
        string_side = "Immune System group" if self.side == 0 else "Infection group"
        return f"{string_side} {self.id+1}"
    
    def __repr__(self):
        return self.__str__()

def parse_group(identifier, side, line):
    match = re.match(pattern, line)
    if match:
        n, hp, specials, attack_strength, attack_type, initiative = match.groups()
        n = int(n)
        hp = int(hp)
        attack_strength = int(attack_strength)
        initiative = int(initiative)

        weaknesses = []
        immunities = []
        if specials != '':
            specials = specials[1:-2].split('; ')
            for s in specials:
                if s.startswith('weak to '):
                    weaknesses = s.split('weak to ')[1].split(', ')
                elif s.startswith('immune to '):
                    immunities = s.split('immune to ')[1].split(', ')
                else:
                    assert False

        return Group(identifier, n, hp, attack_strength, attack_type, initiative, weaknesses, immunities, side)

def fight(groups):
    target_mapping = {}

    order = sorted([g for g in groups if g.n > 0], key=lambda x:(-x.side, -x.power(), -x.initiative))

    target_mapping = {}
    for g in order:
        enemies = sorted([(e, e.select_target(g.power(), g.attack_type)) for e in groups if e.n > 0 and e.side != g.side and not e in target_mapping.values()], key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))
        enemies = [v for v in enemies if v[1][0] != 0]
        if len(enemies) > 0:
            target_mapping[g] = enemies[0][0]
    
    for g, e in sorted(target_mapping.items(), key=lambda x: -x[0].initiative):
        curr_units = e.n
        e.attacked(g.power(), g.attack_type)

with open('input.txt') as f:
    armies = [x.strip() for x in f.read().split('\n\n')]

groups = []

identifier = 0
for line in armies[0].split('\n')[1:]:
    groups.append(parse_group(identifier, 0, line))
    identifier += 1

identifier = 0
for line in armies[1].split('\n')[1:]:
    groups.append(parse_group(identifier, 1, line))
    identifier += 1

while True:
    fight(groups)
    if len(set([g.side for g in groups if g.n > 0])) == 1:
        print(sum([g.n for g in groups]))
        break
