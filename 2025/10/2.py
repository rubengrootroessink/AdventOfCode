# Inspired by others
import z3

def resolve(joltages, button_presses):
    result = 0

    # Define buttons as z3.Ints with unique names
    presses = [z3.Int(f"b{i}") for i in range(len(button_presses))]

    # SMT solver
    s = z3.Optimize()

    # Requirement that presses can only be positive numbers
    s.add(z3.And([press >= 0 for press in presses]))

    # Define which buttons affect which joltages and create equations
    s.add(z3.And([sum(presses[j] for j, button in enumerate(button_presses) if i in button) == joltage for i, joltage in enumerate(joltages)]))

    # Define objective to be minified
    s.minimize(sum(presses))

    # Assert that a satisfiable assignment of variables exists
    assert s.check() == z3.sat

    # Print the minimized solutions
    m = s.model()
    for press in presses:
        result = result + m[press].as_long()

    return result

with open('input.txt') as f:
    lines = [x.strip().split(' ') for x in f.readlines()]

count = 0
for line in lines:
    _, button_presses, joltages = line[0], line[1:-1], line[-1]
    joltages = list(map(int, joltages[1:-1].split(',')))
    button_presses = [tuple(map(int, b[1:-1].split(','))) for b in button_presses]
    count += resolve(joltages, button_presses)

print(count)
