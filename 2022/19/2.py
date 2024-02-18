import re
import copy
import math
import heapq

def extract_vals(line):
    pattern = r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.'
    matcher = re.match(pattern, line)
    extracted_values = [int(x) for x in matcher.groups()]
    
    index = extracted_values[0]
    ore_robot = extracted_values[1:2]
    clay_robot = extracted_values[2:3]
    obsidian_robot = extracted_values[3:5]
    geode_robot = extracted_values[5:7]
    return index, ore_robot, clay_robot, obsidian_robot, geode_robot

with open('input.txt', 'r') as f:
    blueprints = [extract_vals(x.split('\n')[0]) for x in f.readlines()]

max_minutes = 32

geode_per_blueprint = []

for blueprint in blueprints[:3]:
    index = blueprint[0]
    ore_robot_cost = blueprint[1]
    clay_robot_cost = blueprint[2]
    obsidian_robot_cost = blueprint[3]
    geode_robot_cost = blueprint[4]

    max_ore_spend = max([ore_robot_cost[0], clay_robot_cost[0], obsidian_robot_cost[0], geode_robot_cost[0]])
    max_clay_spend = obsidian_robot_cost[1]
    max_obsidian_spend = geode_robot_cost[1]

    max_geodes = 0

    start_robots = [1, 0, 0, 0]

    start_materials = [0, 0, 0, 0]

    heap, visited = [(0, start_robots, start_materials, 0)], set()
    
    final_robots = []
    final_materials = []

    while heap:
        minutes, robots, materials, geode_count = heapq.heappop(heap)

        if minutes >= max_minutes:
            if geode_count > max_geodes:
                final_robots = robots
                final_materials = materials
            max_geodes = max(max_geodes, geode_count)
            continue
        if geode_count + robots[3] * (max_minutes - minutes) + sum(range(max_minutes - minutes + 1)) <= max_geodes:
            continue
        if (minutes, tuple(robots), tuple(materials)) in visited:
            continue
        visited.add((minutes, tuple(robots), tuple(materials)))

        # Ore Robot
        j = 0
        mined_materials = copy.deepcopy(materials)
        while mined_materials[0] < ore_robot_cost[0]:
            mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
            j += 1
        mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
        new_robots = copy.deepcopy(robots)
        new_robots[0] += 1
        new_materials = copy.deepcopy(mined_materials)
        new_materials[0] -= ore_robot_cost[0]
        if minutes + j + 1 <= max_minutes and not new_robots[0] > max_ore_spend:
            heap.append((minutes + j + 1, new_robots, new_materials, new_materials[3]))

        # Clay Robot
        j = 0
        mined_materials = copy.deepcopy(materials)
        while mined_materials[0] < clay_robot_cost[0]:
            mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
            j += 1
        mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
        new_robots = copy.deepcopy(robots)
        new_robots[1] += 1
        new_materials = copy.deepcopy(mined_materials)
        new_materials[0] -= clay_robot_cost[0]
        if minutes + j + 1 <= max_minutes and not new_robots[1] > max_clay_spend:
            heap.append((minutes + j + 1, new_robots, new_materials, new_materials[3]))

        # Obsidian Robot
        if robots[1] > 0:

            j = 0
            mined_materials = copy.deepcopy(materials)
            while mined_materials[0] < obsidian_robot_cost[0] or mined_materials[1] < obsidian_robot_cost[1]:
                mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
                j += 1
            mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
            new_robots = copy.deepcopy(robots)
            new_robots[2] += 1
            new_materials = copy.deepcopy(mined_materials)
            new_materials[0] -= obsidian_robot_cost[0]
            new_materials[1] -= obsidian_robot_cost[1]
            if minutes + j + 1 <= max_minutes and not new_robots[2] > max_obsidian_spend:
                heap.append((minutes + j + 1, new_robots, new_materials, new_materials[3]))

        # Geode Robot
        if robots[2] > 0:
            j = 0
            mined_materials = copy.deepcopy(materials)
            while mined_materials[0] < geode_robot_cost[0] or mined_materials[2] < geode_robot_cost[1]:
                mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
                j += 1
            mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
            new_robots = copy.deepcopy(robots)
            new_robots[3] += 1
            new_materials = copy.deepcopy(mined_materials)
            new_materials[0] -= geode_robot_cost[0]
            new_materials[2] -= geode_robot_cost[1]
            if minutes + j + 1 <= max_minutes:
                heap.append((minutes + j + 1, new_robots, new_materials, new_materials[3]))

        if minutes >= (max_minutes - 1):
            mined_materials = copy.deepcopy(materials)
            mined_materials = [x+robots[i] for i, x in enumerate(mined_materials)]
            heap.append((minutes + 1, robots, mined_materials, mined_materials[3]))
        
        heap = sorted(heap, key=lambda x:(x[1][3],x[1][2],x[1][1],x[1][0]), reverse=True)
    
    geode_per_blueprint.append((index, max_geodes))

print(math.prod([y for (x,y) in geode_per_blueprint]))
