def result(x, y, sign):
    """
    The function performs the simplest mathematical calculations
    """

    if sign == '+':
        result = x + y
    elif sign == '-':
        result = x - y
    elif sign == '/':
        result = x / y
    elif sign == '*':
        result = x * y
    elif sign == '**':
        result = x ** y
    return result


try:
    # Enter a math expression separated by a space
    exp = input("enter a number, sign and number separated by a space :").split()

    # Getting ahead of the first and second numbers
    number1 = int(exp[0])
    number2 = int(exp[2])

    print("{0:.3f}".format(result(number1, number2, exp[1])))

except ZeroDivisionError:
    print("Division by zero!")


# vladalh@mail.ru
