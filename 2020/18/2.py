import re

def rreplace(pattern, sub, string):
    return re.sub('%s$' % pattern, sub, string)

def find_matching(assignment, count):
    currPos = count
    level = 0
    found = False
    while not found:
        if assignment[currPos] == '(':
            level += 1
        elif assignment[currPos] == ')':
            level -= 1
        if level == 0:
            found = True
            return count, currPos + 1
        currPos += 1
                
def split(assignment):
    result = []
    count = 0
    while count < len(assignment) - 1:
        if assignment[count] == '(':
            startPos, endPos = find_matching(assignment, count)
            result.append(assignment[startPos:endPos+1])
            count += endPos - count
        elif assignment[count].isdigit():
            startPos = count
            currPos = count
            while assignment[currPos].isdigit():
                currPos += 1
            result.append(int(assignment[startPos:currPos]))
            count += currPos - startPos
        elif assignment[count] == '*' or assignment[count] == '+':
            result.append(assignment[count])
            count += 1
    return result
    
def check_index(splitted_string, op):
    try:
        index = splitted_string.index(op)
        return index
    except ValueError:
        return -1
        
def calc(assignment, op):
    splitted_string = assignment

    index = check_index(splitted_string, op)
    while not index == -1:
        val_left = splitted_string[index - 1]
        if type(val_left) != int:
            val_left = eval(val_left[1:len(val_left)-1])

        val_right = splitted_string[index + 1]
        if type(val_right) != int:
            val_right = eval(val_right[1:len(val_right)-1])

        if op == '+':
            result = val_left + val_right
        elif op == '*':
            result = val_left * val_right

        splitted_string = splitted_string[0:index-1] + [result] + splitted_string[index+2:len(splitted_string)]
        index = check_index(splitted_string, op)

    return splitted_string

def eval(assignment):
    splitted_string = split(assignment)
    splitted_string = calc(splitted_string, '+')
    splitted_string = calc(splitted_string, '*')
    return int(splitted_string[0])

with open('input.txt', 'r') as file:
    result = []
    for assignment in file.readlines():
        result.append(eval(assignment.replace(' ', '')))
    print(sum(result))
