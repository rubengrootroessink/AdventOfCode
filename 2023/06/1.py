import math

time, distance = [list(map(int, x.split()[1:])) for x in open('input.txt').read().split('\n')[:-1]]

result_list = []

for i in range(len(time)):
    t = time[i]
    d = distance[i]
    
    low = math.ceil(0.5*(t-math.sqrt(t**2-4*d)))
    high = math.floor(0.5*(math.sqrt(t**2-4*d)+t))

    count = high - low + 1

    # Edge case if any of the boundaries is exactly the distance
    if t*low-low**2 == d:
        count -= 1
    if t*high-high**2 == d:
        count -= 1
    
    result_list.append(count)

print(math.prod(result_list))
