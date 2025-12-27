from collections import deque, defaultdict
from itertools import combinations
import heapq
import copy

class Computer:
    def __init__(self, program):
        self.program = program        
        self.eip = 0
        self.rel_base = 0
        self.input_list = deque()
        self.output_list = deque()

    def parse_opcode(self, opcode):
        opcode = str(opcode).zfill(5)
        modes = [int(x) for x in opcode[0:3]][::-1]
        opcode = int(opcode[3:5])

        match opcode:
            case 1 | 2 | 7 | 8:
                return opcode, modes
            case 3 | 4 | 9:
                return opcode, modes[0:1]
            case 5 | 6:
                return opcode, modes[0:2]
            case 99:
                return opcode, []
    
    def reg_value(self, reg, mode, opcode, reg_num):
        match (mode, opcode, reg_num):
            case (0, _, _): return self.program[reg]
            case (1, _, _): return reg
            case (2, _, _): return self.program[reg] + self.rel_base

    # Opcode 1
    def add(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = self.program[reg_1] + self.program[reg_2]
        self.eip += 4

    # Opcode 2
    def mul(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = self.program[reg_1] * self.program[reg_2]
        self.eip += 4

    # Opcode 3
    def input(self, reg_1):
        self.program[reg_1] = self.input_list.popleft()
        self.eip += 2

    # Opcode 4
    def output(self, reg_1):
        self.output_list.append(self.program[reg_1])
        self.eip += 2

    # Opcode 5
    def jit(self, reg_1, reg_2):
        if self.program[reg_1] != 0: self.eip = self.program[reg_2]
        else: self.eip += 3

    # Opcode 6
    def jif(self, reg_1, reg_2):
        if self.program[reg_1] == 0: self.eip = self.program[reg_2]
        else: self.eip += 3

    # Opcode 7
    def lt(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = int(self.program[reg_1] < self.program[reg_2])
        self.eip += 4

    # Opcode 8
    def eq(self, reg_1, reg_2, reg_3):
        self.program[reg_3] = int(self.program[reg_1] == self.program[reg_2])
        self.eip += 4

    # Opcode 9
    def adj_rel(self, reg_1):
        self.rel_base += self.program[reg_1]
        self.eip += 2

    def run(self):
        opcode, modes = self.parse_opcode(self.program[self.eip])
        while opcode != 99:
            regs = [self.reg_value(self.eip+1+i, modes[i], opcode, i) for i in range(len(modes))]

            match opcode:
                case 1: self.add(regs[0], regs[1], regs[2])
                case 2: self.mul(regs[0], regs[1], regs[2])
                case 3:
                    if len(self.input_list) == 0:
                        break
                    else:
                        self.input(regs[0])
                case 4: self.output(regs[0])
                case 5: self.jit(regs[0], regs[1])
                case 6: self.jif(regs[0], regs[1])
                case 7: self.lt(regs[0], regs[1], regs[2])
                case 8: self.eq(regs[0], regs[1], regs[2])
                case 9: self.adj_rel(regs[0])
        
            opcode, modes = self.parse_opcode(self.program[self.eip])

bt_dict = {
    'north': 'south',
    'south': 'north',
    'west': 'east',
    'east': 'west',
}

def parse_move(comp):
    ascii_str = ''
    while len(comp.output_list) != 0:
        ascii_str += chr(comp.output_list.popleft())

    room_title, rest = ascii_str.split('== ')[1].split(' ==\n')
    
    blocks = rest.split('\n\n')
    description = blocks[0]

    block_titles = {
        'move': 'Doors here lead:\n',
        'items': 'Items here:\n',
        'input': 'Command?\n',
    }

    moves = []
    items = None

    for block in blocks[1:]:
        found = False
        for k, v in block_titles.items():
            if block.startswith(v):
                found = True
                values = block.split('\n- ')[1:]

                match k:
                    case 'move': moves = values
                    case 'items':
                        assert len(values) in [0, 1]
                        if len(values) == 1:
                            items = values[0]
            
    return room_title, moves, items

def parse_last_move(comp):
    ascii_str = ''
    while len(comp.output_list) != 0:
        ascii_str += chr(comp.output_list.popleft())

    res = [x for x in ascii_str.split('\n') if x.endswith('ejected back to the checkpoint.')]
    if len(res) == 1:
        if 'heavier' in res[0]:
            return True
        elif 'lighter' in res[0]:
            return False
    else:
        print(ascii_str.split('by typing ')[1].split(' ')[0])

def parse_take(comp, input_val):
    ascii_str = ''
    while len(comp.output_list) != 0:
        ascii_str += chr(comp.output_list.popleft())

    if ascii_str == f'\nYou take the {input_val}.\n\nCommand?\n':
        return True
    return False

def parse_drop(comp, input_val):
    ascii_str = ''
    while len(comp.output_list) != 0:
        ascii_str += chr(comp.output_list.popleft())

def command_input(comp, input_str):
    for x in input_str:
        comp.input_list.append(ord(x))
    comp.input_list.append(10)
    comp.run()

def backtrack_path(path):
    result_val = []

    for direction in path:
        result_val.append(bt_dict[direction])

    return result_val[::-1]

def get_combinations(input_list):
    combs = []
    for i in range(len(input_list)):
        combs.extend(combinations(input_list, i+1))
    return combs

with open('input.txt') as f:
    data = [int(x) for x in f.read().strip().split(',')]

program = defaultdict(int)
for i, v in enumerate(data):
    program[i] = v

location_dict = {}

comp = Computer(copy.deepcopy(program))
comp.run()

title, moves, item = parse_move(comp)
location_dict[title] = {'item': item, 'path': [], 'moves': {}}

for move in moves:
    location_dict[title]['moves'][move] = None

useful_items = []

while any([any([y == None for y in v['moves'].values()]) for k, v in location_dict.items()]):
    curr_title = None
    next_move = None
    for key, value in location_dict.items():
        if any([m == None for m in value['moves'].values()]):
            curr_title = key
            next_move = [mk for mk, mv in value['moves'].items() if mv == None][0]
            break
    
    path = location_dict[curr_title]['path'] + [next_move]

    comp = Computer(copy.deepcopy(program))
    comp.run()

    title, moves, item = parse_move(comp)
    for d in path:
        command_input(comp, d)
        title, moves, item = parse_move(comp)
   
    location_dict[curr_title]['moves'][next_move] = title
    location_dict[title] = {'item': item, 'path': path, 'moves': {}}
    
    for m in moves:
        if m != bt_dict[d]:
            location_dict[title]['moves'][m] = None
        else:
            location_dict[title]['moves'][m] = curr_title

    if item:
        if item in ['infinite loop', 'giant electromagnet']:
            pass
        else:
            command_input(comp, f'take {item}')
            if parse_take(comp, item):
                useful_items.append(item)

comp = Computer(copy.deepcopy(program))
comp.run()

visit_locations = [k for k, v in location_dict.items() if v['item'] in useful_items] + ['Security Checkpoint']

title, moves, item = parse_move(comp)

for i, loc in enumerate(visit_locations):
    path = location_dict[loc]['path']
    
    for d in path:
        command_input(comp, d)
        title, moves, item = parse_move(comp)

    if i != len(visit_locations) - 1:
        command_input(comp, f'take {location_dict[loc]["item"]}')
        assert parse_take(comp, item)
    
        for d in backtrack_path(path):
            command_input(comp, d)
            title, moves, item = parse_move(comp)

for item in useful_items:
    command_input(comp, f'drop {item}')
    parse_drop(comp, item)

next_move = [k for k, v in location_dict['Security Checkpoint']['moves'].items() if v == 'Pressure-Sensitive Floor'][0]

too_much = []

for comb in get_combinations(useful_items):
    if any(x.issubset(set(comb)) for x in too_much):
        continue

    for item in comb:
        command_input(comp, f'take {item}')
        assert parse_take(comp, item)

    command_input(comp, next_move)
    result = parse_last_move(comp)

    if result == None:
        break
    else:
        if not result:
            too_much.append(set(comb))

        for item in comb:
            command_input(comp, f'drop {item}')
            parse_drop(comp, item)
