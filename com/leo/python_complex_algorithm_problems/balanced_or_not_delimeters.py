def balance_or_not(delimeterssequence):
    stack = []
    for i in range(0, len(delimeterssequence)):
        if delimeterssequence[1] == '}' or delimeterssequence[1] == ')' or delimeterssequence[1] == ']':
            print('Not balanced')
            break
        elif delimeterssequence[i] == '{' or delimeterssequence[i] == '(' or delimeterssequence[i] == '[':
            stack.append(delimeterssequence[i])
        elif delimeterssequence[i] == '}' or delimeterssequence[i] == ')' or delimeterssequence[i] == ']':
            if delimeterssequence[i] == '}' and '{' in stack:
                stack.pop(stack.__getitem__('}'))
            elif delimeterssequence[i] == ')' and '(' in stack:
                stack.pop(stack.__getitem__(')'))
            elif delimeterssequence[i] == ']' and '[' in stack:
                stack.pop(stack.__getitem__(']'))
        if not stack:
            print("balanced")
            break
        else:
            print("not balanced")
            break

    trial = ['(', ')', '{', '}']
    balance_or_not(trial)
