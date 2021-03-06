def varLenArg(*n):
    print(n)


varLenArg(10, 20, 30, 40)


def varLenArg(*n, a):
    print(n)
    print(a)


varLenArg(10, 20, 30, 40, a=50)
