# With treamendous help from: https://github.com/mebeim/aoc/blob/master/2022/README.md#day-16---proboscidea-volcanium

import re
import math
from itertools import product
from collections import defaultdict

def find_vals(line):
    pattern = r'Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]+)'
    matcher = re.match(pattern, line)
    valve_name = matcher.group(1)
    flow_rate = int(matcher.group(2))
    other_tunnels = matcher.group(3).split(', ')
    return valve_name, flow_rate, other_tunnels

def floyd_warshall(tunnel_graph):
    dist = defaultdict(lambda: defaultdict(lambda: math.inf))

    for valve, connected_valves in tunnel_graph.items():
        dist[valve][valve] = 0

        for c_valve in connected_valves:
            dist[valve][c_valve] = 1
            dist[c_valve][c_valve] = 0

    for n_1, n_2, n_3 in product(tunnel_graph, tunnel_graph, tunnel_graph):
        e_3, e_1, e_2 = dist[n_2][n_3], dist[n_2][n_1], dist[n_1][n_3]

        cmp_sum = e_1 + e_2
        if cmp_sum < e_3:
            dist[n_2][n_3] = cmp_sum

    return dist

def eval_path(rates, path):
    result = 0
    for valve, minutes in path.items():
        result += rates[valve] * minutes
    return result

def solutions(dist, flow_rates, eval_valves, minutes=30, curr_valve='AA', chosen_valves={}):
    for e_valve in eval_valves:
        new_minutes = minutes - dist[curr_valve][e_valve] - 1
        
        if new_minutes < 2:
            continue

        new_chosen_valves = chosen_valves | {e_valve: new_minutes}
        yield from solutions(dist, flow_rates, eval_valves - {e_valve}, new_minutes, e_valve, new_chosen_valves)

    yield chosen_valves

flow_rates = {}
tunnel_graph = defaultdict(list)

with open('input.txt', 'r') as f:
    data = [find_vals(x.split('\n')[0]) for x in f.readlines()]
    for item in data:
        valve_name, flow_rate, other_tunnels = item
        
        flow_rates[valve_name] = flow_rate
        tunnel_graph[valve_name] = other_tunnels

pressurized_valves = set([key for key, value in flow_rates.items() if value != 0])
dist = floyd_warshall(tunnel_graph)
max_flow = 0
for choice in solutions(dist, flow_rates, pressurized_valves):
    flow_rate = eval_path(flow_rates, choice)
    max_flow = max(flow_rate, max_flow)

print(max_flow)
