# This is a calculator that calculates expression written on reversed polish , for example (1 2 3 + -) = -4
def calculate(expressions):
    stack = []
    for i in expressions:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
            print(stack)
            continue
        elif i == '-':
            stack.append(stack.pop() - stack.pop())
            print(stack)
            continue
        elif i == '/':
            stack.append(stack.pop() / stack.pop())
            print(stack)
            continue
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
            print(stack)
            continue
        stack.append(i)
        print(stack)
    return stack.pop()


calculate([1, 2, 3, '*', '+', 2, '-'])

# ka8e praxi einai dimelis