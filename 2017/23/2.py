def non_prime(n):
    i = 2
    while i * i <= n:
        if n%i == 0:
            return True
        i += 1
    return False

b = 105700
c = 122700

h = 0
while True:
    if non_prime(b):
        h += 1
    if b == c:
        break
    b += 17

print(h)
