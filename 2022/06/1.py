with open('input.txt', 'r') as f:
    data = f.read().split('\n')[0]

last_chars = list(data[:3])
for i, char in enumerate(data[3:]):
    last_chars = last_chars + [char]
    if len(set(last_chars)) == 4:
        print(i + 4)
        break
    last_chars.pop(0)
