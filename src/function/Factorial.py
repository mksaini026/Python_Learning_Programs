def factorial(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result


def factorial1(num):
    result = 1
    if num >= 1:
        result = num * factorial1(num - 1)
    return result


num = int(input("Enter the num "))
print(factorial(num))
print(factorial1(num))
