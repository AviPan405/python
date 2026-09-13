def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
while True:
    try:
        a = float(input('Enter a number : '))
        b = float(input('Enter another number : '))
        c = input('Enter your operation, choose between (+),(-),(*) and (/) or enter exit to exit the calculator : ')
        if c == '+':
            result =  add(a,b)
            print(result)
            continue
        elif c == '-':
            result = substract(a,b)
            print(result)
            continue
        elif c == '*':
            result = multiply(a,b)
            print(result)
            continue
        elif c == '/':
            result = divide(a,b)
            print(result)
            continue
        elif c == 'exit':
            break
        else:
            print('Error,Try again!')
            continue
    except ValueError:
        print('Incorrect value try again!')
    except ZeroDivisionError:
        print('A number cannot be divided by Zero!')