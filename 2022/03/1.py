alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
with open('input.txt', 'r') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

for item in data:
    assert len(item) % 2 == 0
    f, s = item[:len(item) // 2], item[len(item) // 2:]
    for char in f:
        if char in s:
            result += (alphabet.index(char) + 1)
            break
                
print(result)    
