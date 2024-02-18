def dragon_curve(initial_state, size):
    a = initial_state
    while len(a) < size:
        b = ''.join(['0' if i == '1' else '1' for i in a[::-1]])
        a = a + '0' + b
    
    return a[0:size]

def checksum(bits):
    checksum = bits
    while len(checksum) % 2 == 0:
        pairs = [checksum[i:i+2] for i in range(0, len(checksum), 2)]
        checksum = ''.join(['1' if x[0] == x[1] else '0' for x in pairs])
    return checksum

with open('input.txt') as f:
    initial_state = f.read().strip()

disk_size = 35651584

bits = dragon_curve(initial_state, disk_size)
checksum = checksum(bits)

print(checksum)
