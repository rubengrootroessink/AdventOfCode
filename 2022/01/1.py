carry_on = []
with open('input.txt', 'r') as file:
    data = file.read()
    carry_on = data.split('\n\n')

elf_sum = []
for elf in carry_on:
    items = [int(x) for x in elf.split('\n') if x != '']
    elf_sum.append(sum(items))

print(max(elf_sum))
