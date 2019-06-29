# print(0/0)

num1 = int(input('Enter number1: '))
num2 = int(input('Enter number2: '))
try:
    print(num1/num2)

except:
    print('{} can not be divisible ny {}' .format(num1, num2))
