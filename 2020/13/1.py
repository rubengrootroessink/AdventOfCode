def multiple(timestamp, busses):
    result = []
    for bus in busses:
        multiple = bus
        while multiple < timestamp:
            multiple = multiple + bus
        result.append((multiple, bus))
    return sorted(result)

with open('input.txt', 'r') as file:
    timestamp = int(file.readline())
    busses = [int(bus) for bus in file.readline().split(',') if bus != 'x']
    bus = multiple(timestamp, busses)[0]
    print(bus[1] * (bus[0] - timestamp))
