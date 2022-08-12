"""BASIC CALCULATOR PROGRAM"""

print('What operation would you like to perform?')
operation = str(input('Choose: \n [1. addition, 2. subtraction, 3.multiplication and 4. division] : '))


def calc():
    if operation in ('1', '2', '3', '4'):
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))

        if operation == '1':
            print(f'{num1} + {num2} = ' + str(addition(num1, num2)))

        elif operation == '2':
            print(f'{num1} - {num2} = ' + str(subtract(num1, num2)))

        elif operation == '3':
            print(f'{num1} * {num2} = ' + str(multiply(num1, num2)))

        elif operation == '4':
            print(f'{num1} / {num2} = ' + str(division(num1, num2)))

    else:
        print('Enter a valid input!')


def addition(x, y):
    return x + y


def division(x, y):
    return x / y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


calc()
