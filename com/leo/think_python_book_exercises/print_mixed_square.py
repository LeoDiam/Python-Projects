def printplus():
    return '+'


def printminus():
    return '-'


def printmixedline():
    return printplus() + 4 * printminus() + printplus() + 4 * printminus() + printplus()


def printemptyline():
    return '|' + 4 * ' ' + '|' + 4 * ' ' + '|'


def print_mixed_sqr():
    print(printmixedline())
    for i in range(0, 3):
        print(printemptyline())
    print(printmixedline())
    for i in range(0, 3):
        print(printemptyline())
    print(printmixedline())


print_mixed_sqr()


def multiply_lines(numoflines):
    numoflines = numoflines - 1
    print((numoflines * '+----') + '+')


def multiply_rows(numofrows, numoflines):
    for i in range(0, numofrows):
        print(numoflines * ('|' + 4 * ' '))


def printe(nol, nor):
    multiply_lines(nol)
    multiply_rows(nor, nol)
    multiply_lines(nol)
    multiply_rows(nor, nol)
    multiply_lines(nol)


printe(5, 15)
