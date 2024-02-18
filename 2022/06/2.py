with open('input.txt', 'r') as f:
    data = f.read().split('\n')[0]

last_chars = list(data[:13])
for i, char in enumerate(data[13:]):
    last_chars = last_chars + [char]
    if len(set(last_chars)) == 14:
        print(i + 14)
        break
    last_chars.pop(0)
