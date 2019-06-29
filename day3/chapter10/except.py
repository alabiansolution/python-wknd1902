# print(0/0)
import module
num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
try:
    print(num1/num2)
    print(module.state['Imo'])
except Exception as e:
    print("This is an attribute error '{}'".format(e))
except Exception as a:
    print("{} can not be divisible by {} this is a '{}' error".format(num1, num2, a))
