def closes_b(x, y):
    if x == '(' and y == ')':
        return True
    elif x == '[' and y == ']':
        return True
    elif x == '{' and y == '}':
        return True
    else:
        return False


def balance_check(insert):
    stack = []
    for i in insert:
        if i in '({[':
            stack.append(i)
        elif i == stack[0] and i in ')]}':
            return False
        elif i in ')]}':
            stack.append(i)
    for j in stack:
        for k in stack:
            if closes_b(j,k):
                stack.pop(j)
                stack.pop(k)
                continue

    if(len(stack) == 0):
        return True
    else:
        return False

insert = ['(','(',')',')']
if balance_check(insert):
    print('balanced')
else:
    print('unbalanced')

