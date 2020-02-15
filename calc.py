
""" this is a simple calculator app with no gui """

print("Welcome to the simple calculator")
print('I can 1. add, 2. subtract, 3. divide, 4. multiply ')
x = 0
y = 0


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def mult(x, y):
    return x * y


choice = input('Choose from 1 - 4: ')
x = int(input('your first number: '))
y = int(input('your second number: '))

if choice == '1':
    print(add(x, y))
elif choice == '2':
    print(sub(x, y))
elif choice == '3':
    print(div(x, y))
elif choice == '4':
    print(mult(x, y))


