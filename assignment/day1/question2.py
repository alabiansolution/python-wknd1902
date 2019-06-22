# 2. Write a program in python that will print the lowest number among three numbers supplied

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))

if num1 < num2 and num1 < num3:
    print('{} is the lowest among {} and {}'.format(num1, num2, num3))
elif num2 < num1 and num2 < num3:
    print('{} is the lowest among {} and {}'.format(num2, num1, num3))
elif num3 < num1 and num3 < num2:
    print('{} is the lowest among {} and {}'.format(num3, num2, num1))
