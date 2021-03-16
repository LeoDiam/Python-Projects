import math

arr = [1, 7, 3, '+', '-']
arr_copy = arr[:]


def get_number_of_args(func):
    variables = list(func.__code__.co_varnames)
    return len(variables)


def func_sum(a, b):
    return a + b


def func_sub(a, b):
    return a - b


def func_mul(a, b):
    return a * b


def func_div(a, b):
    return float(a) / b


def func_sqrt(a):
    return math.sqrt(a)


operators = {
    '+': func_sum,
    '-': func_sub,
    '*': func_mul,
    '/': func_div,
    'sqrt': func_sqrt
}


def calc():
    i = 0
    while len(arr) != 1:
        if isinstance(arr[i], str):
            op = arr[i]
            num = get_number_of_args(operators[op])
            res = operators[op](*arr[i - num:i])
            arr[i - num] = res
            if num == 2:
                arr.pop(i - num + 1)
                arr.pop(i - num + 1)
            if num == 1:
                arr.pop(i - num + 1)
            i -= num
        else:
            i += 1
    print("The result of", arr_copy, "is:", arr[0])


calc()
