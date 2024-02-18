import re

def rreplace(pattern, sub, string):
    return re.sub('%s$' % pattern, sub, string)

def find_matching(assignment):
    startPos = len(assignment)

    for i in range(len(assignment) - 1, -1, -1):
        if ')' in assignment[i] and startPos == len(assignment):
            startPos = i

    openBr = 0
    for endPos in range(len(assignment) - 1, -1, -1):
        if ')' in assignment[endPos]:
            openBr += assignment[endPos].count(')')
        elif '(' in assignment[endPos]:
            openBr -= assignment[endPos].count('(')
            if openBr == 0:
                return startPos, endPos

def eval(assignment):
    if ')' in assignment[-1]:
        startPos, endPos = find_matching(assignment)
        
        data = [assignment[endPos].replace('(', '', 1)]
        data = data + assignment[endPos + 1:len(assignment) - 1]
        data = data + [rreplace('\)', '', assignment[startPos])]

        running_val = eval(data)
        op = assignment[endPos - 1]

        if endPos == 0:
            return eval(data)

        val = 0
        if len(assignment[0:endPos - 1]) == 1:
            val = int(assignment[0:endPos - 1][0])
        else:
            val = eval(assignment[0:endPos - 1])

        if op == '*':
            return val * running_val
        else:
            return val + running_val
    else:
        running_val = int(assignment[-1])
        op = assignment[-2]
        val = 0

        if len(assignment) == 3:
            val = int(assignment[0])
        else:
            val = eval(assignment[0:-2])

        if op == '*':
            return val * running_val
        else:
            return val + running_val

with open('input.txt', 'r') as file:
    result = []
    for assignment in file.readlines():
        listed = assignment.split('\n')[0].split(' ')
        result.append(eval(listed))
    print(sum(result))
