def isMatch(x, y):
    if x == '(' and y == ')':
        return True
    elif x == '[' and y == ']':
        return True
    elif x == '{' and y == '}':
        return True
    else:
        return False


def balance(stringList):
    stack = []
    index = 0
    isBalanced = True
    while index < len(stringList) and isBalanced:
        sL = stringList[index]
        if sL in '({[':
            stack.append(sL)
        else:
            if len(stack) == 0:
                isBalanced = False
            else:
                 top = stack.pop()
                 if not isMatch(top,sL):
                     isBalanced = False
        index +=1
    if len(stack) == 0 and isBalanced:
        return True
    else:
        return False
print(balance('[{(){}[]}]'))