def factorial(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result


def factorial1(num):
    if num == 0:
        return 1
    else:
        return num * factorial1(num - 1)


num = int(input("Enter the num "))
print(factorial(num))
print(factorial1(num))
