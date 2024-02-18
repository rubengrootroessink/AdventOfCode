import math

time, distance = [int(x.split(': ')[1].replace(' ', '')) for x in open('input.txt').read().split('\n')[:-1]]

low = math.ceil(0.5*(time-math.sqrt(time**2-4*distance)))
high = math.floor(0.5*(math.sqrt(time**2-4*distance)+time))

result = high - low + 1

# Edge case if any of the boundaries is exactly the distance
# Not applicable in my case, can be tested by the third test case in question 1
if time*low-low**2 == distance:
    result -= 1
if time*high-high**2 == distance:
    result -= 1

print(result)
