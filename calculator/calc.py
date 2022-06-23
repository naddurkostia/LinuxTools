def calculate():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    operator = input("Enter operator: ")

    if operator == '+':
        print('Answer: '.format(first, second))
        print(first + second)
    elif operator == '-':
        print('Answer: '.format(first, second))
        print(first - second)
    elif operator == '*':
        # print('{} * {} = '.format(first, second))
        print(first * second)
    elif operator == '/':
        # print('{} / {} = '.format(first, second))
        print(first / second)
calculate()