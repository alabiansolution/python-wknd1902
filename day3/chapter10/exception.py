# print(0/0)
import module
num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
try:
    print(num1/num2)
    print(module.states['Imo'])
except ModuleNotFoundError as e:
    print("This module is not found '{}'".format(e))
except ZeroDivisionError as a:
    print("{} can not be divisible by {} this is a '{}' error".format(num1, num2, a))
