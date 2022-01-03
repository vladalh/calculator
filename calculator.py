# Enter a math expression separated by a space
exp = input("Enter math expression :").split()

# Getting ahead of the first and second numbers
number1 = int(exp[0])
number2 = int(exp[2])

# Defining a math action
result = ""
if exp[1] == '+':
    result = "{0:.3f}".format(number1 + number2)
elif exp[1] == '-':
    result = "{0:.3f}".format(number1 - number2)
elif exp[1] == '/' and number2 != 0:
    result = "{0:.3f}".format(number1 / number2)
elif exp[1] == '*':
    result = "{0:.3f}".format(number1 * number2)
elif exp[1] == '**':
    result = "{0:.3f}".format(number1 ** number2)
print("Expression result :", result)


# vladalh@mail.ru