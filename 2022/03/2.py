alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
with open('input.txt', 'r') as f:
    data = [x.split('\n')[0] for x in f.readlines()]

n = 3
chunked_list = [data[i*n:(i+1)*n] for i in range((len(data)+n-1)//n)]
for item in chunked_list:
    f, s, t = item
    for char in f:
        if char in s and char in t:
            result += (alphabet.index(char) + 1)
            break
                
print(result)    
